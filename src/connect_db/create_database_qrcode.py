import sqlite3
conn = sqlite3.connect('database_qrcode.db')

cursor = conn.cursor()
# cursor.execute('''
# CREATE TABLE IF NOT EXISTS products_qrcode (
#     qr_code INTEGER PRIMARY KEY,
#     name TEXT NOT NULL,
#     price INTEGER NOT NULL,
#     description VARCHAR
# )
# ''')
#
# cursor.execute('''
# INSERT INTO products_qrcode (qr_code, name, price, description)
# VALUES (167893939348, 'Sạc dự phòng', 100000, 'Sạc dự phòng anker có dung lượng 10000mah giúp bạn sử dụng này dài mà không lo về pin')
# ''')
#
# cursor.execute('''
# INSERT INTO products_qrcode (qr_code, name, price, description)
# VALUES (232434234356, 'Ai Phone', 20000000, 'Ai Phone 16 Pro Max Ultra Ultimate Speciel bản TiTan Biển Xa Mạc với chip A18 ')
# ''')
#
# cursor.execute('''
# INSERT INTO products_qrcode (qr_code, name, price, description)
# VALUES (353267895356, 'Doc sạc', 150000, 'Doc sạc công suất 120w sạc siêu nhanh')
# ''')
cursor.execute('''
DELETE FROM products_qrcode WHERE qr_code = 3
''')
conn.commit()

# Truy vấn và in ra tất cả các bản ghi từ bảng products_qrcode
cursor.execute("SELECT * FROM products_qrcode")
rows = cursor.fetchall()
for row in rows:
    print(row)

# Đóng kết nối
conn.close()
