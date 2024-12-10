# import cv2
# import numpy as np
#
# image = cv2.imread('D:\projects\qr_barcode_xla\dataset\wedding-qr-code-august-2023-517ac560ee9545cea6289e40ad835452.jpg')
# gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# _, thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
# cv2.imshow("hung", thresh)
# contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
#
# square_contours = []
# for contour in contours:
#     peri = cv2.arcLength(contour, True)
#     approx = cv2.approxPolyDP(contour, 0.02 * peri, True)
#
#     if len(approx) == 4:
#         x, y, w, h = cv2.boundingRect(approx)
#
#         aspect_ratio = float(w) / h
#         if 0.8 <= aspect_ratio <= 1.1:
#             square_contours.append(contour)
#
# square_contours = sorted(square_contours, key=cv2.contourArea)
# closest_triple = None
# min_difference = float('inf')
# for i in range(len(square_contours) - 2):
#     area1 = cv2.contourArea(square_contours[i])
#     area2 = cv2.contourArea(square_contours[i + 1])
#     area3 = cv2.contourArea(square_contours[i + 2])
#
#     difference_percentage_1 = abs(area1 - area2) / min(area1, area2)
#     difference_percentage_2 = abs(area2 - area3) / min(area2, area3)
#
#     if difference_percentage_1 <= 1 and difference_percentage_2 <= 1:
#         closest_triple = (square_contours[i], square_contours[i + 1], square_contours[i + 2])
#         break
# if closest_triple is not None:
#     cv2.drawContours(image, [closest_triple[0]], -1, (0, 255, 0), 5)
#     cv2.drawContours(image, [closest_triple[1]], -1, (255, 0, 0), 5)
#     cv2.drawContours(image, [closest_triple[2]], -1, (0, 0, 255), 5)
#     print("Đã tìm thấy 3 contour có diện tích gần bằng nhau.")
# else:
#     print("Không tìm thấy 3 contour có diện tích gần bằng nhau dưới 5%.")
#
# # Hiển thị ảnh kết quả
# cv2.imshow("Closest Square Contours", image)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# import cv2
# import numpy as np
# from matplotlib.pyplot import imshow
#
# # Đọc ảnh và xử lý Canny để tìm cạnh
# image = cv2.imread(r'D:\projects\qr_barcode_xla\dataset\WIN_20241114_09_03_31_Pro.jpg')
# gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# edges = cv2.Canny(gray, 50, 150)
# cv2.imshow("", edges)
#
# # Tìm contours
# contours, _ = cv2.findContours(edges, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
#
# squares = []
# for cnt in contours:
#     approx = cv2.approxPolyDP(cnt, 0.02 * cv2.arcLength(cnt, True), True)
#
#     if len(approx) == 4 and cv2.contourArea(cnt) > 1000:
#         squares.append(approx)
#
# def get_bounding_box(square):
#     x_coords = [point[0][0] for point in square]
#     y_coords = [point[0][1] for point in square]
#     x1, y1 = min(x_coords), min(y_coords)
#     x2, y2 = max(x_coords), max(y_coords)
#     return x1, y1, x2, y2
#
# def is_square1_cover_square2(squareA, squareB):
#     x1A, y1A, x2A, y2A = get_bounding_box(squareA)
#     x1B, y1B, x2B, y2B = get_bounding_box(squareB)
#
#     return x1A <= x1B <= x2A and y1A <= y1B <= y2A and x1A <= x2B <= x2A and y1A <= y2B <= y2A
#
#
# def distance(p1, p2):
#     return np.sqrt((p2[0] - p1[0]) ** 2 + (p2[1] - p1[1]) ** 2)
#
#
# def calculate_area(square):
#     p1, p2, p3, p4 = square
#     side_length = distance(p1[0], p2[0])
#     area = side_length ** 2
#     return area
#
# def is_area_10_percent_larger(areaA, areaB):
#     return 1.7*areaB >= areaA >= 1.1 * areaB
#
# count =0
# for i, squareA in enumerate(squares):
#     for j, squareB in enumerate(squares):
#         if i != j:
#             if is_square1_cover_square2(squareA, squareB):
#                 print(f"Hình vuông {j} nằm trong hình vuông {i}")
#                 if is_area_10_percent_larger(calculate_area(squareA), calculate_area(squareB)):
#                     squares.pop(squares.index(squareB))
#                     print(squares.index(squareB))
#
#
# for square in squares:
#     cv2.drawContours(image, [square], -1, (0, 255, 0), 3)
#
# # Hiển thị hình ảnh kết quả
# cv2.imshow('QR Code Corners', image)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# import cv2
# import numpy as np
#
# def distance(p1, p2):
#     return np.sqrt((p2[0] - p1[0]) ** 2 + (p2[1] - p1[1]) ** 2)
#
# def get_bounding_box(square):
#     x_coords = [point[0][0] for point in square]
#     y_coords = [point[0][1] for point in square]
#     x1, y1 = min(x_coords), min(y_coords)
#     x2, y2 = max(x_coords), max(y_coords)
#     return x1, y1, x2, y2
#
# def calculate_area(square):
#     p1, p2, p3, p4 = square
#     side_length = distance(p1[0], p2[0])
#     area = side_length ** 2
#     return area
#
# def is_square(approx):
#     if len(approx) == 4:
#         p1, p2, p3, p4 = approx
#         d1 = distance(p1[0], p2[0])
#         d2 = distance(p2[0], p3[0])
#         d3 = distance(p3[0], p4[0])
#         d4 = distance(p4[0], p1[0])
#         if abs(d1 - d2) < 50 and abs(d2 - d3) < 50 and abs(d3 - d4) < 50 and calculate_area(approx)> 50:
#             return True
#     return False
#
#
# #
# image = cv2.imread(r'D:\projects\qr_barcode_xla\dataset\img_1.png')
#
# gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# thresh = cv2.threshold(gray, 170, 255, cv2.THRESH_BINARY)[1]
# cv2.imshow("",thresh)
# edges = cv2.Canny(thresh, 50, 150)
# contours, _ = cv2.findContours(edges, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
# # cv2.imshow("",edges)
# squares = []
#
# for cnt in contours:
#     approx = cv2.approxPolyDP(cnt, 0.02 * cv2.arcLength(cnt, True), True)
#     if is_square(approx) and 50> cv2.contourArea(cnt) > 100:
#         squares.append(approx)
#
# for square in squares:
#     cv2.drawContours(image, [square], -1, (0, 255, 0), 3)
#
# # Hiển thị kết quả
# cv2.imshow('Detected Squares', image)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

