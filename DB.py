import sqlite3

conn = sqlite3.connect('shop_database.db')

cursor = conn.cursor()



# create_table_users = """
# CREATE TABLE IF NOT EXISTS users (
#     id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
#     username TEXT NOT NULL,
#     password TEXT NOT NULL,
#     email TEXT NOT NULL,
#     role TEXT CHECK(role IN ('admin', 'user')) NOT NULL,
#     purchase_count INTEGER DEFAULT 0,
#     created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
# );
# """

# create_table_categories = """
# CREATE TABLE IF NOT EXISTS categories (
#     id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
#     name TEXT NOT NULL,
#     description TEXT
# );
# """

# create_table_products = """
# CREATE TABLE IF NOT EXISTS products (
#     id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
#     name TEXT NOT NULL,
#     description TEXT,
#     price DECIMAL(10, 2) NOT NULL,
#     image_url TEXT,
#     category_id INTEGER,
#     likes INTEGER DEFAULT 0,
#     created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
#     FOREIGN KEY (category_id) REFERENCES categories(id)
# );
# """

# create_table_comments = """
# CREATE TABLE IF NOT EXISTS comments (
#     id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
#     user_id INTEGER,
#     product_id INTEGER,
#     comment TEXT NOT NULL,
#     created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
#     FOREIGN KEY (user_id) REFERENCES users(id),
#     FOREIGN KEY (product_id) REFERENCES products(id)
# );
# """

# create_table_orders = """
# CREATE TABLE IF NOT EXISTS orders (
#     id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
#     user_id INTEGER,
#     customer_name TEXT NOT NULL,
#     phone_number TEXT NOT NULL,
#     address TEXT NOT NULL,
#     total_amount DECIMAL(10, 2) NOT NULL,
#     payment_link TEXT NOT NULL,
#     payment_status TEXT CHECK(payment_status IN ('pending', 'paid', 'failed')) DEFAULT 'pending',
#     created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
#     FOREIGN KEY (user_id) REFERENCES users(id)
# );
# """

# cursor.execute(create_table_users)
# cursor.execute(create_table_categories)
# cursor.execute(create_table_products)
# cursor.execute(create_table_comments)
# cursor.execute(create_table_orders)

conn.commit()
conn.close()

# print("Database and tables created successfully.")
print("Users added successfully.")
