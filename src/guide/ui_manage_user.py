import sqlite3
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox


class UserManagerApp:
    def __init__(self, root):
        self.root = root
        self.root.title('Quản lý người dùng')

        # Kết nối đến cơ sở dữ liệu SQLite
        self.conn = sqlite3.connect('database_qrcode.db')
        self.cursor = self.conn.cursor()

        # Tạo bảng nếu chưa tồn tại
        self.cursor.execute('''
        CREATE TABLE IF NOT EXISTS manage_user (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            password INTEGER NOT NULL
        )
        ''')

        # Tạo giao diện
        self.create_widgets()

        # Hiển thị dữ liệu ban đầu
        self.display_data()

    def create_widgets(self):
        """Tạo các thành phần giao diện"""
        # Frame bên trái để nhập liệu
        left_frame = tk.Frame(self.root)
        left_frame.pack(side=tk.LEFT, padx=20, pady=20)

        # Ô nhập mã sản phẩm
        tk.Label(left_frame, text="id").pack()
        self.entry_id = tk.Entry(left_frame)
        self.entry_id.pack(pady=5)

        # Ô nhập tên sản phẩm
        tk.Label(left_frame, text="Username").pack()
        self.entry_name = tk.Entry(left_frame)
        self.entry_name.pack(pady=5)

        # Ô nhập giá sản phẩm
        tk.Label(left_frame, text="Password").pack()
        self.entry_password = tk.Entry(left_frame)
        self.entry_password.pack(pady=5)

        # Các nút Thêm, Sửa, Xóa
        btn_add = tk.Button(left_frame, text="Thêm", command=self.add_product)
        btn_add.pack(side=tk.LEFT, padx=5, pady=10)

        btn_update = tk.Button(left_frame, text="Sửa", command=self.update_product)
        btn_update.pack(side=tk.LEFT, padx=5)

        btn_delete = tk.Button(left_frame, text="Xóa", command=self.delete_product)
        btn_delete.pack(side=tk.LEFT, padx=5)

        # Tạo Frame để chứa bảng dữ liệu
        right_frame = tk.Frame(self.root)
        right_frame.pack(side=tk.RIGHT, pady=20)

        # Tạo bảng Treeview
        columns = ('id', 'Username', 'Password')
        self.tree = ttk.Treeview(right_frame, columns=columns, show='headings', height=8)

        # Đặt tên cho các cột
        self.tree.heading('id', text='id')
        self.tree.heading('Username', text='Username')
        self.tree.heading('Password', text='Password')

        self.tree.column('id', width=100)
        self.tree.column('Username', width=150)
        self.tree.column('Password', width=100)

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
        self.cursor.execute("SELECT * FROM manage_user")
        return self.cursor.fetchall()

    def display_data(self):
        """Hiển thị dữ liệu trong Treeview"""
        self.tree.delete(*self.tree.get_children())  # Xóa dữ liệu hiện tại
        for row in self.load_data():
            self.tree.insert('', tk.END, values=row)

    def add_product(self):
        """Thêm sản phẩm mới vào cơ sở dữ liệu"""
        id = self.entry_id.get()
        name = self.entry_name.get()
        password = self.entry_password.get()

        if id and name and password:
            try:
                self.cursor.execute('''
                    INSERT INTO manage_user (id, name, password)
                    VALUES (?, ?, ?)
                ''', (id, name, password))
                self.conn.commit()
                self.display_data()  # Cập nhật lại bảng sau khi thêm
                self.clear_entries()  # Xóa nội dung đã nhập
            except sqlite3.IntegrityError:
                messagebox.showerror("Lỗi", "Mã sản phẩm đã tồn tại.")
        else:
            messagebox.showwarning("Thiếu thông tin", "Vui lòng nhập đầy đủ thông tin.")

    def delete_product(self):
        """Xóa sản phẩm khỏi cơ sở dữ liệu"""
        barcode = self.entry_id.get()
        if barcode:
            self.cursor.execute("DELETE FROM manage_user WHERE id=?", (barcode,))
            self.conn.commit()
            self.display_data()  # Cập nhật lại bảng sau khi xóa
            self.clear_entries()  # Xóa nội dung đã nhập
        else:
            messagebox.showwarning("Thiếu thông tin", "Vui lòng nhập mã sản phẩm để xóa.")

    def update_product(self):
        """Sửa thông tin sản phẩm dựa trên mã barcode"""
        id = self.entry_id.get()
        name = self.entry_name.get()
        password = self.entry_password.get()

        if id and name and password:
            self.cursor.execute('''
                UPDATE manage_user
                SET name = ?, password = ?
                WHERE id = ?
            ''', (name,password, id))
            self.conn.commit()
            self.display_data()  # Cập nhật lại bảng sau khi sửa
            self.clear_entries()  # Xóa nội dung đã nhập
        else:
            messagebox.showwarning("Thiếu thông tin", "Vui lòng nhập đầy đủ thông tin.")

    def clear_entries(self):
        """Xóa nội dung trong các ô nhập liệu"""
        self.entry_id.delete(0, tk.END)
        self.entry_name.delete(0, tk.END)
        self.entry_password.delete(0, tk.END)

    def close_connection(self):
        """Đóng kết nối cơ sở dữ liệu"""
        self.conn.close()


if __name__ == "__main__":
    root = tk.Tk()
    app = UserManagerApp(root)
    root.protocol("WM_DELETE_WINDOW", app.close_connection)  # Đảm bảo đóng DB khi đóng ứng dụng
    root.mainloop()