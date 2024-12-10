# import cv2
#
#
# def recognition_qrcode(image):
#     decoder = cv2.QRCodeDetector()
#     data, points, _ = decoder.detectAndDecode(image)
#
#     if points is not None:
#         print('Decoded data: ' + data)
#
#         points = points[0]
#         for i in range(len(points)):
#             pt1 = [int(val) for val in points[i]]
#             pt2 = [int(val) for val in points[(i + 1) % 4]]
#             cv2.line(image, pt1, pt2, color=(255, 0, 0), thickness=3)
#
#         cv2.imshow('Detected QR code', image)
#         cv2.waitKey(0)
#         cv2.destroyAllWindows()
#
#     return data
#
# image_path =r"D:\projects\qr_barcode_xla\dataset\WIN_20241114_09_03_31_Pro.jpg"
# image= cv2.imread(image_path)
#
# recognition_qrcode(image)

"""
Write by Phạm Nguyên Hưng
Thuật toán chính cho bài toán detect QrCode
"""
import cv2
import numpy as np


def distance(p1, p2):
    return np.sqrt((p2[0] - p1[0]) ** 2 + (p2[1] - p1[1]) ** 2)

def calculate_area(square):
    p1, p2, p3, p4 = square
    side_length = distance(p1[0], p2[0])
    area = side_length ** 2
    return area

def is_square(approx):
    if len(approx) == 4:
        p1, p2, p3, p4 = approx
        d1 = distance(p1[0], p2[0])
        d2 = distance(p2[0], p3[0])
        d3 = distance(p3[0], p4[0])
        d4 = distance(p4[0], p1[0])
        if abs(d1 - d2) < 10 and abs(d2 - d3) < 10 and abs(d3 - d4) < 10 and calculate_area(approx)>50:
            return True
    return False

def calculate_angle(vectorA, vectorB):
    dot_product = np.dot(vectorA, vectorB)
    magnitude_A = np.linalg.norm(vectorA)
    magnitude_B = np.linalg.norm(vectorB)
    cos_theta = dot_product / (magnitude_A * magnitude_B)

    cos_theta = np.clip(cos_theta, -1.0, 1.0)
    # Tính góc
    angle_rad = np.arccos(cos_theta)

    # Chuyển đổi góc từ radian sang độ (degrees)
    angle_deg = np.degrees(angle_rad)

    return angle_deg

def is_perpendicular(p1, p2, p3, p4):
    # Lấy tọa độ (x, y) từ các điểm
    vector_AB = np.array([p2[0][0] - p1[0][0], p2[0][1] - p1[0][1]])  # Vector từ A đến B
    vector_BC = np.array([p3[0][0] - p2[0][0], p3[0][1] - p2[0][1]])  # Vector từ B đến C
    vector_CD = np.array([p4[0][0] - p3[0][0], p4[0][1] - p3[0][1]])  # Vector từ C đến D
    vector_DA = np.array([p1[0][0] - p4[0][0], p1[0][1] - p4[0][1]])  # Vector từ D đến A

    # Tính góc giữa các vector
    angle_ABC = calculate_angle(vector_AB, vector_BC)
    angle_BCD = calculate_angle(vector_BC, vector_CD)
    angle_CDA = calculate_angle(vector_CD, vector_DA)
    angle_DAB = calculate_angle(vector_DA, vector_AB)

    return angle_ABC, angle_BCD, angle_CDA, angle_DAB


def count_children(hierarchy, parent, inner=False):
    if parent == -1:
        return 0
    elif not inner:
        return count_children(hierarchy, hierarchy[parent][2], True)
    return 1 + count_children(hierarchy, hierarchy[parent][0], True) + count_children(hierarchy, hierarchy[parent][2], True)


def has_square_parent(hierarchy, squares, parent):
    if hierarchy[parent][3] == -1:
        return False
    if hierarchy[parent][3] in squares:
        return True
    return has_square_parent(hierarchy, squares, hierarchy[parent][3])


def get_center(c):
    """

    :param c:
    :return: center của đối tượng ( ở đây là
    """
    m = cv2.moments(c)
    return [int(m["m10"] / m["m00"]), int(m["m01"] / m["m00"])]

def find_fourth_center(centers):
    A, B, C = centers
    D = (A[0] + C[0] - B[0], A[1] + C[1] - B[1])
    return D

def non_max_suppression(squares, overlap_thresh=0.3):
    boxes = []
    for square in squares:
        x, y, w, h = cv2.boundingRect(square)
        boxes.append((x, y, w, h))

    # Sắp xếp các ô vuông theo diện tích giảm dần
    boxes = sorted(boxes, key=lambda b: b[2] * b[3], reverse=True)
    filtered_boxes = []

    while boxes:
        # Chọn ô vuông lớn nhất còn lại
        largest = boxes.pop(0)
        filtered_boxes.append(largest)

        # Loại bỏ các ô vuông có độ trùng lặp lớn hơn ngưỡng
        boxes = [
            box for box in boxes
            if compute_iou(largest, box) < overlap_thresh
        ]

    return filtered_boxes



def crop_and_rotate_corner():
    pass

