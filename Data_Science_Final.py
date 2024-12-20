from flask import Flask, render_template, request, redirect, url_for, flash, session
from sqlalchemy import create_engine, func
from sqlalchemy.orm import sessionmaker
from models import User, Topic, Progress
from exceptions import UserAlreadyExistsException, InvalidRatingException
import hashlib

app = Flask(__name__)
app.secret_key = "your_secret_key"

# Database setup
engine = create_engine("mysql+mysqlconnector://root:Swagger2002@localhost/progress_tracker")
Session = sessionmaker(bind=engine)
db_session = Session()

# Password hashing function
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

# Register route
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        password_hash = hash_password(password)
        existing_user = db_session.query(User).filter_by(username=username).first()
        if existing_user:
            flash("Username already exists.", "error")
        else:
            new_user = User(username=username, password_hash=password_hash)
            db_session.add(new_user)
            db_session.commit()
            flash("Account created successfully!", "success")
            return redirect(url_for('login'))
    return render_template('register.html')

# Login route
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = hash_password(request.form['password'])
        user = db_session.query(User).filter_by(username=username, password_hash=password).first()
        if user:
            session['user_id'] = user.user_id
            flash("Login successful!", "success")
            return redirect(url_for('tracker'))
        else:
            flash("Invalid login credentials.", "error")
    return render_template('login.html')

# Route to view all available shows with search functionality
@app.route('/shows', methods=['GET', 'POST'])
def shows():
    query = db_session.query(Topic)

    # Search functionality by title or genre
    if request.method == 'POST':
        search_term = request.form.get('search_term')
        if search_term:
            query = query.filter(Topic.title.ilike(f"%{search_term}%") | Topic.genre.ilike(f"%{search_term}%"))

    all_shows = query.all()
    return render_template('shows.html', shows=all_shows)

# Route to add a show to the user's tracker
@app.route('/add_to_tracker/<int:topic_id>', methods=['POST'])
def add_to_tracker(topic_id):
    if 'user_id' not in session:
        flash("Please log in to add shows to your tracker.", "error")
        return redirect(url_for('login'))
    
    user_id = session['user_id']
    existing_progress = db_session.query(Progress).filter_by(user_id=user_id, topic_id=topic_id).first()
    
    if existing_progress:
        flash("Show is already in your tracker.", "info")
    else:
        new_progress = Progress(user_id=user_id, topic_id=topic_id, status="Plan to Watch")
        db_session.add(new_progress)
        db_session.commit()
        flash("Show added to your tracker!", "success")
    
    return redirect(url_for('tracker'))

# Route to view and update the tracker for the logged-in user
@app.route('/tracker')
def tracker():
    if 'user_id' not in session:
        flash("Please log in to view your tracker.", "error")
        return redirect(url_for('login'))
    
    user_id = session['user_id']
    user_progress = db_session.query(Progress).filter_by(user_id=user_id).all()
    shows = []
    
    # Prepare list of shows with average ratings
    for progress in user_progress:
        topic = db_session.query(Topic).get(progress.topic_id)
        avg_rating = db_session.query(func.avg(Progress.rating)).filter(Progress.topic_id == topic.topic_id).scalar()
        shows.append({
            "id": topic.topic_id,
            "title": topic.title,
            "status": progress.status,
            "avg_rating": round(avg_rating, 1) if avg_rating else "No ratings"
        })
    
    return render_template('tracker.html', shows=shows)

# Route to update the status and rating of a show in the user's tracker
@app.route('/update_tracker/<int:topic_id>', methods=['POST'])
def update_tracker(topic_id):
    if 'user_id' not in session:
        flash("Please log in to update your tracker.", "error")
        return redirect(url_for('login'))
    
    user_id = session['user_id']
    status = request.form.get('status')
    rating = request.form.get('rating')
    
    try:
        # Convert rating to an integer if it exists; otherwise, leave it as None
        rating = int(rating) if rating else None

        # Validate rating
        if rating and (rating < 1 or rating > 5):
            flash("Rating must be between 1 and 5.", "error")
            return redirect(url_for('tracker'))

        # Fetch the progress entry for the user and topic
        progress = db_session.query(Progress).filter_by(user_id=user_id, topic_id=topic_id).first()
        
        if progress:
            # Update the status and rating
            progress.status = status
            progress.rating = rating
            db_session.commit()
            flash("Tracker updated successfully!", "success")
        else:
            flash("Show not found in your tracker.", "error")
    
    except ValueError:
        flash("Invalid rating value.", "error")
    
    return redirect(url_for('tracker'))

# Logout route
@app.route('/logout')
def logout():
    session.pop('user_id', None)
    flash("You have been logged out.", "info")
    return redirect(url_for('login'))

# Home page route
@app.route('/')
def home():
    return render_template('home.html')

if __name__ == "__main__":
    app.run(debug=True)
