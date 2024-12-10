# import cv2
# import numpy as np
#
# # image = cv2.imread("D:\projects\qr_barcode_xla\dataset\img_1.png")
# def detect_small_square(image):
#     gray = cv2.cvtColor(image,cv2.COLOR_BGRA2GRAY)
#     _,threshold = cv2.threshold(gray,100,255,cv2.THRESH_BINARY)
#     contours,_=cv2.findContours(threshold,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
#     qr_contours = []
#     num_contour = len(contours)
#
#     for contour in contours:
#         peri = cv2.arcLength(contour, True)
#         approx = cv2.approxPolyDP(contour, 0.02 * peri, True)
#         if len(approx) == 4:
#             area = cv2.contourArea(approx)
#             x, y, w, h = cv2.boundingRect(approx)
#             aspect_ratio = w / float(h)
#             if 0.9 <= aspect_ratio <= 1.1 and area > 100:  # Diện tích đủ lớn và tỉ lệ gần hình vuông
#                 qr_contours.append(approx)
#     square_contours = sorted(qr_contours,key=cv2.contourArea)
#     closet_pair = None
#     for i in range(len(square_contours)-1):
#         area1= cv2.contourArea(square_contours[i])
#         area2= cv2.contourArea(square_contours[i+1])
#         difference = abs(area1-area2)/min(area1,area2)
#         if difference <= 0.5:
#             closet_pair = (square_contours[i],square_contours[i+1])
#             break
#     return qr_contours,closet_pair
#
# # def detect_bbox(qr_contours):
# #     if
# # # Vẽ các contour tìm được
# # cv2.drawContours(image, qr_contours, -1, (0, 255, 0), 3)
# #
# # # Hiển thị kết quả
# # cv2.imshow("QR Code Corners", image)
# # cv2.waitKey(0)
# # cv2.destroyAllWindows()

import cv2
import numpy as np

image = cv2.imread('D:\projects\qr_barcode_xla\dataset\OIF.jpg')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
_, thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)

# Tìm các contours
contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Lọc các contour hình vuông
square_contours = []
for contour in contours:
    # Xấp xỉ contour
    peri = cv2.arcLength(contour, True)
    approx = cv2.approxPolyDP(contour, 0.02 * peri, True)

    # Kiểm tra nếu contour có 4 đỉnh (tứ giác)
    if len(approx) == 4:
        x, y, w, h = cv2.boundingRect(approx)

        # Kiểm tra nếu tỷ lệ width/height gần bằng 1 (tức là hình vuông)
        aspect_ratio = float(w) / h
        if 0.8 <= aspect_ratio <= 1.1:  # Tỷ lệ trong khoảng cho phép
            square_contours.append(contour)

square_contours = sorted(square_contours, key=cv2.contourArea)
closest_triple = None
min_difference = float('inf')
for i in range(len(square_contours) - 2):
    area1 = cv2.contourArea(square_contours[i])
    area2 = cv2.contourArea(square_contours[i + 1])
    area3 = cv2.contourArea(square_contours[i + 2])

    difference_percentage_1 = abs(area1 - area2) / min(area1, area2)
    difference_percentage_2 = abs(area2 - area3) / min(area2, area3)

    if difference_percentage_1 <= 1 and difference_percentage_2 <= 1:
        closest_triple = (square_contours[i], square_contours[i + 1], square_contours[i + 2])
        break
if closest_triple is not None:
    cv2.drawContours(image, [closest_triple[0]], -1, (0, 255, 0), 5)
    cv2.drawContours(image, [closest_triple[1]], -1, (255, 0, 0), 5)
    cv2.drawContours(image, [closest_triple[2]], -1, (0, 0, 255), 5)
    print("Đã tìm thấy 3 contour có diện tích gần bằng nhau.")
else:
    print("Không tìm thấy 3 contour có diện tích gần bằng nhau dưới 5%.")

# Hiển thị ảnh kết quả
cv2.imshow("Closest Square Contours", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
