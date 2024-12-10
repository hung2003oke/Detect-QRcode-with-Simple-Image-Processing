# import tkinter as tk
# from tkinter import messagebox,filedialog
# import cv2
# from PIL import Image, ImageTk
# from src.detect_code.detect_qrcode import recognition_qrcode
# # Hàm để chuyển sang màn hình đăng nhập
# def show_login_screen():
#     welcome_frame.pack_forget()
#     login_frame.pack(pady=20)
#
# # Hàm xử lý khi nhấn nút đăng nhập
# def login():
#     username = entry_user.get()
#     password = entry_password.get()
#
#     # Kiểm tra tài khoản đúng (ở đây dùng giá trị giả định)
#     if username == "user" and password == "password":
#         login_frame.pack_forget()
#         user_admin_frame.pack(pady=20)
#     else:
#         messagebox.showerror("Lỗi", "Sai tài khoản hoặc mật khẩu")
#
# def show_user_frame():
#     user_admin_frame.pack_forget()
#     user_frame.pack()
#     update_frame()
#
# def capture_image():
#     ret, frame = cap.read()
#     # if ret:
#     #     file_path = filedialog.asksaveasfilename(defaultextension=".jpg",filetypes = [("JPEG files","*.jpg"),("All files","*")])
#     #     if file_path:
#     #         cv2.imwrite(file_path,frame)
#     data = recognition_qrcode(frame)
#     return data
#
#
#
# def update_frame():
#     # Đọc khung hình từ camera
#     ret, frame = cap.read()
#
#     if ret:
#         # Chuyển đổi từ BGR (OpenCV) sang RGB (Tkinter có thể hiển thị)
#         frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
#         img = Image.fromarray(frame_rgb)
#         imgtk = ImageTk.PhotoImage(image=img)
#
#         # Hiển thị khung hình trên label
#         camera_label.imgtk = imgtk
#         camera_label.configure(image=imgtk)
#
#     # Tiếp tục cập nhật khung hình
#     camera_label.after(10, update_frame)
#
#
# # Tạo cửa sổ chính
# root = tk.Tk()
# root.title("Giao diện đăng nhập")
# root.geometry("800x600")
#
# # Frame chào mừng
# welcome_frame = tk.Frame(root)
# welcome_frame.pack(pady=20)
#
# welcome_label = tk.Label(welcome_frame, text="Chào mừng", font=("Arial", 24))
# welcome_label.pack()
#
# welcome_button = tk.Button(welcome_frame, text="Nhấn để tiếp tục", command=show_login_screen)
# welcome_button.pack(pady=10)
#
# # Frame đăng nhập
# login_frame = tk.Frame(root)
#
# label_user = tk.Label(login_frame, text="User:")
# label_user.grid(row=0, column=0, padx=5, pady=5)
# entry_user = tk.Entry(login_frame)
# entry_user.grid(row=0, column=1, padx=5, pady=5)
#
# label_password = tk.Label(login_frame, text="Password:")
# label_password.grid(row=1, column=0, padx=5, pady=5)
# entry_password = tk.Entry(login_frame, show="*")
# entry_password.grid(row=1, column=1, padx=5, pady=5)
#
# login_button = tk.Button(login_frame, text="Đăng nhập", command=login)
# login_button.grid(row=2, columnspan=2, pady=10)
#
# # Frame sau khi đăng nhập
# cap = cv2.VideoCapture(0)
# user_admin_frame = tk.Frame(root)
# user_button = tk.Button(user_admin_frame, text="User", command=show_user_frame)
#
# user_button.pack(side="left", padx=10)
#
# admin_button = tk.Button(user_admin_frame, text="Admin")
# admin_button.pack(side="right", padx=10)
#
# # Frame User để hiển thị camera
# user_frame = tk.Frame(root)
# camera_label = tk.Label(user_frame)
# camera_label.pack()
#
# label_user = tk.Label(login_frame, text="User:")
# label_user.grid(row=0, column=0, padx=5, pady=5)
#
# admin_button = tk.Button(user_frame, text="Take Photo", command= capture_image)
# admin_button.pack(side="top", padx=10)
#
# root.mainloop()
#
#
# import tkinter as tk
# from tkinter import messagebox, filedialog
# import cv2
# from PIL import Image, ImageTk
# from src.detect_code.detect_qrcode import recognition_qrcode
#
# # Hàm để chuyển sang màn hình đăng nhập
# def show_login_screen():
#     welcome_frame.pack_forget()
#     login_frame.pack(pady=20)
#
# # Hàm xử lý khi nhấn nút đăng nhập
# def login():
#     username = entry_user.get()
#     password = entry_password.get()
#
#     # Kiểm tra tài khoản đúng (ở đây dùng giá trị giả định)
#     if username == "user" and password == "password":
#         login_frame.pack_forget()
#         user_admin_frame.pack(pady=20)
#     else:
#         messagebox.showerror("Lỗi", "Sai tài khoản hoặc mật khẩu")
#
# def show_user_frame():
#     user_admin_frame.pack_forget()
#     user_frame.pack()
#     update_frame()
#
# # Hàm chụp ảnh và xử lý QR code
# def capture_image():
#     ret, frame = cap.read()
#     if ret:
#         data = recognition_qrcode(frame)
#         result_label.config(text=f"QR Code Data: {data}")  # Hiển thị dữ liệu lên ô trắng
#     else:
#         result_label.config(text="Không thể nhận diện ảnh.")
#
# # Cập nhật khung hình video từ camera
# def update_frame():
#     ret, frame = cap.read()
#
#     if ret:
#         frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
#         img = Image.fromarray(frame_rgb)
#         imgtk = ImageTk.PhotoImage(image=img)
#         camera_label.imgtk = imgtk
#         camera_label.configure(image=imgtk)
#
#     camera_label.after(10, update_frame)
#
# # Tạo cửa sổ chính
# root = tk.Tk()
# root.title("Giao diện đăng nhập")
# root.geometry("800x600")
#
# # Frame chào mừng
# welcome_frame = tk.Frame(root)
# welcome_frame.pack(pady=20)
#
# welcome_label = tk.Label(welcome_frame, text="Chào mừng", font=("Arial", 24))
# welcome_label.pack()
#
# welcome_button = tk.Button(welcome_frame, text="Nhấn để tiếp tục", command=show_login_screen)
# welcome_button.pack(pady=10)
#
# # Frame đăng nhập
# login_frame = tk.Frame(root)
#
# label_user = tk.Label(login_frame, text="User:")
# label_user.grid(row=0, column=0, padx=5, pady=5)
# entry_user = tk.Entry(login_frame)
# entry_user.grid(row=0, column=1, padx=5, pady=5)
#
# label_password = tk.Label(login_frame, text="Password:")
# label_password.grid(row=1, column=0, padx=5, pady=5)
# entry_password = tk.Entry(login_frame, show="*")
# entry_password.grid(row=1, column=1, padx=5, pady=5)
#
# login_button = tk.Button(login_frame, text="Đăng nhập", command=login)
# login_button.grid(row=2, columnspan=2, pady=10)
#
# # Khởi động camera
# cap = cv2.VideoCapture(0)
#
# # Frame sau khi đăng nhập
# user_admin_frame = tk.Frame(root)
# user_button = tk.Button(user_admin_frame, text="User", command=show_user_frame)
# user_button.pack(side="left", padx=10)
#
# admin_button = tk.Button(user_admin_frame, text="Admin")
# admin_button.pack(side="right", padx=10)
#
# # Frame User để hiển thị camera
# user_frame = tk.Frame(root)
# camera_label = tk.Label(user_frame)
# camera_label.pack()
#
# # Nút chụp ảnh
# capture_button = tk.Button(user_frame, text="Take Photo", command=capture_image)
# capture_button.pack(side="top", padx=10)
#
# # Label để hiển thị thông tin QR Code
# result_label = tk.Label(user_frame, text="QR Code Data: ", bg="white", width=50, height=2)
# result_label.pack(pady=10)
#
# # Khởi động giao diện
# root.mainloop()
#
# # Giải phóng camera sau khi đóng chương trình
# cap.release()
# cv2.destroyAllWindows()

