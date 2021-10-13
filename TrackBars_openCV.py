import cv2
import numpy as np

def empty(a):  # empty function
    pass


# to create a new window for the track bars
# here we create 6 track bars Hue min, hue max, sat min, sat max, value min, value max
cv2.namedWindow("TrackBars")
cv2.resizeWindow("TrackBars", 640, 240)
cv2.createTrackbar("Hue min", "TrackBars", 99, 179, empty)  # value for hue is 0 to 179
cv2.createTrackbar("Hue max", "TrackBars", 168, 179, empty)
cv2.createTrackbar("Sat min", "TrackBars", 0, 255, empty)  # value for sat and value are 0 to 255
cv2.createTrackbar("Sat max", "TrackBars", 232, 255, empty)
cv2.createTrackbar("value min", "TrackBars", 120, 255, empty)  # and we keep all max values at max
cv2.createTrackbar("value max", "TrackBars", 231, 255, empty)

while True:
    img = cv2.imread(r"D:\backup2020\IMG.jpg", cv2.IMREAD_COLOR)
    imgHSV = cv2.cvtColor(img, cv2.COLOR_RGB2HSV)

    h_min = cv2.getTrackbarPos("Hue min", "TrackBars")
    h_max = cv2.getTrackbarPos("Hue max", "TrackBars")
    s_min = cv2.getTrackbarPos("Sat min", "TrackBars")
    s_max = cv2.getTrackbarPos("Sat max", "TrackBars")
    v_min = cv2.getTrackbarPos("value min", "TrackBars")
    v_max = cv2.getTrackbarPos("value max", "TrackBars")
    print(h_min, h_min, s_min, s_max, v_max, v_min)

    lower=np.array([h_min, s_min, v_min])
    upper=np.array([h_max, s_max, v_max])
    mask=cv2.inRange(imgHSV, lower,upper) #for binary image
    imgResult = cv2.bitwise_and(img,img,mask=mask)  #for colored image


    cv2.imshow("my_img", img)
    cv2.imshow("my_img_hsv", imgHSV)
    cv2.imshow("my_mask", mask)
    cv2.imshow("my_mask_result", imgResult)

    cv2.waitKey(1)

    # cv2.destroyAllWindows()
