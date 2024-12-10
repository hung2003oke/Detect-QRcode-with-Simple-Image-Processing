# import cv2
# import numpy as np
# from tkinter import filedialog, Tk, Button, Label
# from tkinter import messagebox
# from PIL import Image, ImageTk
# import tkinter as tk
# from src.detect_code.detect_qrcode import recognition_qrcode
#
# class Ui_Client:
#     def __init__(self, parent_window):
#         self.root = tk.Toplevel(parent_window)  # Tạo cửa sổ Toplevel
#         self.root.geometry("600x800")
#         self.cap = cv2.VideoCapture(0)
#         self.camera_label = None
#         self.result_label = None
#         self.create_widgets_client()
#
#     def capture_image(self):
#         ret, frame = self.cap.read()
#         if ret:
#             frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
#             data = recognition_qrcode(frame_rgb)
#             if data:
#                 self.result_label.config(text=f"QR Code Data: {data}")
#             else:
#                 self.result_label.config(text="Không tìm thấy QR Code.")
#         else:
#             self.result_label.config(text="Không thể nhận diện ảnh.")
#
#     def update_frame(self):
#         ret, frame = self.cap.read()
#         if ret:
#             frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
#             img = Image.fromarray(frame_rgb)
#             imgtk = ImageTk.PhotoImage(image=img)
#             self.camera_label.imgtk = imgtk  # Sử dụng self để tham chiếu đến label
#             self.camera_label.configure(image=imgtk)
#
#         self.camera_label.after(10, self.update_frame)  # Cập nhật frame sau 10ms
#
#     def create_widgets_client(self):
#         user_frame = tk.Frame(self.root)
#         user_frame.pack()
#
#         # Camera Label để hiển thị hình ảnh từ camera
#         self.camera_label = tk.Label(user_frame)
#         self.camera_label.pack()
#
#         # Nút chụp ảnh
#         capture_button = tk.Button(user_frame, text="Take Photo", command=self.capture_image)
#         capture_button.pack(side="top", padx=10)
#
#         # Nhãn hiển thị kết quả QR Code
#         self.result_label = tk.Label(user_frame, text="QR Code Data: ", bg="white", width=50, height=2)
#         self.result_label.pack(pady=10)
#
#         self.update_frame()  # Bắt đầu cập nhật camera
# import cv2
# import cv2
# import numpy as np
# from tkinter import filedialog, Button, Label, messagebox
# from PIL import Image, ImageTk
# import tkinter as tk
# from src.QRCodeDetector.main import QRCodeProcessor
#
# class Ui_Client:
#     def __init__(self, parent_frame):
#         self.parent_frame = parent_frame  # Sử dụng Frame cha được truyền vào
#         self.cap = cv2.VideoCapture(0)
#         self.camera_label = None
#         self.result_label = None
#         self.create_widgets_client()
#
#     def capture_image(self):
#         ret, frame = self.cap.read()
#         if ret:
#             frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
#             bbox,data = QRCodeProcessor().process_frame(frame)
#             if data:
#                 self.result_label.config(text=f"QR Code Data: {data}")
#             else:
#                 self.result_label.config(text="Không tìm thấy QR Code.")
#         else:
#             self.result_label.config(text="Không thể nhận diện ảnh.")
#
#     def update_frame(self):
#         ret, frame = self.cap.read()
#         if ret:
#             frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
#             img = Image.fromarray(frame_rgb)
#             imgtk = ImageTk.PhotoImage(image=img)
#             self.camera_label.imgtk = imgtk  # Sử dụng self để giữ tham chiếu đến ảnh
#             self.camera_label.configure(image=imgtk)
#
#         self.camera_label.after(1, self.update_frame)  # Cập nhật frame sau 10ms
#
#     def create_widgets_client(self):
#         # Tạo các thành phần trong Frame cha
#         user_frame = tk.Frame(self.parent_frame)
#         user_frame.pack()
#
#         # Camera Label để hiển thị hình ảnh từ camera
#         self.camera_label = tk.Label(user_frame)
#         self.camera_label.pack()
#
#         # Nút chụp ảnh
#         capture_button = tk.Button(user_frame, text="Take Photo", command=self.capture_image)
#         capture_button.pack(side="top", padx=10)
#
#         # Nhãn hiển thị kết quả QR Code
#         self.result_label = tk.Label(user_frame, text="QR Code Data: ", bg="white", width=50, height=2)
#         self.result_label.pack(pady=10)
#
#         self.update_frame()
# import sqlite3
#
# import cv2
# import numpy as np
# from tkinter import Button, Label
# from PIL import Image, ImageTk
# import tkinter as tk
# from src.QRCodeDetector.main import QRCodeProcessor
# from src.QRCodeDetector.compare_qrcontents_vs_database import compare_result
#
# class Ui_Client:
#     def __init__(self, parent_frame):
#         self.parent_frame = parent_frame
#         self.cap = cv2.VideoCapture(0)
#         self.camera_label = None
#         self.result_label = None
#         self.create_widgets_client()
#         self.update_job = None
#         self.compare_result = None
#
#     def capture_image(self):
#         ret, frame = self.cap.read()
#         if ret:
#             processor = QRCodeProcessor()
#             _, qr_contents = processor.process_frame(frame)
#
#             if qr_contents:
#                 self.result_label.config(text=f"QR Code Data: {qr_contents}")
#             else:
#                 self.result_label.config(text="Không tìm thấy QR Code.")
#         else:
#             self.result_label.config(text="Không thể nhận diện ảnh.")
#
#     # def update_frame(self):
#     #     ret, frame = self.cap.read()
#     #     if ret:
#     #         processor = QRCodeProcessor()
#     #         processed_frame, qr_contents = processor.process_frame(frame)
#     #
#     #         img = Image.fromarray(processed_frame)
#     #         imgtk = ImageTk.PhotoImage(image=img)
#     #         self.camera_label.imgtk = imgtk
#     #         self.camera_label.configure(image=imgtk)
#     #
#     #         if qr_contents:
#     #             self.result_label.config(text=f"QR Code Data: {qr_contents}")
#     #         else:
#     #             self.result_label.config(text="Không tìm thấy QR Code.")
#     #
#     #     self.camera_label.after(1, self.update_frame)
#
#     def update_frame(self):
#         ret, frame = self.cap.read()
#         if ret:
#             # Khởi tạo QRCodeProcessor và xử lý frame
#             processor = QRCodeProcessor()
#             _, qr_contents = processor.process_frame(frame)
#
#             # Dùng ảnh RGB gốc để vẽ bounding boxes
#             bbox_img = frame.copy()  # Sao chép khung hình RGB gốc để vẽ
#
#             # Lấy bounding boxes từ processor (từ hàm `process_image` trong QRCodeProcessor)
#             bboxes, _, _ = processor.process_image(cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY))
#
#             # Vẽ bounding boxes lên ảnh RGB
#             if bboxes:
#                 for bbox in bboxes:
#                     cv2.polylines(bbox_img, [bbox.astype(np.int32)], True, (0, 255, 0), 2)
#
#             # Chuyển đổi ảnh đã vẽ sang định dạng mà Tkinter hiểu
#             img = Image.fromarray(cv2.cvtColor(bbox_img, cv2.COLOR_BGR2RGB))
#             imgtk = ImageTk.PhotoImage(image=img)
#
#             # Hiển thị ảnh trong giao diện
#             self.camera_label.imgtk = imgtk
#             self.camera_label.configure(image=imgtk)
#
#             # Hiển thị kết quả QR Code
#             if qr_contents:
#                 self.result_label.config(text=f"QR Code Data: {qr_contents}")
#                 conn = sqlite3.connect(r'D:\projects\qr_barcode_xla\src\guide\admin\database_qrcode.db')
#                 try:
#                     conn = sqlite3.connect(r'D:\projects\qr_barcode_xla\src\guide\admin\database_qrcode.db')
#                     if compare_result(conn, qr_contents):
#                         self.compare_result.config(text="QR đã tồn tại trong database")
#                     else:
#                         self.compare_result.config(text="QR chưa tồn tại trong database")
#                 except Exception as e:
#                     self.result_label.config(text=f"Lỗi: {e}")
#                 finally:
#                     conn.close()
#             else:
#                 self.result_label.config(text="Không tìm thấy QR Code.")
#
#
#         # Cập nhật frame liên tục
#         self.camera_label.after(10, self.update_frame)
#
#     def create_widgets_client(self):
#         user_frame = tk.Frame(self.parent_frame)
#         user_frame.pack()
#
#         self.camera_label = tk.Label(user_frame)
#         self.camera_label.pack()
#
#         capture_button = tk.Button(user_frame, text="Take Photo", command=self.capture_image)
#         capture_button.pack(side="top", padx=10)
#
#         self.result_label = tk.Label(user_frame, text="QR Code Data: ", bg="white", width=50, height=2)
#         self.result_label.pack(pady=10)
#
#         self.compare_result = tk.Label(user_frame, text= "Result of compare: ", bg="white", width=50, height=2)
#         self.compare_result.pack(pady=10)
#
#
#
#         self.update_frame()
#
#     def stop_camera(self):
#         """Dừng camera và hủy cập nhật frame."""
#         if self.update_job:
#             self.camera_label.after_cancel(self.update_job)  # Hủy job after
#             self.update_job = None
#
#         if self.cap.isOpened():
#             self.cap.release()

