class Queries:
    CREATE_TABLE_REVIEWS = '''
    CREATE TABLE IF NOT EXISTS reviews (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    tg_id INTEGER,
    name VARCHAR(255),
    instagram_username VARCHAR(255),
    visit_date VARCHAR(255),
    food_rating VARCHAR(255),
    cleanliness_rating VARCHAR(255),
    extra_comments TEXT)'''