# import cv2
# import sqlite3
# import tkinter as tk
# from tkinter import ttk
#
# # Kết nối đến cơ sở dữ liệu SQLite, nếu chưa có file, nó sẽ được tạo mới
# conn = sqlite3.connect('database_tqrcode.db')
#
# # Tạo đối tượng cursor để thực hiện các truy vấn SQL
# cursor = conn.cursor()
#
# # Tạo bảng nếu chưa tồn tại
# cursor.execute('''
# CREATE TABLE IF NOT EXISTS products_barcode (
#     barcode_code INTEGER PRIMARY KEY,
#     name TEXT NOT NULL,
#     price INTEGER NOT NULL,
#     description VARCHAR
# )
# ''')
#
# # Thêm dữ liệu mẫu vào bảng nếu cần (bỏ qua nếu bảng đã có dữ liệu)
# cursor.execute('''INSERT OR IGNORE INTO products_barcode (barcode_code, name, price, description)
#                   VALUES (123456, 'Product 1', 10000, 'Description 1'),
#                          (789012, 'Product 2', 20000, 'Description 2'),
#                          (345678, 'Product 3', 15000, 'Description 3')''')
# conn.commit()
#
# # Hàm để lấy dữ liệu từ bảng products_barcode
# def load_data():
#     cursor.execute("SELECT * FROM products_barcode")
#     return cursor.fetchall()
#
# # Hàm để hiển thị dữ liệu trong Treeview (bảng dữ liệu)
# def display_data():
#     for row in load_data():
#         tree.insert('', tk.END, values=row)
#
# # Tạo cửa sổ Tkinter
# root = tk.Tk()
# root.title('Danh sách sản phẩm')
#
# # Tạo Frame để chứa bảng dữ liệu
# frame = tk.Frame(root)
# frame.pack(pady=20)
#
# # Tạo bảng Treeview
# columns = ('barcode_code', 'name', 'price', 'description')
# tree = ttk.Treeview(frame, columns=columns, show='headings')
#
# # Đặt tên cho các cột
# tree.heading('barcode_code', text='Barcode')
# tree.heading('name', text='Tên sản phẩm')
# tree.heading('price', text='Giá')
# tree.heading('description', text='Mô tả')
#
# # Đặt kích thước cho các cột
# tree.column('barcode_code', width=100)
# tree.column('name', width=150)
# tree.column('price', width=100)
# tree.column('description', width=200)
#
# # Thêm bảng Treeview vào Frame
# tree.pack()
#
# # Hiển thị dữ liệu lên bảng
# display_data()
#
# # Chạy vòng lặp Tkinter
# root.mainloop()
#
# # Đóng kết nối cơ sở dữ liệu khi kết thúc chương trình
# conn.close()
#

import sqlite3
import tkinter as tk
from tkinter import ttk

# Kết nối đến cơ sở dữ liệu SQLite, nếu chưa có file, nó sẽ được tạo mới
conn = sqlite3.connect('database_qrcode.db')

# Tạo đối tượng cursor để thực hiện các truy vấn SQL
cursor = conn.cursor()

# Tạo bảng nếu chưa tồn tại
cursor.execute('''
CREATE TABLE IF NOT EXISTS products_barcode (
    barcode_code INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    price INTEGER NOT NULL,
    description VARCHAR
)
''')

# Thêm dữ liệu mẫu vào bảng nếu cần (bỏ qua nếu bảng đã có dữ liệu)
cursor.execute('''INSERT OR IGNORE INTO products_barcode (barcode_code, name, price, description)
                  VALUES (123456, 'Product 1', 10000, 'Description 1'),
                         (789012, 'Product 2', 20000, 'Description 2'),
                         (345678, 'Product 3', 15000, 'Description 3')''')
conn.commit()

# Hàm để lấy dữ liệu từ bảng products_barcode
def load_data():
    cursor.execute("SELECT * FROM products_barcode")
    return cursor.fetchall()

# Hàm để hiển thị dữ liệu trong Treeview (bảng dữ liệu)
def display_data():
    for row in load_data():
        tree.insert('', tk.END, values=row)

# Tạo cửa sổ Tkinter
root = tk.Tk()
root.title('Danh sách sản phẩm')

# Tạo Frame để chứa bảng dữ liệu
frame = tk.Frame(root)
frame.pack(pady=20)

# Tạo bảng Treeview với các dòng kẻ
style = ttk.Style()
style.configure("Treeview",
                background="white",
                foreground="black",
                rowheight=25,
                fieldbackground="white")
style.map('Treeview', background=[('selected', 'blue')])

columns = ('barcode_code', 'name', 'price', 'description')
tree = ttk.Treeview(frame, columns=columns, show='headings', height=8)

# Đặt tên cho các cột
tree.heading('barcode_code', text='Barcode')
tree.heading('name', text='Tên sản phẩm')
tree.heading('price', text='Giá')
tree.heading('description', text='Mô tả')

# Đặt kích thước cho các cột
tree.column('barcode_code', width=100)
tree.column('name', width=150)
tree.column('price', width=100)
tree.column('description', width=500)  # Tăng kích thước cột mô tả để chứa dữ liệu dài

# Thêm bảng Treeview vào Frame
tree.grid(row=0, column=0, sticky='nsew')

# Thêm thanh cuộn dọc (vertical scrollbar)
scrollbar_y = ttk.Scrollbar(frame, orient=tk.VERTICAL, command=tree.yview)
tree.configure(yscrollcommand=scrollbar_y.set)
scrollbar_y.grid(row=0, column=1, sticky='ns')

# Thêm thanh cuộn ngang (horizontal scrollbar)
scrollbar_x = ttk.Scrollbar(frame, orient=tk.HORIZONTAL, command=tree.xview)
tree.configure(xscrollcommand=scrollbar_x.set)  # Liên kết Treeview với thanh cuộn ngang
scrollbar_x.grid(row=1, column=0, sticky='ew')

# Cấu hình khung để kích thước Treeview có thể điều chỉnh
frame.grid_rowconfigure(0, weight=1)
frame.grid_columnconfigure(0, weight=1)

# Hiển thị dữ liệu lên bảng
display_data()

# Chạy vòng lặp Tkinter
root.mainloop()

# Đóng kết nối cơ sở dữ liệu khi kết thúc chương trình
conn.close()

