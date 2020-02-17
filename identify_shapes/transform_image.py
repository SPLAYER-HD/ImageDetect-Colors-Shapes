'''Class to transform image into a valid binary to find contours'''
# import the necessary packages
import cv2

class TransformImage():
    def transform(self, image):
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        gray = cv2.GaussianBlur(gray, (5,5), 0)
        edges = cv2.Canny(gray, 60, 0)
        return edges
