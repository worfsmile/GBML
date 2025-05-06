import cv2
import numpy as np
import matplotlib.pyplot as plt

def fft(img):
    f = np.fft.fft2(img)
    fshift = np.fft.fftshift(f)
    magnitude = np.abs(fshift)
    phase = np.angle(fshift)
    return magnitude, phase


if __name__ == '__main__':
    # 1. 读取图像并转换为灰度图
    img = cv2.imread('your_image.jpg', cv2.IMREAD_GRAYSCALE)

    # 2. 执行二维傅里叶变换
    f = np.fft.fft2(img)

    # 3. 移动零频率分量到频谱中心
    fshift = np.fft.fftshift(f)

    # 4. 计算模（Magnitude）和相位（Phase）
    magnitude = np.abs(fshift)
    phase = np.angle(fshift)

    # 5. 可视化模和相位
    # 对模进行对数尺度的缩放，使其更容易查看
    magnitude_log = np.log(magnitude + 1)  # +1 是为了避免对数为负无穷

    # 绘制原图、模和相位
    plt.figure(figsize=(12, 4))

    plt.subplot(1, 3, 1)
    plt.imshow(img, cmap='gray')
    plt.title("Original Image")
    plt.axis('off')

    plt.subplot(1, 3, 2)
    plt.imshow(magnitude_log, cmap='gray')
    plt.title("Magnitude Spectrum (Log Scale)")
    plt.axis('off')

    plt.subplot(1, 3, 3)
    plt.imshow(phase, cmap='gray')
    plt.title("Phase Spectrum")
    plt.axis('off')

    plt.tight_layout()
    plt.show()
