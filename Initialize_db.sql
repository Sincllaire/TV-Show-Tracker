-- Create and use the database
CREATE DATABASE IF NOT EXISTS progress_tracker;
USE progress_tracker;

-- Users Table
CREATE TABLE IF NOT EXISTS Users (
    user_id INTEGER PRIMARY KEY AUTO_INCREMENT,
    username VARCHAR(255) UNIQUE NOT NULL,
    password_hash VARCHAR(255) NOT NULL
);

-- Topics Table (TV Shows)
CREATE TABLE IF NOT EXISTS Topics (
    topic_id INTEGER PRIMARY KEY AUTO_INCREMENT,
    title VARCHAR(255) NOT NULL,
    release_date DATE,
    category VARCHAR(100) DEFAULT 'TV Show'
);

-- Genres Table (Normalized)
CREATE TABLE IF NOT EXISTS Genres (
    genre_id INTEGER PRIMARY KEY AUTO_INCREMENT,
    genre_name VARCHAR(100) NOT NULL UNIQUE
);

-- TopicGenres Table (Link Topics and Genres - Many-to-Many Relationship)
CREATE TABLE IF NOT EXISTS TopicGenres (
    topic_id INTEGER NOT NULL,
    genre_id INTEGER NOT NULL,
    PRIMARY KEY (topic_id, genre_id),
    FOREIGN KEY (topic_id) REFERENCES Topics(topic_id) ON DELETE CASCADE,
    FOREIGN KEY (genre_id) REFERENCES Genres(genre_id) ON DELETE CASCADE
);

-- Progress Table (Track User's Progress)
CREATE TABLE IF NOT EXISTS Progress (
    progress_id INTEGER PRIMARY KEY AUTO_INCREMENT,
    user_id INTEGER NOT NULL,
    topic_id INTEGER NOT NULL,
    status VARCHAR(50) CHECK (status IN ('Plan to Watch', 'Currently Watching', 'Finished Watching')),
    rating INTEGER CHECK (rating BETWEEN 1 AND 5),
    FOREIGN KEY (user_id) REFERENCES Users(user_id) ON DELETE CASCADE,
    FOREIGN KEY (topic_id) REFERENCES Topics(topic_id) ON DELETE CASCADE
);

-- Optional: Insert Sample Data into Users Table
INSERT INTO Users (username, password_hash)
VALUES 
    ('johndoe', '5e884898da28047151d0e56f8dc6292773603d0d6aabbdd9bcbf7b6f9a1d4f7'), -- Example hash for 'password'
    ('janedoe', '6cb75f652a9b52798eb6cf2201057c73e067d3994f172b717c7b1e7bfb76e5'); -- Example hash for 'password123'

-- Optional: Insert Sample Data into Topics Table
INSERT INTO Topics (title, release_date, category)
VALUES 
    ('Breaking Bad', '2008-01-20', 'TV Show'),
    ('Stranger Things', '2016-07-15', 'TV Show'),
    ('The Office', '2005-03-24', 'TV Show');

-- Optional: Insert Sample Data into Genres Table
INSERT INTO Genres (genre_name)
VALUES 
    ('Drama'),
    ('Sci-Fi'),
    ('Comedy');

-- Optional: Insert Sample Data into TopicGenres Table (Linking Topics and Genres)
INSERT INTO TopicGenres (topic_id, genre_id)
VALUES 
    (1, 1), -- Breaking Bad -> Drama
    (2, 2), -- Stranger Things -> Sci-Fi
    (3, 3); -- The Office -> Comedy

-- Optional: Insert Sample Data into Progress Table
INSERT INTO Progress (user_id, topic_id, status, rating)
VALUES 
    (1, 1, 'Finished Watching', 5),
    (1, 2, 'Currently Watching', 4),
    (2, 3, 'Plan to Watch', NULL);
