import numpy as np
import cv2

img = cv2.imread('lenna.png')
# 将彩色图像转换为灰度图像，使用 cv2.cvtColor 函数。
img_g = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# 对灰度图像进行直方图均衡化，使用 cv2.equalizeHist 函数。
img_g_h = cv2.equalizeHist(img_g)
# 生成直方图.计算均衡化后灰度图像的直方图，使用 cv2.calcHist 函数。
hist = cv2.calcHist([img_g_h], [0], None, [256], [0,256])
# 显示直方图均衡化前后的灰度图像并将它们水平堆叠显示，使用 cv2.imshow 函数。
cv2.imshow("Histogram Equalization", np.hstack([img_g, img_g_h]))

# 彩色直方图均衡化
(b, g, r) = cv2.split(img)               # 将彩色图像分离成三个通道的颜色通道。
bh = cv2.equalizeHist(b)                 # 对每个颜色通道进行直方图均衡化，得到均衡化后的通道 be, ge, re。
gh = cv2.equalizeHist(g)
rh = cv2.equalizeHist(r)
img_h = cv2.merge((bh,gh,rh))            # 将三个均衡化后的颜色通道合并，得到最终的彩色直方图均衡化图像
cv2.imshow("Histogram Equalization", np.hstack([img, img_h]))    # 显示彩色直方图均衡化前后的图像并将它们水平堆叠显示。
cv2.waitKey(0)