import cv2
import numpy as np

# Đọc ảnh
image = cv2.imread(r'D:\projects\qr_barcode_xla\dataset\img_1.png')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

blurred = cv2.GaussianBlur(gray, (5, 5), 0)

edges = cv2.Canny(blurred, 50, 150)
cv2.imshow("",edges)
kernel = np.ones((5, 5), np.uint8)
dilated_edges = cv2.dilate(edges, kernel, iterations=1)

closed_edges = cv2.morphologyEx(dilated_edges, cv2.MORPH_CLOSE, kernel)

contours, _ = cv2.findContours(closed_edges, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

def distance(p1, p2):
    return np.sqrt((p2[0] - p1[0]) ** 2 + (p2[1] - p1[1]) ** 2)

# def get_bounding_box(square):
#     x_coords = [point[0][0] for point in square]
#     y_coords = [point[0][1] for point in square]
#     x1, y1 = min(x_coords), min(y_coords)
#     x2, y2 = max(x_coords), max(y_coords)
#     return x1, y1, x2, y2
# def calculate_area(square):
#     p1, p2, p3, p4 = square
#     side_length = distance(p1[0], p2[0])
#     area = side_length ** 2
#     return area
# def is_square(approx):
#     if len(approx) == 4:
#         p1, p2, p3, p4 = approx
#         d1 = distance(p1[0], p2[0])
#         d2 = distance(p2[0], p3[0])
#         d3 = distance(p3[0], p4[0])
#         d4 = distance(p4[0], p1[0])
#         if abs(d1 - d2) < 50 and abs(d2 - d3) < 50 and abs(d3 - d4) < 50 and calculate_area(approx)>50:
#             return True
#     return False

def calculate_area(square):
    p1, p2, p3, p4 = square
    side_length = distance(p1[0], p2[0])
    area = side_length ** 2
    return area
for contour in contours:
    epsilon = 0.02 * cv2.arcLength(contour, True)
    approx = cv2.approxPolyDP(contour, epsilon, True)

    if len(approx) == 4 and calculate_area(approx) >150:
        cv2.drawContours(image, [approx], -1, (0, 255, 0), 3)

# Hiển thị kết quả
cv2.imshow('Detected Squares', image)
cv2.waitKey(0)
cv2.destroyAllWindows()


