import numpy as np
import cv2


def IFFT(magnitude, phase):
    reconstructed_fshift = magnitude * np.exp(1j * phase)
    reconstructed_f = np.fft.ifftshift(reconstructed_fshift)
    reconstructed_img = np.fft.ifft2(reconstructed_f)
    reconstructed_img = np.abs(reconstructed_img)
    reconstructed_img = np.uint8(255 * (reconstructed_img - np.min(reconstructed_img)) / np.ptp(reconstructed_img))
    return reconstructed_img

def fft(img):
    f = np.fft.fft2(img)
    fshift = np.fft.fftshift(f)
    magnitude = np.abs(fshift)
    phase = np.angle(fshift)
    return magnitude, phase

def swap_two_images(img1, img2):
    Modulus1, Phase1 = fft(img1)
    Modulus2, Phase2 = fft(img2)
    mimg1 = IFFT(Modulus1, Phase2)
    mimg2 = IFFT(Modulus2, Phase1)
    cv2.imshow("picJinkes", mimg1)
    cv2.imshow("picEyeMaskGirl", mimg2)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def mix_two_images(img1, img2):
    Modulus1, Phase1 = fft(img1)
    Modulus2, Phase2 = fft(img2)
    mimg1 = IFFT(Modulus1, Phase2)
    mimg2 = IFFT(Modulus2, Phase1)
    mix_img = cv2.addWeighted(mimg1, 0.5, mimg2, 0.5, 0)
    cv2.imshow("mix_img", mix_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == '__main__':
    img1 = cv2.imread("picJinkes.jpg", 0)
    img2 = cv2.imread("picEyeMaskGirl.jpg", 0)
    # cv2.imshow("img1", img1)
    # cv2.imshow("img2", img2)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    mix_two_images(img1, img2)

