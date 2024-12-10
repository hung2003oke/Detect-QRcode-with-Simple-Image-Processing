import sqlite3

# Kết nối đến cơ sở dữ liệu SQLite, nếu chưa có file, nó sẽ được tạo mới
conn = sqlite3.connect('database_qrcode.db')

# Tạo đối tượng cursor để thực hiện các truy vấn SQL
cursor = conn.cursor()
cursor.execute('''
CREATE TABLE IF NOT EXISTS products_barcode (
    barcode_code INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    price INTEGER NOT NULL,
    description VARCHAR
)
''')

cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
print(cursor.fetchall())
