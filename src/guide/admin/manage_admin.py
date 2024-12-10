import sqlite3
import tkinter as tk
from tkinter import ttk, messagebox

class ManageAdmin:
    def __init__(self, parent_frame):
        self.parent_frame = parent_frame  # Sử dụng Frame cha được truyền vào

        # Kết nối đến cơ sở dữ liệu SQLite
        self.conn = sqlite3.connect('database_qrcode.db')
        self.cursor = self.conn.cursor()

        # Tạo bảng nếu chưa tồn tại
        self.cursor.execute('''
        CREATE TABLE IF NOT EXISTS products_barcode (
            barcode_code INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            price INTEGER NOT NULL,
            description VARCHAR
        )
        ''')

        # Tạo giao diện
        self.create_widgets()

        # Hiển thị dữ liệu ban đầu
        self.display_data()

    def create_widgets(self):
        """Tạo các thành phần giao diện"""
        # Frame bên trái để nhập liệu
        left_frame = tk.Frame(self.parent_frame)
        left_frame.pack(side=tk.LEFT, padx=20, pady=20)

        # Ô nhập mã sản phẩm
        tk.Label(left_frame, text="Mã sản phẩm").pack()
        self.entry_barcode = tk.Entry(left_frame)
        self.entry_barcode.pack(pady=5)

        # Ô nhập tên sản phẩm
        tk.Label(left_frame, text="Tên sản phẩm").pack()
        self.entry_name = tk.Entry(left_frame)
        self.entry_name.pack(pady=5)

        # Ô nhập giá sản phẩm
        tk.Label(left_frame, text="Giá sản phẩm").pack()
        self.entry_price = tk.Entry(left_frame)
        self.entry_price.pack(pady=5)

        # Ô nhập mô tả sản phẩm
        tk.Label(left_frame, text="Mô tả").pack()
        self.entry_description = tk.Entry(left_frame)
        self.entry_description.pack(pady=5)

        # Các nút Thêm, Sửa, Xóa
        btn_add = tk.Button(left_frame, text="Thêm", command=self.add_product)
        btn_add.pack(side=tk.LEFT, padx=5, pady=10)

        btn_update = tk.Button(left_frame, text="Sửa", command=self.update_product)
        btn_update.pack(side=tk.LEFT, padx=5)

        btn_delete = tk.Button(left_frame, text="Xóa", command=self.delete_product)
        btn_delete.pack(side=tk.LEFT, padx=5)

        # Tạo Frame để chứa bảng dữ liệu
        right_frame = tk.Frame(self.parent_frame)
        right_frame.pack(side=tk.RIGHT, pady=20)

        # Tạo bảng Treeview
        columns = ('barcode_code', 'name', 'price', 'description')
        self.tree = ttk.Treeview(right_frame, columns=columns, show='headings', height=8)

        # Đặt tên cho các cột
        self.tree.heading('barcode_code', text='Barcode')
        self.tree.heading('name', text='Tên sản phẩm')
        self.tree.heading('price', text='Giá')
        self.tree.heading('description', text='Mô tả')

        # Đặt kích thước cho các cột
        self.tree.column('barcode_code', width=100)
        self.tree.column('name', width=150)
        self.tree.column('price', width=100)
        self.tree.column('description', width=300)

        self.tree.grid(row=0, column=0, sticky='nsew')

        # Thêm thanh cuộn dọc
        scrollbar_y = ttk.Scrollbar(right_frame, orient=tk.VERTICAL, command=self.tree.yview)
        self.tree.configure(yscrollcommand=scrollbar_y.set)
        scrollbar_y.grid(row=0, column=1, sticky='ns')

        # Thêm thanh cuộn ngang
        scrollbar_x = ttk.Scrollbar(right_frame, orient=tk.HORIZONTAL, command=self.tree.xview)
        self.tree.configure(xscrollcommand=scrollbar_x.set)
        scrollbar_x.grid(row=1, column=0, sticky='ew')

    def load_data(self):
        """Lấy dữ liệu từ bảng products_barcode"""
        self.cursor.execute("SELECT * FROM products_barcode")
        return self.cursor.fetchall()

    def display_data(self):
        """Hiển thị dữ liệu trong Treeview"""
        self.tree.delete(*self.tree.get_children())  # Xóa dữ liệu hiện tại
        for row in self.load_data():
            self.tree.insert('', tk.END, values=row)

    def add_product(self):
        """Thêm sản phẩm mới vào cơ sở dữ liệu"""
        barcode = self.entry_barcode.get()
        name = self.entry_name.get()
        price = self.entry_price.get()
        description = self.entry_description.get()

        if barcode and name and price:
            try:
                self.cursor.execute('''
                    INSERT INTO products_barcode (barcode_code, name, price, description)
                    VALUES (?, ?, ?, ?)
                ''', (barcode, name, price, description))
                self.conn.commit()
                self.display_data()  # Cập nhật lại bảng sau khi thêm
                self.clear_entries()  # Xóa nội dung đã nhập
            except sqlite3.IntegrityError:
                messagebox.showerror("Lỗi", "Mã sản phẩm đã tồn tại.")
        else:
            messagebox.showwarning("Thiếu thông tin", "Vui lòng nhập đầy đủ thông tin.")

    def delete_product(self):
        """Xóa sản phẩm khỏi cơ sở dữ liệu"""
        barcode = self.entry_barcode.get()
        if barcode:
            self.cursor.execute("DELETE FROM products_barcode WHERE barcode_code=?", (barcode,))
            self.conn.commit()
            self.display_data()  # Cập nhật lại bảng sau khi xóa
            self.clear_entries()  # Xóa nội dung đã nhập
        else:
            messagebox.showwarning("Thiếu thông tin", "Vui lòng nhập mã sản phẩm để xóa.")

    def update_product(self):
        """Sửa thông tin sản phẩm dựa trên mã barcode"""
        barcode = self.entry_barcode.get()
        name = self.entry_name.get()
        price = self.entry_price.get()
        description = self.entry_description.get()

        if barcode and name and price:
            self.cursor.execute('''
                UPDATE products_barcode
                SET name = ?, price = ?, description = ?
                WHERE barcode_code = ?
            ''', (name, price, description, barcode))
            self.conn.commit()
            self.display_data()
            self.clear_entries()
        else:
            messagebox.showwarning("Thiếu thông tin", "Vui lòng nhập đầy đủ thông tin.")

    def clear_entries(self):
        """Xóa nội dung trong các ô nhập liệu"""
        self.entry_barcode.delete(0, tk.END)
        self.entry_name.delete(0, tk.END)
        self.entry_price.delete(0, tk.END)
        self.entry_description.delete(0, tk.END)

    def close_connection(self):
        """Đóng kết nối cơ sở dữ liệu"""
        self.conn.close()

if __name__ == "__main__":
    root = tk.Tk()
    app = ProductManagerApp(root)
    root.protocol("WM_DELETE_WINDOW", app.close_connection)
    root.mainloop()