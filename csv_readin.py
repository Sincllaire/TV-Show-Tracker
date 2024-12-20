import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Topic
import os

# Set up the database connection, make sure to replace the root and password
engine = create_engine("mysql+mysqlconnector://root:your_password@localhost/progress_tracker")  # Replace with your credentials

# Load the CSV file using a relative path
csv_path = os.path.join(os.path.dirname(__file__), 'data', 'imdb_tvshows.csv')
data = pd.read_csv(csv_path)

# Create a session to interact with the database
Session = sessionmaker(bind=engine)
session = Session()

# Insert data into the Topics table
for _, row in data.iterrows():
    # Extract the release year, handling values like '2019– ' by taking only the starting year
    release_year = row['Years'].split('–')[0].strip()  # Get the start year and strip any whitespace

    # Convert to date or set as None if invalid
    try:
        release_date = f"{release_year}-01-01" if release_year.isdigit() else None  # Set to 'YYYY-01-01' format
    except ValueError:
        release_date = None  # If the conversion fails, set to None

    # Create a new Topic instance with cleaned data
    new_topic = Topic(
        title=row['Title'],
        genre=row['Genres'],
        release_date=release_date,  # Use the cleaned release_date
        category='TV Show'
    )
    session.add(new_topic)

# Commit the transaction
session.commit()
print("Data loaded successfully into the Topics table.")