import tkinter as tk
from tkinter import messagebox
import cv2
from PIL import Image, ImageTk
from src.detect_code.detect_qrcode import recognition_qrcode

def show_login_screen():
    welcome_frame.pack_forget()
    login_frame.pack(pady=20)

def login():
    username = entry_user.get()
    password = entry_password.get()

    # Kiểm tra tài khoản đúng (ở đây dùng giá trị giả định)
    if username == "user" and password == "password":
        login_frame.pack_forget()
        user_admin_frame.pack(pady=20)
    else:
        messagebox.showerror("Lỗi", "Sai tài khoản hoặc mật khẩu")

def show_user_frame():
    user_admin_frame.pack_forget()
    user_frame.pack()
    update_frame()

def show_admin_mode_modify():
    admin_admin_frame.pack_forget()
    admin_frame.pack()


def capture_image():
    ret, frame = cap.read()
    if ret:
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        data = recognition_qrcode(frame_rgb)
        if data:
            result_label.config(text=f"QR Code Data: {data}")
        else:
            result_label.config(text="Không tìm thấy QR Code.")
    else:
        result_label.config(text="Không thể nhận diện ảnh.")

def update_frame():
    ret, frame = cap.read()

    if ret:
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        img = Image.fromarray(frame_rgb)
        imgtk = ImageTk.PhotoImage(image=img)
        camera_label.imgtk = imgtk
        camera_label.configure(image=imgtk)

    camera_label.after(10, update_frame)

