import numpy as np
from PIL import ImageGrab
import cv2
from time import *
from ctype import PressKey, ReleaseKey, W, S, D, A
x1 = 10
y1 = 10
x2 = 325
y2 = 400


def maskk(screen, vertex):
    mask = np.zeros_like(screen)
    cv2.fillPoly(mask, vertex, 255)
    mask1 = cv2.bitwise_and(screen, mask)
    return mask1

def dlinesmid(screen, lines1):
    global x2, y2
    try:
        for line in lines1:
            cor = line[0]
            cv2.line(screen, (cor[0], cor[1]), (cor[2], cor[3]), [0, 255, 50], 5)
            x2 = lines1[0][0][0]
            y2 = lines1[0][0][1]
    except:
        pass
def dlines(screen,lines):
    global x1,y1
    try:
        for line in lines:
            coords=line[0]
            cv2.line(screen,(coords[0],coords[1]),(coords[2],coords[3]),[0, 100,200],5)
            x1=lines[0][0][0]
            y1=lines[0][0][1]
    except:
        pass

while True:
    window1 = np.array(ImageGrab.grab(bbox=(10, 10, 640, 480)))
    im = cv2.cvtColor(window1, cv2.COLOR_BGR2GRAY)
    window11 = cv2.cvtColor(window1, cv2.COLOR_BGR2RGB)
    # sobelx = cv2.Sobel(im, cv2.CV_64F, 1, 0, ksize= 5) #играться с ksize
    # sobely = cv2.Sobel(im, cv2.CV_64F, 0, 1, ksize= 5)
    # sob = (sobelx + sobely)
    Can1 = cv2.Canny(im, 10, 300, 5)
    Can1 = cv2.GaussianBlur(Can1, (3, 3), 0)
    vertexm = np.array([[200, 350], [200, 250], [400, 250], [400, 350]])
    Canm = maskk(Can1, [vertexm])
    linesm = cv2.HoughLinesP(Canm, 1, np.pi / 180, 10, 100, 25)
    dlinesmid(window11, linesm)
    cv2.line(window11, (x2, y2), (325, 400), [100, 0, 100], 5)
    d2 = int(np.sqrt((x2 - 325) ** 2 + (y2 - 400) ** 2))
    cv2.putText(window11, " " + str(d2) + " ", (300, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 5)

    window = np.array(ImageGrab.grab(bbox=(500, 400, 580, 460)))
    window2 = np.repeat(window, 2, axis = 1)
    w_hsv =cv2.cvtColor(window, cv2.COLOR_BGR2HSV)

    l_r = np.array([110, 100, 100])
    u_r = np.array([255, 255, 255])
    mask = cv2.inRange(w_hsv, l_r, u_r)

    kernel = np.ones((2, 2), np.float32)/255
    dilat = cv2.dilate(mask, kernel, iterations=1)
    Can=cv2.Canny(dilat, 100, 300, 7)

    Can=cv2.GaussianBlur(Can, (3, 3), 0)
    lines=cv2.HoughLinesP(Can, 1 , np.pi/180, 10, 10, 10)
    dlines(window2,lines)
    cv2.line(window2,(x1,y1),(40,35),[100,0 ,100],3)

    dx=x1-40
    dy=35-y1
    a = np.arctan2(dy, dx)
    print(a)
    if d2>80:
        if np.abs(a)>1.9:
            PressKey(W)
            PressKey(A)
            sleep(0.8)
            ReleaseKey(W)
            ReleaseKey(A)
            ReleaseKey(S)
            ReleaseKey(D)
            sleep(0.1)
            print("Влево")
        elif np.abs(a)<1.6:
            PressKey(W)
            PressKey(D)
            sleep(0.8)
            ReleaseKey(W)
            ReleaseKey(A)
            ReleaseKey(S)
            ReleaseKey(D)
            sleep(0.1)
            print("Вправо")
        else:
            PressKey(W)
            sleep(1)
            ReleaseKey(W)
            ReleaseKey(A)
            ReleaseKey(S)
            ReleaseKey(D)
            sleep(0.1)
            print("Прямо")
    else:
        PressKey(S)
        sleep(1)
        ReleaseKey(W)
        ReleaseKey(A)
        ReleaseKey(S)
        ReleaseKey(D)
        sleep(0.1)
        print('Назад')
    cv2.imshow("window_nav", window2)
    cv2.imshow("windowm", window11)

    if cv2.waitKey(30)==ord("q"):
        cv2.destroyAllWindows()
        break