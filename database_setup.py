from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

try:
    from models import Base  # Attempt to import models
except ImportError:
    print("Could not import 'models'. Make sure the path is correct and 'models.py' exists in the project folder.")
    raise  # Raise the error to halt execution if models cannot be found

# Replace `username`, `password`, and `database_name` with your actual MySQL details
engine = create_engine("mysql+mysqlconnector://root:your_password@localhost/progress_tracker")
Session = sessionmaker(bind=engine)
session = Session()

# Attempt to create all tables in the database
try:
    Base.metadata.create_all(engine)
    print("Database tables created successfully.")
except Exception as e:
    print(f"An error occurred while creating the tables: {e}")
