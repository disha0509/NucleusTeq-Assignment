from jose import JWTError, jwt
from datetime import datetime, timedelta
from sqlalchemy.orm import Session
from app.database.database import get_db
from app.users.models import User
from app.users.schema import TokenData

#Secret key
#algorithm
#expiration time

SECRET_KEY = "kcRUxml0h4hFSwcbVS44qNnmRBelQeow"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30


# Create a JWT access token with an expiration time.
def create_access_token(data: dict)-> str:
    """
    Create a JWT access token.

    Args:
        data (dict): Data to encode in the token.

    Returns:
        str: Encoded JWT token as a string.
    """
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


# Verify a JWT access token and extract the token data.
def verify_access_token(token: str, credentials_exception) -> TokenData:
    """
    Verify a JWT access token and extract the token data.

    Args:
        token (str): JWT token to verify.
        credentials_exception (HTTPException): Exception to raise if verification fails.

    Returns:
        TokenData: Token data containing the user ID.

    Raises:
        HTTPException: If the token is invalid or expired.
    """
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        id: str = payload.get("user_id")
        # Check if the user_id is present in the token payload
        if id is None:
            raise credentials_exception
        token_data = TokenData(id = id)
        
    except JWTError:
        # If the token is invalid or expired, raise an exception
        raise credentials_exception
    return token_data


from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")  # or your login endpoint


# Dependency to get the current user from the JWT token
def get_current_user(
    token: str = Depends(oauth2_scheme),
    db: Session = Depends(get_db)
) -> User:
    """
    Dependency to retrieve the currently authenticated user from the JWT token.

    Args:
        token (str): JWT token extracted from the request.
        db (Session): Database session.

    Returns:
        User: The authenticated user object.

    Raises:
        HTTPException: If the token is invalid or user does not exist.
    """
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    token_data = verify_access_token(token, credentials_exception)
    user = db.query(User).filter(User.id == token_data.id).first()
    # Check if user exists
    if user is None:
        raise credentials_exception
    return user