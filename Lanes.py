import time
from PIL import ImageGrab
import cv2
import numpy as np

def lanes(img,lines):
    lineimg = np.zeros_like(img)
    if lines is not None:
        for line in lines:
            if line is not None:
                x1, y1, x2, y2 = line.reshape(4)
                try:
                    cv2.line(lineimg, (x1, y1), (x2, y2), (255, 0, 0), 13)
                except OverflowError:
                    pass
    return lineimg


def regionOfInterest(img):
    vertices = np.array([[(10, 635), (10, 400),(350,320),(460, 320), (800, 400), (800, 635)]])
    mask = np.zeros_like(img)
    cv2.fillPoly(mask,vertices,255)
    masked = cv2.bitwise_and(img,mask)
    return masked


def processImg(grabbed_Image) :
    try:
        lane = np.copy(grabbed_Image)
        imgg = cv2.cvtColor(grabbed_Image, cv2.COLOR_BGR2GRAY)
        imgb = cv2.GaussianBlur(imgg, (5, 5), 0)
        edges = cv2.Canny(imgb, threshold1=50, threshold2=150)
        mask = regionOfInterest(edges)
        lines = cv2.HoughLinesP(mask, cv2.HOUGH_PROBABILISTIC,
                                np.pi / 180, 180, np.array([]), 30, 15)
        lanes(mask,lines)
        return mask
    except TypeError:
        pass

def main():
    for i in range(5):
        time.sleep(1)
        print(i)
    while(True):
        grabscreen = np.array(ImageGrab.grab(bbox=(50,50,800,600)))
        try:
            pimg = processImg(grabscreen)
            cv2.imshow('Capture',cv2.cvtColor(pimg, cv2.COLOR_BGR2RGB))
            if cv2.waitKey(25) & 0xFF == ord('q'):
                cv2.destroyAllWindows()
                break
        except TypeError:
            pass

main()