import sqlite3
import cv2
import numpy as np
import ast
# from tkinter import Button, Label
from PIL import Image, ImageTk
import tkinter as tk
from src.QRCodeDetector.main import QRCodeProcessor
from src.QRCodeDetector.compare_qrcontents_vs_database import compare_result
# from src.QRCodeDetector.remove_duplicate_qrcode import remove_duplicate_qrcode_smallest
from src.QRCodeDetector.remove_duplicate_qrcode import remove_duplicate_qrcode_smallest_simple_v2


class Ui_Client:
    def __init__(self, parent_frame):
        self.parent_frame = parent_frame
        self.cap = cv2.VideoCapture(0)
        self.camera_label = None
        self.result_label = None
        self.compare_result = None
        self.create_widgets_client()
        self.update_job = None

    def capture_image(self):
        ret, frame = self.cap.read()
        if ret:
            processor = QRCodeProcessor()
            _, qr_contents = processor.process_frame(frame)

            if qr_contents:
                self.result_label.config(text=f"QR Code Data: {qr_contents}")
            else:
                self.result_label.config(text="Không tìm thấy QR Code.")
        else:
            self.result_label.config(text="Không thể nhận diện ảnh.")

    # def update_frame(self):
    #     ret, frame = self.cap.read()
    #     if ret:
    #         # Khởi tạo QRCodeProcessor và xử lý frame
    #         processor = QRCodeProcessor()
    #         _, qr_contents = processor.process_frame(frame)
    #
    #         # Dùng ảnh RGB gốc để vẽ bounding boxes
    #         bbox_img = frame.copy()  # Sao chép khung hình RGB gốc để vẽ
    #
    #         # Lấy bounding boxes từ processor (từ hàm `process_image` trong QRCodeProcessor)
    #         bboxes, _, _ = processor.process_image(cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY))
    #
    #         bboxes,qr_contents = remove_duplicate_qrcode_smallest(bboxes,qr_contents,0.1)
    #
    #
    #         # Vẽ bounding boxes lên ảnh RGB
    #         if bboxes:
    #             for bbox in bboxes:
    #                 cv2.polylines(bbox_img, [bbox.astype(np.int32)], True, (0, 255, 0), 2)
    #
    #         # Chuyển đổi ảnh đã vẽ sang định dạng mà Tkinter hiểu
    #         img = Image.fromarray(cv2.cvtColor(bbox_img, cv2.COLOR_BGR2RGB))
    #         imgtk = ImageTk.PhotoImage(image=img)
    #
    #         # Hiển thị ảnh trong giao diện
    #         self.camera_label.imgtk = imgtk
    #         self.camera_label.configure(image=imgtk)
    #
    #         # Hiển thị kết quả QR Code
    #         if qr_contents:
    #             self.result_label.config(text=f"QR Code Data: {qr_contents}")
    #             try:
    #
    #                 conn = sqlite3.connect(r'D:\projects\qr_barcode_xla\src\guide\admin\database_qrcode.db')
    #                 if compare_result(conn, qr_contents):
    #                     if self.compare_result:
    #                         self.compare_result.config(text="QR đã tồn tại trong database")
    #                 else:
    #                     if self.compare_result:
    #                         self.compare_result.config(text="QR chưa tồn tại trong database")
    #
    #             except Exception as e:
    #                 self.result_label.config(text=f"Lỗi: {e}")
    #             finally:
    #                 conn.close()
    #         else:
    #             self.result_label.config(text="Không tìm thấy QR Code.")
    #
    #     # Cập nhật frame liên tục
    #     self.camera_label.after(1, self.update_frame)

    def convert_bboxes_to_xywh(self, bboxes):
        """
        Chuyển đổi danh sách các bounding boxes từ định dạng bốn điểm (polygon)
        sang định dạng (x, y, w, h).
        """
        converted_bboxes = []
        for bbox in bboxes:
            # Chuyển mảng NumPy thành bounding box dạng (x, y, w, h)
            if isinstance(bbox, np.ndarray) and bbox.shape == (4, 2):
                x_min = int(np.min(bbox[:, 0]))
                y_min = int(np.min(bbox[:, 1]))
                x_max = int(np.max(bbox[:, 0]))
                y_max = int(np.max(bbox[:, 1]))
                converted_bboxes.append((x_min, y_min, x_max - x_min, y_max - y_min))
            else:
                print(f"Bỏ qua bbox không hợp lệ: {bbox}")
        return converted_bboxes

    # def update_frame(self):
    #     ret, frame = self.cap.read()
    #     if ret:
    #         processor = QRCodeProcessor()
    #         bboxes, _, qr_contents = processor.process_image(
    #             cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY))
    #
    #         if bboxes is None:
    #             self.result_label.config(text="Không tìm thấy QR Code.")
    #             self.camera_label.after(1, self.update_frame)
    #             return
    #
    #         bboxes = self.convert_bboxes_to_xywh(bboxes)
    #         if not bboxes or not qr_contents:
    #             self.result_label.config(text="Không tìm thấy QR Code.")
    #             self.camera_label.after(1, self.update_frame)
    #             return
    #
    #         # Gọi hàm loại bỏ QR Code trùng lặp
    #
    #         # Dùng ảnh RGB gốc để vẽ bounding boxes
    #         bbox_img = frame.copy()  # Sao chép khung hình RGB gốc để vẽ
    #         # bboxes, qr_contents = remove_duplicate_qrcode_smallest(bboxes, qr_contents, 0.1)
    #         bboxes, qr_contents = remove_duplicate_qrcode_smallest_simple_v2(bboxes, qr_contents)
    #
    #         # # Vẽ bounding boxes lên ảnh RGB
    #         if bboxes:
    #             for bbox in bboxes:
    #                 x, y, w, h = bbox
    #                 cv2.rectangle(bbox_img, (x, y), (x + w, y + h), (0, 255, 0), 2)
    #
    #         # Hiển thị nội dung không trùng lặp
    #         # if qr_contents:
    #         #     self.result_label.config(text=f"QR Code Data: {', '.join(qr_contents)}")
    #
    #         # Chuyển đổi ảnh đã vẽ sang định dạng mà Tkinter hiểu
    #         img = Image.fromarray(cv2.cvtColor(bbox_img, cv2.COLOR_BGR2RGB))
    #         imgtk = ImageTk.PhotoImage(image=img)
    #
    #         # Hiển thị ảnh trong giao diện
    #         self.camera_label.imgtk = imgtk
    #         self.camera_label.configure(image=imgtk)
    #         if qr_contents:
    #             if not isinstance(qr_contents, str):
    #                 qr_contents = str(qr_contents)
    #
    #             qr_contents = qr_contents.strip()
    #             print(f"QR Content after cleaning: {qr_contents}")
    #             print(type(qr_contents))
    #             qr_contents = ast.literal_eval(qr_contents)
    #
    #             self.result_label.config(text=f"QR Content after cleaning: {qr_contents}")
    #             conn = sqlite3.connect(r'D:\projects\qr_barcode_xla\src\guide\admin\database_qrcode.db')
    #             try:
    #                 result = compare_result(conn, qr_contents)
    #                 conn.close()
    #                 print(result)
    #                 true_keys = [key for key, value in result.items() if value]
    #                 print(true_keys)
    #                 if true_keys:
    #                     self.compare_result.config(text=f"QR tồn tại: {', '.join(true_keys)}")
    #                 else:
    #                     self.compare_result.config(text="QR chưa tồn tại trong database")
    #             except sqlite3.Error as e:
    #                 self.compare_result.config(text=f"Lỗi truy vấn database: {e}")
    #         else:
    #             self.result_label.config(text="Không thể tìm thấy QR Code.")
    #             self.compare_result.config(text="QR chưa tồn tại trong database")
    #     else:
    #         self.result_label.config(text="Không thể nhận diện ảnh.")
    #
    #     self.camera_label.after(1, self.update_frame)

    def update_frame(self):
        ret, frame = self.cap.read()
        if ret:
            processor = QRCodeProcessor()
            bboxes, _, qr_contents = processor.process_image(
                cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY))

            # Chuyển đổi bounding box nếu tồn tại
            bboxes = self.convert_bboxes_to_xywh(bboxes) if bboxes else []

            # Nếu không tìm thấy QR Code, hiển thị khung hình gốc
            if not bboxes or not qr_contents:
                self.result_label.config(text="Không tìm thấy QR Code.")
                qr_contents = None  # Đảm bảo không xử lý dữ liệu QR nữa

            else:
                # Xử lý khi có QR Code: loại bỏ trùng lặp
                bboxes, qr_contents = remove_duplicate_qrcode_smallest_simple_v2(bboxes, qr_contents)

                # Vẽ bounding boxes lên khung hình
                for bbox in bboxes:
                    x, y, w, h = bbox
                    cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
            if qr_contents:
                if not isinstance(qr_contents, str):
                    qr_contents = str(qr_contents)

                qr_contents = qr_contents.strip()
                print(f"QR Content after cleaning: {qr_contents}")
                print(type(qr_contents))
                qr_contents = ast.literal_eval(qr_contents)

                self.result_label.config(text=f"QR Content after cleaning: {qr_contents}")
                conn = sqlite3.connect(r'D:\projects\qr_barcode_xla\src\guide\admin\database_qrcode.db')
                try:
                    result = compare_result(conn, qr_contents)
                    conn.close()
                    print(result)
                    true_keys = [key for key, value in result.items() if value]
                    print(true_keys)
                    if true_keys:
                        self.compare_result.config(text=f"QR tồn tại: {', '.join(true_keys)}")
                    else:
                        self.compare_result.config(text="QR chưa tồn tại trong database")
                except sqlite3.Error as e:
                    self.compare_result.config(text=f"Lỗi truy vấn database: {e}")
            else:
                self.result_label.config(text="Không thể tìm thấy QR Code.")
                self.compare_result.config(text="QR chưa tồn tại trong database")
            img = Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
            imgtk = ImageTk.PhotoImage(image=img)

            # Hiển thị hình ảnh trong `camera_label`
            self.camera_label.imgtk = imgtk
            self.camera_label.configure(image=imgtk)
        else:
            self.result_label.config(text="Không thể nhận diện ảnh.")

        self.camera_label.after(1, self.update_frame)

    def create_widgets_client(self):
        user_frame = tk.Frame(self.parent_frame)
        user_frame.pack()

        self.camera_label = tk.Label(user_frame)
        self.camera_label.pack()

        capture_button = tk.Button(user_frame, text="Take Photo", command=self.capture_image)
        capture_button.pack(side="top", padx=10)

        self.result_label = tk.Label(user_frame, text="QR Code Data: ", bg="white", width=50, height=2)
        self.result_label.pack(pady=10)

        self.compare_result = tk.Label(user_frame, text="Result of compare: ", bg="white", width=50, height=2)
        self.compare_result.pack(pady=10)

        self.update_frame()

    def stop_camera(self):
        """Dừng camera và hủy cập nhật frame."""
        if self.update_job:
            self.camera_label.after_cancel(self.update_job)
            self.update_job = None

        if self.cap.isOpened():
            self.cap.release()
