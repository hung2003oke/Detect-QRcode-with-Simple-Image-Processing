# import sqlite3
# import tkinter as tk
# from tkinter import messagebox
#
# from src.guide.admin.ui_admin import ProductManagerApp
# from src.guide.client.ui_client import Ui_Client
#
#
# class Run_Project:
#     def __init__(self):
#         self.root = tk.Tk()
#         self.root.geometry("1000x800")
#         self.root.title("Main Interface")
#
#         self.conn_user = sqlite3.connect('D:/projects/qr_barcode_xla/src/guide/database_qrcode.db')
#         self.cursor_user = self.conn_user.cursor()
#
#         # Khởi tạo Frame chính
#         self.main_frame = tk.Frame(self.root)
#         self.main_frame.pack(fill="both", expand=True)
#
#         self.login_frame = tk.Frame(self.main_frame)
#         self.user_frame = tk.Frame(self.main_frame)
#         self.admin_frame = tk.Frame(self.main_frame)
#
#         self.create_login_interface()
#
#         # Khởi tạo các ứng dụng con nhưng không hiển thị chúng
#         self.user_app = None
#         self.admin_app = None
#
#     def create_login_interface(self):
#         # Thêm các widget cho Frame đăng nhập
#         self.login_frame.pack(fill="both", expand=True)
#
#         username_label = tk.Label(self.login_frame, text="Username:")
#         username_label.pack(padx=10, pady=5)
#
#         self.entry_name = tk.Entry(self.login_frame)
#         self.entry_name.pack(padx=10, pady=5)
#
#         password_label = tk.Label(self.login_frame, text="Password:")
#         password_label.pack(padx=10, pady=5)
#
#         self.entry_password = tk.Entry(self.login_frame, show="*")
#         self.entry_password.pack(padx=10, pady=5)
#
#         login_button = tk.Button(self.login_frame, text="Login", command=self.check_login)
#         login_button.pack(pady=10)
#
#     def check_login(self):
#         name = self.entry_name.get()
#         password = self.entry_password.get()
#
#         if not name or not password:
#             messagebox.showerror("Error", "Please enter both username and password.")
#             return
#
#         self.cursor_user.execute("SELECT * FROM manage_user WHERE name = ? AND password = ?", (name, password))
#         result = self.cursor_user.fetchone()
#
#         if result:
#             messagebox.showinfo("Success", "Login successful!")
#             self.show_choice_frame()
#         else:
#             messagebox.showerror("Error", "Invalid username or password.")
#
#     def show_choice_frame(self):
#         self.login_frame.pack_forget()
#
#         choice_label = tk.Label(self.main_frame, text="Choose your role:", font=("Arial", 14))
#         choice_label.pack(pady=10)
#
#         user_button = tk.Button(self.main_frame, text="User", command=self.show_user_frame)
#         user_button.pack(pady=5)
#
#         admin_button = tk.Button(self.main_frame, text="Admin", command=self.show_admin_frame)
#         admin_button.pack(pady=5)
#
#     def show_user_frame(self):
#         # Ẩn giao diện lựa chọn và hiển thị giao diện User
#         self.clear_main_frame()
#         self.user_frame.pack(fill="both", expand=True)
#         if not self.user_app:
#             self.user_app = Ui_Client(self.user_frame)
#
#     def show_admin_frame(self):
#         # Ẩn giao diện lựa chọn và hiển thị giao diện Admin
#         self.clear_main_frame()
#         self.admin_frame.pack(fill="both", expand=True)
#         if not self.admin_app:
#             self.admin_app = ProductManagerApp(self.admin_frame)
#
#     def clear_main_frame(self):
#         # Hàm xóa tất cả các widget trong main_frame để chuyển giao diện
#         for widget in self.main_frame.winfo_children():
#             widget.pack_forget()
#
#     def on_closing(self):
#         self.conn_user.close()
#         print("Database connection closed.")
#         self.root.quit()
#
#
# if __name__ == "__main__":
#     project = Run_Project()
#     project.root.protocol("WM_DELETE_WINDOW", project.on_closing)
#     project.root.mainloop()

