from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = 'postgresql://postgres:Anjali#123@localhost/e-commerce'


#Creates a SQLAlchemy engine, which manages the connection pool and database communication.
engine = create_engine(SQLALCHEMY_DATABASE_URL)

# Creates a session factory bound to the engine, which is used to create new Session objects.
sessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


Base = declarative_base()
def get_db():
    db = sessionLocal()
    try:
        yield db
    finally:
        db.close()
        