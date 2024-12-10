# import tkinter as tk
# from tkinter import messagebox
# import cv2
# from PIL import Image, ImageTk
# from src.detect_code.detect_qrcode import recognition_qrcode
#
# class Sign_in:
#     def __int__(self):
#         self.cursor = None
#         self.welcome_frane =
#
#     def show_login_screen(self,welcome_frame,login_frame):
#         welcome_frame.pack_forget()
#         login_frame.pack(pady=20)
#
#     def check_login(self):
#         name = entry_name.get()
#         password = entry_password.get()
#
#         if not name or not password:
#             messagebox.showerror("Error", "Please enter both username and password.")
#             return
#
#         self.cursor.execute("SELECT * FROM user WHERE name = ? AND password = ?", (name, password))
#         result = self.cursor.fetchone()
#
#         if result:
#             messagebox.showinfo("Success", "Login successful!")
#         else:
#             messagebox.showerror("Error", "Invalid username or password.")
#
#     def login(self,entry_user,entry_password,login_frame, user_admin_frame):
#         username = entry_user.get()
#         password = entry_password.get()
#
#         # Kiểm tra tài khoản đúng (ở đây dùng giá trị giả định)
#         if username == "user" and password == "password":
#             login_frame.pack_forget()
#             user_admin_frame.pack(pady=20)
#         else:
#             messagebox.showerror("Lỗi", "Sai tài khoản hoặc mật khẩu")
#
#     # def show_user_frame():
#     #     user_admin_frame.pack_forget()
#     #     user_frame.pack()
#     #     update_frame()
#     def widge(self):
#
#     # Tạo cửa sổ chínha
#         root = tk.Tk()
#         root.title("Giao diện đăng nhập")
#         root.geometry("800x600")
#
#         # Frame chào mừng
#         welcome_frame = tk.Frame(root)
#         welcome_frame.pack(pady=20)
#
#         welcome_label = tk.Label(welcome_frame, text="Chào mừng", font=("Arial", 24))
#         welcome_label.pack()
#
#         welcome_button = tk.Button(welcome_frame, text="Nhấn để tiếp tục", command=show_login_screen)
#         welcome_button.pack(pady=10)
#
#         login_frame = tk.Frame(root)
#
#         label_user = tk.Label(login_frame, text="User:")
#         label_user.grid(row=0, column=0, padx=5, pady=5)
#         entry_user = tk.Entry(login_frame)
#         entry_user.grid(row=0, column=1, padx=5, pady=5)
#
#         label_password = tk.Label(login_frame, text="Password:")
#         label_password.grid(row=1, column=0, padx=5, pady=5)
#         entry_password = tk.Entry(login_frame, show="*")
#         entry_password.grid(row=1, column=1, padx=5, pady=5)
#
#         login_button = tk.Button(login_frame, text="Đăng nhập", command=login)
#         login_button.grid(row=2, columnspan=2, pady=10)
#
#         user_admin_frame = tk.Frame(root)
#         user_button = tk.Button(user_admin_frame, text="User", command=show_user_frame)
#         user_button.pack(side="left", padx=10)
#
#         admin_admin_frame = tk.Frame(root)
#         admin_button = tk.Button(user_admin_frame, text="Admin")
#         admin_button.pack(side="right", padx=10)
#
#         root.mainloop()

import sqlite3
import tkinter as tk
from tkinter import messagebox
from src.detect_code.detect_qrcode import recognition_qrcode


class SignIn:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Giao diện đăng nhập")
        self.root.geometry("800x600")

        # Kết nối đến cơ sở dữ liệu SQLite
        self.conn = sqlite3.connect(r'D:\projects\qr_barcode_xla\src\guide\database_qrcode.db')  # Đảm bảo tên file DB đúng
        self.cursor = self.conn.cursor()

        # Khởi tạo các frame và widget
        self.welcome_frame = tk.Frame(self.root)
        self.login_frame = tk.Frame(self.root)
        self.user_admin_frame = tk.Frame(self.root)
        self.entry_user = None
        self.entry_password = None
        self.create_widgets()

    def show_login_screen(self):
        self.welcome_frame.pack_forget()
        self.login_frame.pack(pady=20)

    def check_login(self):
        name = self.entry_user.get()
        password = self.entry_password.get()

        if not name or not password:
            messagebox.showerror("Error", "Please enter both username and password.")
            return

        # Truy vấn thông tin đăng nhập từ database
        self.cursor.execute("SELECT * FROM manage_user WHERE name = ? AND password = ?", (name, password))
        result = self.cursor.fetchone()

        if result:
            messagebox.showinfo("Success", "Login successful!")
            self.show_user_frame()
        else:
            messagebox.showerror("Error", "Invalid username or password.")

    def login(self):
        # Chuyển hướng xử lý đăng nhập sang hàm check_login
        self.check_login()

    def show_user_frame(self):
        self.login_frame.pack_forget()
        self.user_admin_frame.pack(pady=20)
        tk.Label(self.user_admin_frame, text="Welcome to the user dashboard!", font=("Arial", 18)).pack(pady=10)

    def create_widgets(self):
        # Frame chào mừng
        self.welcome_frame.pack(pady=20)
        welcome_label = tk.Label(self.welcome_frame, text="Chào mừng", font=("Arial", 24))
        welcome_label.pack()
        welcome_button = tk.Button(self.welcome_frame, text="Nhấn để tiếp tục", command=self.show_login_screen)
        welcome_button.pack(pady=10)

        # Frame đăng nhập
        label_user = tk.Label(self.login_frame, text="User:")
        label_user.grid(row=0, column=0, padx=5, pady=5)
        self.entry_user = tk.Entry(self.login_frame)
        self.entry_user.grid(row=0, column=1, padx=5, pady=5)

        label_password = tk.Label(self.login_frame, text="Password:")
        label_password.grid(row=1, column=0, padx=5, pady=5)
        self.entry_password = tk.Entry(self.login_frame, show="*")
        self.entry_password.grid(row=1, column=1, padx=5, pady=5)

        login_button = tk.Button(self.login_frame, text="Đăng nhập", command=self.login)
        login_button.grid(row=2, columnspan=2, pady=10)

        # Frame quản trị người dùng (user admin frame)
        user_button = tk.Button(self.user_admin_frame, text="  User  ", command=self.show_user_frame)
        user_button.pack(side="bottom", padx=10)

        admin_button = tk.Button(self.user_admin_frame, text="Admin")
        admin_button.pack(side="bottom", padx=10)

    def run(self):
        # Chạy vòng lặp chính của ứng dụng tkinter
        self.root.mainloop()

    def __del__(self):
        # Đóng kết nối database khi đối tượng bị hủy
        if self.conn:
            self.conn.close()


# Khởi chạy chương trình
if __name__ == "__main__":
    app = SignIn()
    app.run()

