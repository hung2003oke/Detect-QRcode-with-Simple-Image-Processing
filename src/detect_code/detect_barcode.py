# import cv2
#
# # Đọc hình ảnh từ file
# image = cv2.imread(r'D:\projects\qr_barcode_xla\dataset\OIF.jpg')
#
# # Kiểm tra nếu hình ảnh đã được đọc thành công
# if image is None:
#     print("Không thể đọc được hình ảnh.")
# else:
#     # Khởi tạo đối tượng QRCodeDetector
#     qr_detector = cv2.QRCodeDetector()
#
#     # Phát hiện và giải mã mã QR
#     data, vertices, _ = qr_detector.detectAndDecode(image)
#
#     # Kiểm tra nếu mã QR được phát hiện
#     if data:
#         print("Nội dung mã QR:", data)
#
#         # Kiểm tra nếu tọa độ của các đỉnh tồn tại
#         if vertices is not None:
#             vertices = vertices.astype(int)  # Chuyển đổi tọa độ về dạng số nguyên
#
#             # Vẽ bounding box (hình chữ nhật) xung quanh mã QR
#             for i in range(len(vertices[0])):
#                 cv2.line(image, tuple(vertices[0][i]), tuple(vertices[0][(i + 1) % len(vertices[0])]), (0, 255, 0), 3)
#
#         # Hiển thị ảnh với mã QR được phát hiện và bounding box
#         cv2.imshow("QR Code Detected", image)
#
#     else:
#         print("Không phát hiện được mã QR.")
#
#     # Đợi người dùng nhấn phím bất kỳ để đóng cửa sổ
#     cv2.waitKey(0)
#     cv2.destroyAllWindows()

# import cv2
# import numpy as np
#
# # Đọc hình ảnh từ file
# image = cv2.imread(r'D:\projects\qr_barcode_xla\dataset\download.jpg')
#
# # Kiểm tra nếu hình ảnh đã được đọc thành công
# if image is None:
#     print("Không thể đọc được hình ảnh.")
# else:
#     # Chuyển đổi hình ảnh sang grayscale
#     gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
#     blurred_image = cv2.GaussianBlur(gray_image, (5, 5), 0)
#     edges = cv2.Canny(blurred_image, 50, 150)
#
#     # Tìm kiếm các contour trong ảnh cạnh
#     contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
#
#     # Duyệt qua các contour và vẽ bounding box hình vuông
#     for contour in contours:
#         # Xấp xỉ contour thành hình đa giác (polygon)
#         epsilon = 0.04 * cv2.arcLength(contour, True)
#         approx = cv2.approxPolyDP(contour, epsilon, True)
#
#         # Kiểm tra xem contour có 4 đỉnh và có thể là hình vuông không
#         if len(approx) == 4:
#             x, y, w, h = cv2.boundingRect(approx)
#
#             # Kiểm tra xem bounding box có gần như hình vuông không
#             aspect_ratio = float(w) / h
#             if 0.7 <= aspect_ratio <= 1.1:
#                 # Vẽ bounding box hình vuông trên ảnh gốc
#                 cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
#
#     # Hiển thị hình ảnh với bounding box hình vuông
#     cv2.imshow('Bounding Boxes', image)
#
#     # Lưu kết quả
#     cv2.imwrite('bounding_boxes.jpg', image)
#
#     # Đợi người dùng nhấn phím bất kỳ để đóng cửa sổ
#     cv2.waitKey(0)
#     cv2.destroyAllWindows()



