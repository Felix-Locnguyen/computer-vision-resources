'''
Note:
Ảnh sẽ có 3 kênh: red, green, blue
Chiều của ảnh sẽ được viết dưới dạng (h,w,c) ví dụ (1100,150,3)
    - h (height): là chiều cao của ảnh.
    - w (width): là chiều rộng của ảnh.
    - c (channels): số kênh màu.
Khoảng biến giá trị  của 1px = [0,255]
'''


'''
======================================================================
CÁC DẠNG INPUT ĐẦU VÀO:
======================================================================
'''

import os 
import cv2 
import numpy as np

# # Read image 
# img_path = os.path.join("Datasets", "Images", "earth.jpg")
# img = cv2.imread(img_path)

# # write image
# # cv2.imwrite(os.path.join("Datasets", "Images", "earth_copy.jpg"), img)

# # Visualise image 

# cv2.imshow('image',img)
# cv2.waitKey(0) # nếu không có thì ảnh sẽ hiện và tắt liền 


# # Read video

# video_path = f"video_path"

# video = cv2.VideoCapture(video_path)

# # Visualise image 
# ret = True 
# while ret:
#     ret, frame = video.read()
#     if ret:
#         cv2.imshow(frame)
#         cv2.waitKey(40)
# # giải phóng bộ nhớ và kết thúc 
# video.release()
# cv2.destroyAllWindows()
    

# # Read webcam 
# webcam = cv2.VideoCapture(0)

# # Visualise webcam 
# ret = True 
# while ret:
#     ret, frame = video.read()
#     if ret:
#         cv2.imshow(frame)
#         if cv2.waitKey(0) & 0xFF == ord('q'): # ấn q để tắt
#             break

# # giải phóng bộ nhớ và kết thúc 
# video.release()
# cv2.destroyAllWindows()



'''
======================================================================
Basic operations (CÁC THAO TÁC CƠ BẢN)
======================================================================
'''
# # THAI ĐỔI KÍCH THƯỚC HÌNH ẢNH

# img_path = os.path.join("Datasets", "Images", "earth.jpg")
# img = cv2.imread(img_path)

# resize_img = cv2.resize(img,(480,640))
# print(img.shape)

# cv2.imshow('image',resize_img)
# cv2.waitKey(0) 



# # CROP 
# img_path = os.path.join("Datasets", "Images", "earth.jpg")
# img = cv2.imread(img_path)

# crop_img = img[320:640, 420:840]

# cv2.imshow('image',crop_img)
# cv2.waitKey(0) 


'''
======================================================================
Colorspaces (không gian màu)
======================================================================
'''


# img_path = os.path.join("computer-vision-resources","Datasets", "Images", "earth.jpg")
# img = cv2.imread(img_path)

# img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# img_hsv = cv2.cvtColor(img,cv2.COLOR_HSV2BGR)       # không gian màu HSV

# cv2.imshow('image1',img)
# cv2.imshow('image2',img_hsv)
# cv2.waitKey(0) 


'''
======================================================================
Blurring (làm mờ hình ảnh)
======================================================================
'''
# img_path = os.path.join("computer-vision-resources","Datasets", "Images", "earth.jpg")
# img = cv2.imread(img_path)

# k_size = 11 # mức độ mờ
# img_blur = cv2.blur(img,(k_size,k_size)) #cách 1  # mờ theo chiều x,y
# img_gaussian_blur = cv2.GaussianBlur(img,(k_size,k_size),5) #cách 1
# img_median_blur = cv2.medianBlur(img,k_size)

# cv2.imshow('img_median_blur', img_median_blur)
# cv2.imshow('img_blur', img_blur)
# cv2.imshow('img_gaussian_blur', img_gaussian_blur)
# cv2.waitKey(0) 


'''
======================================================================
Threshold (Phân loại điểm sáng)
======================================================================
'''

# img_path = os.path.join("Datasets", "Images", "earth.jpg")
# img = cv2.imread(img_path)

# img_gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

# ret, thresh = cv2.threshold(img_gray, 50, 255, cv2.THRESH_BINARY) # phương pháp 1
#     # 50 là giá trị ngưỡng 
#     # các giá trị trên 50 giá trị chuyển đổi thành 255
#     # phân ngưỡng nhị phân.
# # thresh = cv2.blur(thresh,(20,20)) # kết hợp với nhiều phương pháp để cải thiện kể quả
# adaptivethresh = cv2.adaptiveThreshold(img_gray,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,21,30)
#     # img_gray: ảnh đầu vào (ảnh mức xám).
#     # 255: giá trị tối đa sau khi phân ngưỡng (thường là 255 cho ảnh trắng).
#     # cv2.ADAPTIVE_THRESH_GAUSSIAN_C: cách tính ngưỡng. Ở đây dùng Gaussian-weighted sum của vùng lân cận rồi trừ đi hằng số C.
#     # cv2.THRESH_BINARY: kiểu phân ngưỡng nhị phân (pixel > ngưỡng → 255, ngược lại → 0).
#     # 21: kích thước khối (block size). Mỗi vùng 21×21 pixel sẽ được tính ngưỡng riêng.
#     # 30: hằng số C. Giá trị ngưỡng tính được sẽ bị trừ đi 30 để điều chỉnh.

# cv2.imshow('img_gray', img_gray)
# cv2.imshow('thresh', thresh)
# cv2.imshow('adaptivethresh', adaptivethresh)

# cv2.waitKey(0) 

'''
======================================================================
Edge detection (Đường viền)
======================================================================
'''
# img_path = os.path.join("Datasets", "Images", "earth.jpg")
# img = cv2.imread(img_path)

# img_edge = cv2.Canny(img,100,200) 
# img_edge_d = cv2.dilate(img_edge,np.ones((3,5),dtype=np.int8))
# img_erode = cv2.erode(img_edge_d,np.ones((3,5),dtype=np.int8))

# cv2.imshow('img_edge', img_edge)
# cv2.imshow('img_edge_d', img_edge_d) # tăng độ dày cho đường viền 
# cv2.imshow('img_erode', img_erode) # làm mỏng đường viền 

# cv2.waitKey(0)

'''
======================================================================
DRAWING
======================================================================
'''

# img_path = os.path.join("Datasets", "Images", "earth.jpg")
# img = cv2.imread(img_path)

# #line
# cv2.line(img,(100,150),(300,450),(0,255,0), thickness=3)
# #rectangle
# cv2.rectangle(img,(200,350),(450,600),(0,255,0),thickness=3)
# #circle
# cv2.circle(img,(300,400),6,(0,255,0),thickness=3)
# #text
# cv2.putText(img,"hello world",(500,700),cv2.FONT_HERSHEY_SIMPLEX,3,(0,255,255),thickness=10)
# cv2.imshow('img', img) 

# cv2.waitKey(0)

'''
======================================================================
Contours
======================================================================
'''


img_path = os.path.join("Datasets", "Images", "bee.png")
img = cv2.imread(img_path)
img_gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

ret, thresh = cv2.threshold(img_gray,127,255,cv2.THRESH_BINARY_INV)
contour, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE) 

for cnt in contour:
    if cv2.contourArea(cnt) > 350:
        # cv2.drawContours(img,cnt,-1,(0,255,0),3)
        x1,y1,w,h = cv2.boundingRect(cnt)
        cv2.rectangle(img,(x1,y1),(x1 + w, y1 + h),(0,255,0),2)
cv2.imshow('img', img) 
cv2.imshow('thresh', thresh) 
cv2.waitKey(0)