import cv2
import numpy as np
import matplotlib.pyplot as plt

def IFFT(magnitude, phase):
    reconstructed_fshift = magnitude * np.exp(1j * phase)
    reconstructed_f = np.fft.ifftshift(reconstructed_fshift)
    reconstructed_img = np.fft.ifft2(reconstructed_f)
    reconstructed_img = np.abs(reconstructed_img)
    return reconstructed_img


if __name__ == '__main__':
    # 1. 读取图像并转换为灰度图
    img = cv2.imread('your_image.jpg', cv2.IMREAD_GRAYSCALE)

    # 2. 执行傅里叶变换
    f = np.fft.fft2(img)
    fshift = np.fft.fftshift(f)

    # 3. 计算频域的模和相位
    magnitude = np.abs(fshift)
    phase = np.angle(fshift)

    # 4. 根据模和相位重建频谱
    reconstructed_fshift = magnitude * np.exp(1j * phase)

    # 5. 对频谱进行逆傅里叶变换
    reconstructed_f = np.fft.ifftshift(reconstructed_fshift)  # 移回零频率分量
    reconstructed_img = np.fft.ifft2(reconstructed_f)
    reconstructed_img = np.abs(reconstructed_img)  # 取绝对值得到图像

    # 6. 显示结果
    plt.figure(figsize=(12, 4))

    plt.subplot(1, 3, 1)
    plt.imshow(img, cmap='gray')
    plt.title("Original Image")
    plt.axis('off')

    plt.subplot(1, 3, 2)
    plt.imshow(reconstructed_img, cmap='gray')
    plt.title("Reconstructed Image")
    plt.axis('off')

    plt.tight_layout()
    plt.show()