def compute_iou(box1, box2):
    # Tính toán Intersection over Union (IoU) của hai bounding box
    x1, y1, w1, h1 = box1
    x2, y2, w2, h2 = box2

    xi1 = max(x1, x2)
    yi1 = max(y1, y2)
    xi2 = min(x1 + w1, x2 + w2)
    yi2 = min(y1 + h1, y2 + h2)

    inter_area = max(0, xi2 - xi1) * max(0, yi2 - yi1)
    box1_area = w1 * h1
    box2_area = w2 * h2
    union_area = box1_area + box2_area - inter_area

    return inter_area / union_area

def filter_inner_squares(squares, area_thresh=0.5):
    # Tạo danh sách các bounding box và diện tích tương ứng cho mỗi ô vuông
    boxes = []
    for square in squares:
        x, y, w, h = cv2.boundingRect(square)
        area = w * h
        boxes.append((x, y, w, h, area, square))  # Thêm ô vuông ban đầu vào để tiện dùng sau này

    # Sắp xếp các ô vuông theo diện tích giảm dần
    boxes = sorted(boxes, key=lambda b: b[4], reverse=True)
    filtered_boxes = []

    for i in range(len(boxes)):
        keep = True
        x1, y1, w1, h1, area1, square1 = boxes[i]

        # Kiểm tra các ô vuông nhỏ hơn nằm bên trong ô vuông lớn hơn
        for j in range(i + 1, len(boxes)):
            x2, y2, w2, h2, area2, square2 = boxes[j]

            # Kiểm tra bao chứa
            if (x1 <= x2 <= x1 + w1 and y1 <= y2 <= y1 + h1 and
                    x1 <= x2 + w2 <= x1 + w1 and y1 <= y2 + h2 <= y1 + h1):
                # Nếu diện tích ô lớn hơn ô bên trong 50%
                if area1 > area2 * (1 + area_thresh):
                    keep = False  # Đánh dấu để loại ô vuông nhỏ hơn

        if keep:
            filtered_boxes.append(square1)

    return filtered_boxes
# def filter_inner_squares(squares, threshold=0.3):
#     """
#     Loại bỏ các hình vuông nằm bên trong một hình vuông khác dựa trên tỷ lệ chồng lấn.
#     :param squares: Danh sách các hình vuông (x, y, w, h).
#     :param threshold: Ngưỡng diện tích (0.3 là 30%).
#     :return: Danh sách các hình vuông không bị lồng.
#     """
#     filtered_squares = []
#     for i, square1 in enumerate(squares):
#         x1, y1, w1, h1 = square1
#         area1 = w1 * h1
#         keep = True
#         for j, square2 in enumerate(squares):
#             if i == j:
#                 continue
#             x2, y2, w2, h2 = square2
#             area2 = w2 * h2
#             # Kiểm tra nếu square1 nằm trong square2
#             if (
#                 x1 >= x2
#                 and y1 >= y2
#                 and x1 + w1 <= x2 + w2
#                 and y1 + h1 <= y2 + h2
#                 and (area1 / area2) < threshold
#             ):
#                 keep = False
#                 break
#         if keep:
#             filtered_squares.append(square1)
#     return filtered_squares


def classify_corners(centers):
    """
    Phân loại các trung tâm của hình vuông thành các góc: trên-trái, trên-phải, dưới-trái
    :param centers: danh sách các trung tâm (x, y)
    :return: dict với các góc {"top-left": (x, y), "top-right": (x, y), "bottom-left": (x, y)}
    """
    # Sắp xếp các trung tâm theo trục y trước, rồi theo trục x
    sorted_centers_y = sorted(centers, key=lambda c: (c[1], c[0]))  # Sắp xếp theo y, sau đó theo x
    sorted_centers_x = sorted(centers, key=lambda c: (c[0], c[1]))  # Sắp xếp theo x, sau đó theo y
    # top-right là điểm có x lớn nhất
    top_right = max(sorted_centers_x, key=lambda c: c[0])
    # bottom-left là điểm có y lớn nhất
    bottom_left = max(sorted_centers_y, key=lambda c: c[1])
    # top-right là điểm còn lại
    top_left = [c for c in centers if c != top_right and c != bottom_left][0]

    return {"top-left": top_left, "top-right": top_right, "bottom-left": bottom_left}