# import cv2
#
# # Đọc hình ảnh từ file
# image = cv2.imread('D:\\projects\\qr_barcode_xla\\dataset\\wedding-qr-code-august-2023-517ac560ee9545cea6289e40ad835452.jpg', cv2.IMREAD_GRAYSCALE)
#
# # Kiểm tra nếu hình ảnh đã được đọc thành công
# if image is None:
#     print("Không thể đọc được hình ảnh.")
# else:
#     # Áp dụng thresholding
#     _, threshold_image = cv2.threshold(image, 120, 255, cv2.THRESH_BINARY)
#
#     # Áp dụng Gaussian Blur để giảm nhiễu
#     blurred_image = cv2.GaussianBlur(threshold_image, (5, 5), 0)
#
#     # Áp dụng thuật toán Canny để phát hiện các cạnh
#     edges = cv2.Canny(blurred_image, 50, 150)
#
#     # Tìm kiếm các contour trong ảnh cạnh
#     contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
#
#     # Duyệt qua các contour và vẽ bounding box hình vuông
#     for contour in contours:
#         # Xấp xỉ contour thành hình đa giác (polygon)
#         epsilon = 0.04 * cv2.arcLength(contour, True)
#         approx = cv2.approxPolyDP(contour, epsilon, True)
#
#         # Kiểm tra xem contour có 4 đỉnh và có thể là hình vuông không
#         if len(approx) == 4:
#             x, y, w, h = cv2.boundingRect(approx)
#
#             # Kiểm tra xem bounding box có gần như hình vuông không
#             aspect_ratio = float(w) / h
#             if 0.8 <= aspect_ratio <= 1.2:
#                 # Vẽ bounding box hình vuông trên ảnh gốc
#                 cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
#
#     # Hiển thị hình ảnh với bounding box hình vuông
#     cv2.imshow('Bounding Boxes', image)
#
#     # Lưu kết quả
#     cv2.imwrite('bounding_boxes.jpg', image)
#
#     # Đợi người dùng nhấn phím bất kỳ để đóng cửa sổ
#     cv2.waitKey(0)
#     cv2.destroyAllWindows()


#
# import cv2
# import numpy as np
#
# # Đọc hình ảnh từ file
# image = cv2.imread('D:\projects\qr_barcode_xla\dataset\wedding-qr-code-august-2023-517ac560ee9545cea6289e40ad835452.jpg')
#
# # Kiểm tra nếu hình ảnh đã được đọc thành công
# if image is None:
#     print("Không thể đọc được hình ảnh.")
# else:
#     # Chuyển đổi hình ảnh sang grayscale
#     gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
#
#     # Áp dụng Gaussian Blur để giảm nhiễu
#     blurred_image = cv2.GaussianBlur(gray_image, (5, 5), 0)
#
#     # Áp dụng thuật toán Canny để phát hiện các cạnh
#     edges = cv2.Canny(blurred_image, 100, 200)
#
#     # Tìm kiếm các contour trong ảnh cạnh
#     contours, _ = cv2.findContours(edges, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
#
#     # Lọc và vẽ các bounding box cho các vùng có mật độ cạnh cao
#     for contour in contours:
#         area = cv2.contourArea(contour)
#         if area > 2500:
#             x, y, w, h = cv2.boundingRect(contour)
#
#             # Vẽ bounding box trên ảnh gốc
#             cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
#
#     # Hiển thị hình ảnh với bounding box
#     cv2.imshow('Detected Regions', image)
#
#     # Lưu kết quả
#     cv2.imwrite('detected_qr_regions.jpg', image)
#     cv2.waitKey(0)
#     cv2.destroyAllWindows()

# import cv2
#
# img = cv2.imread('D:\projects\qr_barcode_xla\dataset\wedding-qr-code-august-2023-517ac560ee9545cea6289e40ad835452.jpg')
#
# decoder = cv2.QRCodeDetector()
# data, points, _ = decoder.detectAndDecode(img)
#
# if points is not None:
#     print('Decoded data: ' + data)
#
#     points = points[0]
#     for i in range(len(points)):
#         pt1 = [int(val) for val in points[i]]
#         pt2 = [int(val) for val in points[(i + 1) % 4]]
#         cv2.line(img, pt1, pt2, color=(255, 0, 0), thickness=3)
#
#     cv2.imshow('Detected QR code', img)
#     cv2.waitKey(0)
#     cv2.destroyAllWindows()

import cv2

camera_id = 0
delay = 1
window_name = 'OpenCV Barcode'

bd = cv2.barcode.BarcodeDetector()
cap = cv2.VideoCapture(camera_id)

while True:
    ret, frame = cap.read()

    if ret:
        ret_bc, decoded_info, points = bd.detectAndDecode(frame)
        if ret_bc:
            frame = cv2.polylines(frame, points.astype(int), True, (0, 255, 0), 3)
            for s, p in zip(decoded_info, points):
                if s:
                    print(s)
                    frame = cv2.putText(frame, s, p[1].astype(int),
                                        cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 2, cv2.LINE_AA)
        cv2.imshow(window_name, frame)

    if cv2.waitKey(delay) & 0xFF == ord('q'):
        break

cv2.destroyWindow(window_name)


