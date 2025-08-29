from fastapi import FastAPI, HTTPException, Depends, status, APIRouter
from fastapi.security import OAuth2PasswordRequestForm
from app.products import models
from app.users.schema import UserSignup, UserOut
from sqlalchemy.orm import Session
from app.database.database import get_db
from app.users.models import User
from app.utils import oauth2, util
from app.utils.email import sending_email_with_token
from app.utils.util import hash_password
from typing import List
from app.users.models import PasswordResetToken
from app.users.schema import ForgotPassword, ResetPassword
from app.utils.util import hash_password, generate_reset_token
from datetime import datetime
from app.logging_config import logger


router = APIRouter()

# User Authentication and Management Routes
# This api is used for user signup
@router.post("/signup", response_model=UserOut, status_code=status.HTTP_201_CREATED)
def signup(user: UserSignup,db: Session = Depends(get_db))-> UserOut:
    """
    Register a new user.

    Args:
        user (UserSignup): User signup data.
        db (Session): Database session.

    Returns:
        UserOut: The created user.

    Raises:
        HTTPException: If the email already exists.
    """
    existing_user = db.query(User).filter(User.email == user.email).first()
    # Check if the user already exists
    if existing_user:
        logger.warning(f"Signup failed: Email already exists for {user.email}")
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Email already exists."
        )
    user_data = user.dict()
    user_data["password"] = hash_password(user_data["password"])
    logger.info(f"Signup attempt for email: {user.email}")
    print(user_data)
    new_user = User(**user_data)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    logger.info(f"User created: {new_user.id}")
    return new_user


# This api is used for user login
@router.post("/login")
def login(user_credentials:  OAuth2PasswordRequestForm=Depends(), db:  Session = Depends(get_db))-> dict:
    """
    Authenticate a user and return an access token.

    Args:
        user_credentials (OAuth2PasswordRequestForm): User login credentials.
        db (Session): Database session.

    Returns:
        dict: Access token and token type.

    Raises:
        HTTPException: If user is not found or password is incorrect.
    """
    logger.info(f"Login attempt for username: {user_credentials.username}")
    user = db.query(User).filter(User.email == user_credentials.username).first()
    # Check if the user exists
    if not user:
        logger.warning(f"Login failed: User not found for {user_credentials.username}")
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found"
        )
    # Verify the password
    if not util.verify_password(user_credentials.password, user.password):
        logger.warning(f"Login failed: Incorrect password for {user_credentials.username}")
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Incorrect password"
        )
    
    access_token = oauth2.create_access_token(data={"user_id": user.id})
    logger.info(f"Login successful for user {user.id}")
    return {"access_token": access_token, "token_type": "bearer"}


# This api is used to get the details of the user
@router.get("/getAllUsers", response_model=List[UserOut])
def get_all_users(db:Session = Depends(get_db))-> List[UserOut]:
    """
    Retrieve all users.

    Args:
        db (Session): Database session.

    Returns:
        List[UserOut]: List of all users.

    Raises:
        HTTPException: If no users are found.
    """
    logger.info("Fetching all users")
    users = db.query(User).all()
    # Check if users exist
    if not users:
        logger.warning("No users found!")
        raise HTTPException(status_code=404, detail="No users found!")
    logger.info(f"Found {len(users)} users")
    return users


# This api is used for user forgot password functionality
@router.post("/forgot-password")
def secure_forgot_password(request: ForgotPassword, db: Session = Depends(get_db))-> dict:
    """
    Generate and send a password reset token to the user's email.

    Args:
        request (ForgotPassword): Email for password reset.
        db (Session): Database session.

    Returns:
        dict: Message and reset token.

    Raises:
        HTTPException: If user is not found.
    """
    logger.info(f"Password reset requested for email: {request.email}")
    user = db.query(User).filter(User.email == request.email).first()
    # Check if the user exists
    if not user:
        logger.warning(f"Password reset failed: User not found for {request.email}")
        raise HTTPException(status_code=404, detail="User not found.")

    token, expires_at = generate_reset_token()
    reset_token = PasswordResetToken(token=token, user_id=user.id, expires_at=expires_at)
    db.add(reset_token)
    db.commit()
    # Send the reset token to the user's email
    sender = "bundeladisha05@gmail.com"
    receiver = user.email
    receiver_name = user.name
    reset_token = reset_token.token
    sending_email_with_token(sender=sender,receiver=receiver,reset_token=reset_token,receiver_name=receiver_name)



    logger.info(f"Reset token created for user {user.id}")
    return {"message": "Reset token created", "token": token}


# This api is used for user password reset functionality
@router.post("/reset-password")
def secure_reset_password(request: ResetPassword, db: Session = Depends(get_db))-> dict:
    """
    Reset the user's password using a valid reset token.

    Args:
        request (ResetPassword): Token and new password.
        db (Session): Database session.

    Returns:
        dict: Success message.

    Raises:
        HTTPException: If token is invalid/expired or user not found.
    """
    logger.info(f"Password reset attempt with token: {request.token}")
    token_entry = db.query(PasswordResetToken).filter(PasswordResetToken.token == request.token).first()
    # Check if the token is valid and not expired
    if not token_entry or token_entry.expires_at < datetime.utcnow():
        logger.warning(f"Invalid or expired token used: {request.token}")
        raise HTTPException(status_code=400, detail="Invalid or expired token.")

    user = db.query(User).filter(User.id == token_entry.user_id).first()
    # Check if the user exists
    if not user:
        logger.warning(f"Password reset failed: User not found for token {request.token}")
        raise HTTPException(status_code=404, detail="User not found.")

    user.password = hash_password(request.new_password)
    logger.info(f"Password updated for user {user.id}")

    # Invalidate token after use
    db.delete(token_entry)
    db.commit()
    logger.info(f"Reset token invalidated for user {user.id}")
    return {"message": "Password successfully reset"}

