import numpy as np
import cv2

# 双线性插值
# 定义名为 bili_near_interpolation 的函数，执行双线性插值。该函数接受一个图像 img 和两个整数 num_h、num_w 作为输入参数。
def bili_near_interpolation(img, num_h, num_w):
    original_h, original_w, original_t = img.shape            # 获取输入图像的高度、宽度和通道数。
    img_r = np.zeros([num_h, num_w, original_t], np.uint8)    # 创建一个新的图像数组（矩阵）img_r，用于存储插值后的图像。数组的大小为 (num_h, num_w, original_t)。

# 三重循环，分别遍历通道数 k、目标图像高度 j 和宽度 i
# 然后根据双线性插值的公式，计算出插值点 (x, y) 处的像素值 z0 和 z1。
# 最后，根据双线性插值的公式，计算出插值后的像素值，并将其存储在新的图像数组 img_r 中
    for k in range(original_t):
        for j in range(num_h):
            for i in range(num_w):
                x = (i+0.5)*original_w / num_w - 0.5
                y = (j+0.5)*original_h / num_h - 0.5
                x0 = int(np.floor(x))
                x1 = min(x0+1, original_w-1)
                y0 = int(np.floor(y))
                y1 = min(y0+1, original_h-1)

                z0 = (x1-x) * img[y0, x0, k] + (x-x0) * img[y0, x1, k]
                z1 = (x1-x) * img[y1, x1, k] + (x-x0) * img[y1, x1, k]
                img_r[j, i, k] = int((y1-y)*z0+(y-y0)*z1)
    return img_r


img = cv2.imread('lenna.png')
img_ni = bili_near_interpolation(img, 800, 800)
cv2.imshow("lenna", img)
cv2.imshow("lenna_nl", img_ni)
cv2.waitKey(0)