#
# import sqlite3
# import tkinter as tk
# from tkinter import messagebox
#
# from src.guide.admin.ui_admin import ProductManagerApp
# from src.guide.client.ui_client import Ui_Client
#
# class Run_Project:
#     def __init__(self):
#         self.root = tk.Tk()
#         self.root.geometry("1000x800")
#         self.root.title("Main Interface")
#
#         self.conn_user = sqlite3.connect('D:/projects/qr_barcode_xla/src/guide/database_qrcode.db')
#         self.cursor_user = self.conn_user.cursor()
#
#         # Khởi tạo Frame chính
#         self.main_frame = tk.Frame(self.root)
#         self.main_frame.pack(fill="both", expand=True)
#
#         self.login_frame = tk.Frame(self.main_frame)
#         self.choice_frame = tk.Frame(self.main_frame)
#         self.user_frame = tk.Frame(self.main_frame)
#         self.admin_frame = tk.Frame(self.main_frame)
#
#         self.create_login_interface()
#
#         # Khởi tạo các ứng dụng con nhưng không hiển thị chúng
#         self.user_app = None
#         self.admin_app = None
#
#     def create_login_interface(self):
#         for widget in self.choice_frame.winfo_children():
#             widget.destroy()
#
#         self.clear_main_frame()
#         # Thêm các widget cho Frame đăng nhập
#         self.login_frame.pack(fill="both", expand=True)
#
#         username_label = tk.Label(self.login_frame, text="Username:")
#         username_label.pack(padx=10, pady=5)
#
#         self.entry_name = tk.Entry(self.login_frame)
#         self.entry_name.pack(padx=10, pady=5)
#
#         password_label = tk.Label(self.login_frame, text="Password:")
#         password_label.pack(padx=10, pady=5)
#
#         self.entry_password = tk.Entry(self.login_frame, show="*")
#         self.entry_password.pack(padx=10, pady=5)
#
#         login_button = tk.Button(self.login_frame, text="Login", command=self.check_login)
#         login_button.pack(pady=10)
#
#     def check_login(self):
#         name = self.entry_name.get()
#         password = self.entry_password.get()
#
#         if not name or not password:
#             messagebox.showerror("Error", "Please enter both username and password.")
#             return
#
#         self.cursor_user.execute("SELECT * FROM manage_user WHERE name = ? AND password = ?", (name, password))
#         result = self.cursor_user.fetchone()
#
#         if result:
#             messagebox.showinfo("Success", "Login successful!")
#             self.show_choice_frame()
#         else:
#             messagebox.showerror("Error", "Invalid username or password.")
#
#     def show_choice_frame(self):
#         # Xóa tất cả các widget con của choice_frame trước khi tạo mới
#         for widget in self.choice_frame.winfo_children():
#             widget.destroy()
#
#         self.clear_main_frame()
#
#         choice_label = tk.Label(self.choice_frame, text="Choose your role:", font=("Arial", 14))
#         choice_label.pack(pady=10)
#
#         user_button = tk.Button(self.choice_frame, text="User", command=self.show_user_frame)
#         user_button.pack(pady=5)
#
#         admin_button = tk.Button(self.choice_frame, text="Admin", command=self.show_admin_frame)
#         admin_button.pack(pady=5)
#
#         self.choice_frame.pack(fill="both", expand=True)
#         back_button = tk.Button(self.admin_frame, text="Quay lại", command=self.create_login_interface())
#         back_button.pack(side="bottom", pady=10)
#
#     def show_choice_frame_v2(self):
#         for widget in self.choice_frame.winfo_children():
#             widget.destroy()
#
#         self.clear_main_frame()
#
#
#     def show_user_frame(self):
#         self.clear_main_frame()
#         self.user_frame.pack(fill="both", expand=True)
#
#         if not self.user_app:
#             self.user_app = Ui_Client(self.user_frame)
#
#         back_button = tk.Button(self.user_frame, text="Quay lại", command=self.show_choice_frame)
#         back_button.pack(side="bottom", pady=10)
#
#     def show_admin_frame(self):
#         self.clear_main_frame()
#         self.admin_frame.pack(fill="both", expand=True)
#
#         if not self.admin_app:
#             self.admin_app = ProductManagerApp(self.admin_frame)
#
#         back_button = tk.Button(self.admin_frame, text="Quay lại", command=self.show_choice_frame)
#         back_button.pack(side="bottom", pady=10)
#
#     def clear_main_frame(self):
#         for widget in self.main_frame.winfo_children():
#             widget.pack_forget()
#
#     def on_closing(self):
#         self.conn_user.close()
#         print("Database connection closed.")
#         self.root.quit()
#
#
# if __name__ == "__main__":
#     project = Run_Project()
#     project.root.protocol("WM_DELETE_WINDOW", project.on_closing)
#     project.root.mainloop()

import sqlite3
import tkinter as tk
from tkinter import messagebox


