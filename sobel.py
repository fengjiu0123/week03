import numpy as np
import cv2

img = cv2.imread('lenna.png')

x = cv2.Sobel(img, cv2.CV_16S, 1, 0)   # 对输入图像 img 进行水平方向的 Sobel 边缘检测，返回结果存储在变量 x 中。
y = cv2.Sobel(img, cv2.CV_16S, 0, 1)   # 对输入图像 img 进行垂直方向的 Sobel 边缘检测，返回结果存储在变量 y 中。
absX = cv2.convertScaleAbs(x)          # 将水平Sobel边缘检测结果 x 转换为绝对值，并将其存储在 absX 中。
absY = cv2.convertScaleAbs(y)          # 将垂直Sobel边缘检测结果 y 转换为绝对值，并将其存储在 absY 中。

# 将经过处理的水平和垂直边缘检测结果进行加权相加，生成最终的边缘检测结果，存储在 result_img 中。
result_img = cv2.addWeighted(absX, 0.5, absY, 0.5, 0)
# 显示命名为 "SobelEdgeDetection" 的窗口，展示经过 Sobel 边缘检测处理后的图像。
cv2.imshow("SobelEdgeDetection", result_img)
cv2.waitKey(0)