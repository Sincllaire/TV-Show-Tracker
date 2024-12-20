from sqlalchemy import Column, Integer, String, Date, ForeignKey, Enum
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class User(Base):
    __tablename__ = 'Users'
    user_id = Column(Integer, primary_key=True)
    username = Column(String(255), unique=True, nullable=False)
    password_hash = Column(String(255), nullable=False)

class Topic(Base):
    __tablename__ = 'Topics'
    topic_id = Column(Integer, primary_key=True)
    title = Column(String(255), nullable=False)
    genre = Column(String(255))
    release_date = Column(Date)
    category = Column(String(255), default='TV Show')

class Progress(Base):
    __tablename__ = 'Progress'
    progress_id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('Users.user_id'), nullable=False)
    topic_id = Column(Integer, ForeignKey('Topics.topic_id'), nullable=False)
    status = Column(Enum('Plan to Watch', 'Currently Watching', 'Finished Watching'))
    rating = Column(Integer)