from src.guide.admin.ui_admin import ProductManagerApp
from src.guide.client.ui_client import Ui_Client
from src.QRCodeDetector.main import QRCodeProcessor
# from src.guide.sign_in import show_user_frame


class Run_Project:
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("1000x800")
        self.root.title("Main Interface")
        self.update_job = None
        self.user_app = None

        self.conn_user = sqlite3.connect('D:/projects/qr_barcode_xla/src/guide/database_qrcode.db')
        self.cursor_user = self.conn_user.cursor()

        # Khởi tạo Frame chính
        self.main_frame = tk.Frame(self.root)
        self.main_frame.pack(fill="both", expand=True)

        self.login_frame = tk.Frame(self.main_frame)
        self.choice_frame = tk.Frame(self.main_frame)
        self.user_frame = tk.Frame(self.main_frame)
        self.admin_frame = tk.Frame(self.main_frame)

        self.create_login_interface()

        # Khởi tạo các ứng dụng con nhưng không hiển thị chúng
        self.user_app = None
        self.admin_app = None

    def create_login_interface(self):
        for widget in self.login_frame.winfo_children():
            widget.destroy()
        self.clear_main_frame()
        self.login_frame.pack(fill="both", expand=True)

        username_label = tk.Label(self.login_frame, text="Username:")
        username_label.pack(padx=10, pady=5)

        self.entry_name = tk.Entry(self.login_frame)
        self.entry_name.pack(padx=10, pady=5)

        password_label = tk.Label(self.login_frame, text="Password:")
        password_label.pack(padx=10, pady=5)

        self.entry_password = tk.Entry(self.login_frame, show="*")
        self.entry_password.pack(padx=10, pady=5)

        login_button = tk.Button(self.login_frame, text="Login", command=self.check_login)
        login_button.pack(pady=10)

    def check_login(self):
        name = self.entry_name.get()
        password = self.entry_password.get()
        if name == "admin" and password =="password":
                messagebox.showinfo("Success", "You are Admin , Let's start !")
                self.user_app = self.show_user_frame()
        if not name or not password:
            messagebox.showerror("Error", "Please enter both username and password.")
            return

        self.cursor_user.execute("SELECT * FROM manage_user WHERE name = ? AND password = ?", (name, password))
        result = self.cursor_user.fetchone()

        if result:
            messagebox.showinfo("Success", "Login successful!")
            self.show_choice_frame()

        else:
            messagebox.showerror("Error", "Invalid username or password.")

    def show_choice_frame(self):
        for widget in self.choice_frame.winfo_children():
            widget.destroy()
        self.clear_main_frame()

        choice_label = tk.Label(self.choice_frame, text="Choose your role:", font=("Arial", 14))
        choice_label.pack(pady=10)

        user_button = tk.Button(self.choice_frame, text="User Manage", command=self.show_user_frame)
        user_button.pack(pady=5)

        admin_button = tk.Button(self.choice_frame, text="Admin", command=self.show_admin_frame)
        admin_button.pack(pady=5)

        back_button = tk.Button(self.choice_frame, text="Quay lại", command=self.create_login_interface)
        back_button.pack(pady=10)

        self.choice_frame.pack(fill="both", expand=True)

    def stop_user_frame(self):
        if self.user_app:
            self.user_app.stop_camera()
            self.user_app = None
        self.show_choice_frame()

    def show_user_frame(self):
        self.clear_main_frame()
        self.user_frame.pack(fill="both", expand=True)

        if not self.user_app:
            self.user_app = Ui_Client(self.user_frame)

        # self.user_app.update_frame()

        back_button = tk.Button(self.user_frame, text="Quay lại", command=self.stop_user_frame)
        back_button.pack(side="bottom", pady=10)

    def show_admin_frame(self):
        self.clear_main_frame()
        self.admin_frame.pack(fill="both", expand=True)

        if not self.admin_app:
            self.admin_app = ProductManagerApp(self.admin_frame)

        back_button = tk.Button(self.admin_frame, text="Quay lại", command=self.show_choice_frame)
        back_button.pack(side="bottom", pady=10)



    def clear_main_frame(self):
        for widget in self.main_frame.winfo_children():
            widget.pack_forget()

    def on_closing(self):
        self.conn_user.close()
        print("Database connection closed.")
        self.root.quit()



if __name__ == "__main__":
    project = Run_Project()
    project.root.protocol("WM_DELETE_WINDOW", project.on_closing)
    project.root.mainloop()