# def calculate_missing_corner(corners):
#     """
#     Tính toán tọa độ góc thứ 4 dựa trên các góc đã biết
#     :param corners: dict chứa 3 góc
#     :return: tọa độ của góc thứ 4 (x, y)
#     """
#     top_left = corners["top-left"]
#     top_right = corners["top-right"]
#     bottom_left = corners["bottom-left"]
#     # Dự đoán góc dưới-phải bằng cách đối xứng
#     bottom_right = (top_right[0] + bottom_left[0] - top_left[0],
#                     top_right[1] + bottom_left[1] - top_left[1])
#     return bottom_right
#
# def find_4th_corner(target_center):
#     """
#     Tính toán hình vuông mới từ trung tâm mục tiêu bằng cách dịch chuyển các góc.
#     :param target_center: dictionary chứa các tọa độ của góc top-left và bottom-right
#     :return: danh sách các điểm của hình vuông mới
#     """
#     # Lấy các tọa độ của góc top-left và bottom-right
#     top_left_x = classify_corners(target_center)["top-left"][0]
#     top_left_y = classify_corners(target_center)["top-left"][1]
#     bottom_right_x = calculate_missing_corner(target_center)[0]
#     bottom_right_y = calculate_missing_corner(target_center)[1]
#
#     # Tính toán tỷ lệ x và y (sự chênh lệch giữa các góc)
#     x_ratio = int(bottom_right_x - top_left_x)
#     y_ratio = int(bottom_right_y - top_left_y)
#
#     # Tạo ra các điểm của hình vuông mới (di chuyển theo tỷ lệ)
#     square = [
#         [top_left_x + x_ratio, top_left_y + y_ratio],  # Điểm 1
#         [top_left_x + x_ratio, top_left_y],  # Điểm 2
#         [bottom_right_x + x_ratio, bottom_right_y],  # Điểm 3
#         [bottom_right_x + x_ratio, top_left_y + y_ratio],  # Điểm 4
#     ]
#
#     return square


# image = cv2.imread(r'D:\projects\qr_barcode_xla\dataset\img_5.png')
# gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# # blur = cv2.GaussianBlur(gray, (5, 5), 0)
# ret3, th = cv2.threshold(gray, 50, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)
# edges = cv2.Canny(th, 50, 150)
# # kernel = np.ones((5, 5), np.uint8)
# # dilated_edges = cv2.dilate(edges, kernel, iterations=1)
# # closed_edges = cv2.morphologyEx(dilated_edges, cv2.MORPH_CLOSE, kernel)
# contours, _ = cv2.findContours(edges, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
#
# squares = []
#
# for cnt in contours:
#     approx = cv2.approxPolyDP(cnt, 0.02 * cv2.arcLength(cnt, True), True)
#     if len(approx) == 4:
#         p1, p2, p3, p4 = approx
#         angles = is_perpendicular(p1, p2, p3, p4)
#         (x, y, w, h) = cv2.boundingRect(approx)
#         aspect_ratio = w / float(h)
#
#         # Kiểm tra điều kiện hình vuông
#         if 0.8 <= aspect_ratio <= 1.2 and is_square(approx) and all(80 < angle < 100 for angle in angles):
#             squares.append(approx)
# print(squares)
# overlap_process = non_max_suppression(squares)
# max_square = filter_inner_squares(squares,0.3)
#
# centers = [get_center(square) for square in max_square]
# print(centers)
# if len(centers) >= 3:
#     # corners = classify_corners(centers)
#     # missing_corner = calculate_missing_corner(corners)
#     selected_centers = centers[:3]
#     print(selected_centers)
#     missing_corner = find_fourth_center(selected_centers)
#     # print(missing_corner)
#     # fourth_square = find_4th_corner(corners)
#
#     for square in max_square:
#         print(square)
#         square = np.array(square, dtype=np.int32)
#         cv2.drawContours(image, [square], -1, (0, 255, 0), 1)
#
#     cv2.circle(image, missing_corner, 5, (255, 0, 0), -1)
#
# cv2.imshow('Final Squares', image)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

cap = cv2.VideoCapture(0)  # Thay `0` bằng đường dẫn video nếu muốn phát từ file

if not cap.isOpened():
    print("Không thể mở camera hoặc video")
    exit()

while True:
    ret, frame = cap.read()
    if not ret:
        print("Không thể đọc khung hình từ video")
        break

    # Tiền xử lý frame
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    ret3, th = cv2.threshold(gray, 50, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    edges = cv2.Canny(th, 50, 150)
    contours, _ = cv2.findContours(edges, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    squares = []

    for cnt in contours:
        approx = cv2.approxPolyDP(cnt, 0.02 * cv2.arcLength(cnt, True), True)
        if len(approx) == 4:
            p1, p2, p3, p4 = approx
            angles = is_perpendicular(p1, p2, p3, p4)
            (x, y, w, h) = cv2.boundingRect(approx)
            aspect_ratio = w / float(h)

            # Kiểm tra điều kiện hình vuông
            if 0.8 <= aspect_ratio <= 1.2 and is_square(approx) and all(80 < angle < 100 for angle in angles):
                squares.append(approx)

    # Lọc các hình vuông và tìm góc thứ 4
    max_square = filter_inner_squares(squares, 0.3)

    centers = [get_center(square) for square in max_square]
    if len(centers) >= 3:
        selected_centers = centers[:3]
        missing_corner = find_fourth_center(selected_centers)

        for square in max_square:
            square = np.array(square, dtype=np.int32)
            cv2.drawContours(frame, [square], -1, (0, 255, 0), 2)

        cv2.circle(frame, missing_corner, 5, (255, 0, 0), -1)

    # Hiển thị khung hình
    cv2.imshow('Realtime Detection', frame)

    # Nhấn 'q' để thoát
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Giải phóng tài nguyên
cap.release()
cv2.destroyAllWindows()
