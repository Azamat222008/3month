class Queries:
    CREATE_TABLE_REVIEWS = '''
    CREATE TABLE IF NOT EXISTS reviews (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    tg_id INTEGER,
    name VARCHAR(255),
    instagram_username VARCHAR(255),
    visit_date VARCHAR(255),
    food_rating INTEGER,
    cleanliness_rating INTEGER,
    extra_comments TEXT)'''


    CREATE_TABLE_CATEGORIES = '''
    CREATE TABLE IF NOT EXISTS categories (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(255),
    UNIQUE (name))'''


    CREATE_TABLE_DISHES = '''
    CREATE TABLE IF NOT EXISTS dishes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title VARCHAR(255),
    price INTEGER,
    photo TEXT,
    category_id INTEGER,
    UNIQUE (title)
    FOREIGN KEY(category_id) REFERENCES categories (id))'''





    INSERT_INTO_CAT = '''
    INSERT OR IGNORE INTO categories (name) VALUES ('drinks'),('soups'),('salads')'''


    INSERT_INTO_DISHES = '''
    INSERT OR IGNORE INTO dishes (title,price,photo,category_id) VALUES ('Борщ',200,'images/borsch.jfif',2),
    ('Цезарь',250,'images/caesar.jfif',3),
    ('Кола',60,'images/coke.jfif',1),
    ('Греческий салат',230,'images/greek.jfif',3),
    ('Грибной суп',220,'images/mushrooms.jfif',2),
    ('Чай',30,'images/tea.jfif',1)'''

