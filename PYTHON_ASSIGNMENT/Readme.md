***E- commerce backend project***
----------------------------------------------------------------------

🖥️ **Project Overview:**

This E-commerce Backend API is a modern, scalable, and secure backend solution built with **FastAPI** and **PostgreSQL**.
It provides all the essential features required for an online store, including:

- **User Management:** Registration, login, JWT authentication, and password reset via email.
- **Admin Controls:** Only admins can add, update, or delete products.
- **Product Catalog:** Public endpoints for browsing, searching, and filtering products.
- **Shopping Cart:** Authenticated users can add, update, and remove products from their cart.
- **Order Processing:** Users can place orders and view their order history.
- **Security:** Passwords are hashed, sensitive routes are protected, and role-based access is enforced.
----------------------------------------------------------------------

📜 **Prerequisites:**

Before you begin, ensure you have the following installed on your system:
- **Python 3.8+**
- **PostgreSQL** (for database)
- **Git**
- **Postman**
--------------------------------------------------------------------

👩🏻‍💻 **Technological Stack:**

This project is built using the following technologies:

- **FastAPI** – High-performance Python web framework for building APIs
- **SQLAlchemy** – ORM for database interactions
- **PostgreSQL** – Relational database for data storage
- **Alembic** – Database migrations
- **Pydantic** – Data validation and settings management
- **Uvicorn** – ASGI server for running FastAPI apps
- **Passlib (bcrypt)** – Secure password hashing
- **python-dotenv** – Environment variable management
- **JWT** – Secure authentication tokens
- **Logging** – For tracking application events
- **Email (smtplib)** – For sending password reset emails

-----------------------------------------------------------------------


📁 **Project Structure**

| Folder/File                
|----------------------------
| `app/`                     
| ├── `cart/`                
| ├── `checkout/`            
| ├── `database/`            
| ├── `exception/`           
| ├── `order/`               
| ├── `products/`            
| ├── `users/`               
| ├── `utils/`               
| ├── `logging_config.py`    
| └── `main.py`              
| `alembic/`                 
| ├── `versions/`           
| `requirements.txt`         
| `.env`                     
| `.gitignore`               
| `Readme.md`                
----------------------------------------------------------------------

----------------------------------------------------------------------

⚡ **Setup Instructions**

Follow these steps to set up and run the E-commerce Backend project on your local machine:

1. **Clone the Repository**
    ```sh
    git clone <your-repo-url>
    cd PYTHON_ASSIGNMENT
    ```

2. **Create and Activate a Virtual Environment**
    ```sh
    python -m venv venv
    # On Windows:
    venv\Scripts\activate
    # On macOS/Linux:
    source venv/bin/activate
    ```

3. **Install Dependencies**
    ```sh
    pip install -r requirements.txt
    ```

4. **Configure Environment Variables**
    - Create a `.env` file in the project root with the following content:
      ```
      ://DATABASE_URL=postgresql<username>:<password>@localhost:5432/<your_db>
      EMAIL_PASSWORD=<your_email_password>
      ```
    - Replace `<username>`, `<password>`, `<your_db>`, and `<your_email_password>` with your actual credentials.

5. **Set Up the Database**
    - Make sure PostgreSQL is running and your database exists.
    - Run Alembic migrations to create the tables:
      ```sh
      alembic upgrade head
      ```

6. **Run the Application**
    ```sh
    uvicorn app.main:app --reload
    ```
    - The API will be available at [http://127.0.0.1:8000](http://127.0.0.1:8000)

7. **Access API Documentation**
    - Swagger UI: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
    - ReDoc: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

----------------------------------------------------------------------

**Note:**
- Do **not** commit your `.env` or [venv](http://_vscodecontentref_/0) folders to version control.
- For admin-only routes, ensure your user has the `"admin"` role in the database.

---------------------------------------------------------------------
🚧 **Future Improvements**

- Add unit tests with pytest
- Implement rate limiting
- Integrate with multiple payment gateways