# Tạo cửa sổ chính
root = tk.Tk()
root.title("Giao diện đăng nhập")
root.geometry("800x600")

# Frame chào mừng
welcome_frame = tk.Frame(root)
welcome_frame.pack(pady=20)

welcome_label = tk.Label(welcome_frame, text="Chào mừng", font=("Arial", 24))
welcome_label.pack()

welcome_button = tk.Button(welcome_frame, text="Nhấn để tiếp tục", command=show_login_screen)
welcome_button.pack(pady=10)

login_frame = tk.Frame(root)

label_user = tk.Label(login_frame, text="User:")
label_user.grid(row=0, column=0, padx=5, pady=5)
entry_user = tk.Entry(login_frame)
entry_user.grid(row=0, column=1, padx=5, pady=5)

label_password = tk.Label(login_frame, text="Password:")
label_password.grid(row=1, column=0, padx=5, pady=5)
entry_password = tk.Entry(login_frame, show="*")
entry_password.grid(row=1, column=1, padx=5, pady=5)

login_button = tk.Button(login_frame, text="Đăng nhập", command=login)
login_button.grid(row=2, columnspan=2, pady=10)

cap = cv2.VideoCapture(0)

user_admin_frame = tk.Frame(root)
user_button = tk.Button(user_admin_frame, text="User", command=show_user_frame)
user_button.pack(side="left", padx=10)

admin_admin_frame = tk.Frame(root)
admin_button = tk.Button(user_admin_frame, text="Admin")
admin_button.pack(side="right", padx=10)

user_frame = tk.Frame(root)
camera_label = tk.Label(user_frame)
camera_label.pack()

capture_button = tk.Button(user_frame, text="Take Photo", command=capture_image)
capture_button.pack(side="top", padx=10)

result_label = tk.Label(user_frame, text="QR Code Data: ", bg="white", width=50, height=2)
result_label.pack(pady=10)

admin_frame = tk.Frame(root)
admin_label = tk.Label(admin_frame)
admin_label.pack()

modify_button = tk.Button(admin_frame, text="Modify Data", command=show_admin_mode_modify())
modify_button.pack(side="top", padx=10)

user_mode_button = tk.Button(admin_frame, text="Modify Data", command=capture_image)
user_mode_button.pack(side="top", padx=10)

root.mainloop()

cap.release()
cv2.destroyAllWindows()
