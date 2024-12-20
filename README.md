TV Show Tracker!

Welcome to the TV Show Tracker App! This application is a place for you to not only keep track of all of your favorite shows, but also keep track of which ones you are watching, want to watch, and even ones you have finished! Along with this, you can rate your shows! 


Table of Contents
-------------------------

-Overview

-Features

-Technologies Used

-Setup Instructions

-Running the Application

-Usage Guide

-Project Structure

Overview
----------------

The TV Show Tracker App is a Flask web application that allows users to keep track of TV shows they want to watch, are currently watching, or have finished. Users can log in, add shows to their tracker, update show statuses, and rate shows!

Features
----------------

-User Registration & Login: Users can create accounts and log in.

-Add Shows to Tracker: Users can add shows from a list of available shows.

-Update Status & Rating: Users can update the status (e.g., "Plan to Watch," "Currently Watching," -"Finished Watching") and rate shows from 1-5.

-Track Viewing Progress: Users can view and manage the progress of each show they are tracking.


Technologies Used
--------------------

-Python with Flask for the web application

-MySQL for the database

-SQLAlchemy for ORM (Object-Relational Mapping)

-HTML and Jinja2 for templating

Setup Instructions
--------------------

To set up this project on your local machine:

Clone the repository:

git clone https://github.com/yourusername/tv-show-tracker-app.git
cd Data_Science_Final


Create a Virtual Environment:

python3 -m venv env
source env/bin/activate  # For macOS/Linux
- or -
env\Scripts\activate  # For Windows


Install Dependencies:

pip install -r requirements.txt
Ensure you have all necessary libraries like Flask, SQLAlchemy, and mysql-connector-python installed.


Set Up the Database:

Create a MySQL database named progress_tracker (or update the code with your database name if it’s different).

Run the SQL script provided (if any) to initialize the tables, or let SQLAlchemy create the tables automatically on first run.


Update Database Credentials:

Open Data_Science_Final.py and update the line below with your own MySQL username and password:
python

Copy code:
engine = create_engine("mysql+mysqlconnector://username:password@localhost/progress_tracker")


Running the Application
--------------------------

Activate the virtual environment:

source env/bin/activate  # For macOS/Linux

-or-

env\Scripts\activate  # For Windows

Run the Flask App:

python Data_Science_Final.py
Open a browser and go to http://127.0.0.1:5000/ to access the app.

Usage Guide
-------------

-Register: Go to the Register page and create a new account.

-Login: After registering, log in to access your tracker.

-View Shows: Visit the Available Shows page to see a list of shows you can track.

-Add Shows: Add shows to your tracker by clicking "Add to Tracker" on the Available Shows page.

-Update Shows: On your Tracker page, update the status (Plan to Watch, Currently Watching, Finished Watching) and rate shows from 1-5.

Project Structure
-------------------

Data_Science_Final.py     # Main Flask application
models.py                 # SQLAlchemy models for User, Topic, and Progress
exceptions.py             # Custom exceptions (e.g., UserAlreadyExistsException)
requirements.txt          # Python dependencies
templates/                # HTML templates for the application
    home.html             # Home page template
    register.html         # User registration template
    login.html            # User login template
    tracker.html          # Tracker template (view and update shows)
    shows.html            # Available shows template
README.md                 # Project documentation
