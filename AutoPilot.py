import numpy as np
from PIL import ImageGrab
import cv2
import time
from ctype import PressKey, ReleaseKey, W, A, S, D

x1 = 150
y1 = 400

x2 = 325
y2 = 400


x3 = 500
y3 = 400

def maskk(screen, vertex):
    mask = np.zeros_like(screen)
    cv2.fillPoly(mask, vertex, 255)
    mask1 = cv2.bitwise_and(screen, mask)
    return mask1

def dlinesleft(screen, lines):
    global x1, y1
    try:
        for line in lines:
            cor = line[0]
            cv2.line(screen, (cor[0], cor[1]), (cor[2], cor[3]), [0, 255, 50], 5)
            x1 = lines[0][0][0]
            y1 = lines[0][0][1]
    except:
        pass

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
def dlinesright(screen, lines1):
    global x3, y3
    try:
        for line in lines1:
            cor = line[0]
            cv2.line(screen, (cor[0], cor[1]), (cor[2], cor[3]), [0, 255, 50], 5)
            x3 = lines1[0][0][0]
            y3 = lines1[0][0][1]
    except:
        pass

t = time.process_time()
print(t)
while True:
    window = np.array(ImageGrab.grab(bbox=(10, 10, 640, 480)))
    #print("Время кадра " + str(time.process_time() -t))
    t = time.process_time()
    im = cv2.cvtColor(window, cv2.COLOR_BGR2GRAY)
    window1 = cv2.cvtColor(window, cv2.COLOR_BGR2RGB)
    # sobelx = cv2.Sobel(im, cv2.CV_64F, 1, 0, ksize= 5) #играться с ksize
    # sobely = cv2.Sobel(im, cv2.CV_64F, 0, 1, ksize= 5)
    # sob = (sobelx + sobely)
    Can = cv2.Canny(im, 100, 300, 7) #играемся с 2-4
    # s
s
    vertexl = np.array([[10, 360], [10, 240], [200, 240], [200, 360]])
    vertexm = np.array([[250, 360], [250, 240], [390, 240], [390, 360]])
    vertexr = np.array([[440, 360], [440, 240], [630, 240], [630, 360]])
s
    Canl = maskk(Can, [vertexl])
    Canm = maskk(Can, [vertexm])
    Canr = maskk(Can, [vertexr])

    linesl = cv2.HoughLinesP(Canl, 1, np.pi / 180, 100, 50, 100)
    linesm = cv2.HoughLinesP(Canm, 1, np.pi / 180, 100, 50, 100)
    linesr = cv2.HoughLinesP(Canr, 1, np.pi / 180, 100, 50, 100)

    dlinesleft(window1, linesl)
    dlinesmid(window1, linesm)
    dlinesright(window1, linesr)


    cv2.line(window1, (x1, y1), (150, 400), [100, 0, 100], 5)
    cv2.line(window1, (x2, y2), (325, 400), [100, 0, 100], 5)
    cv2.line(window1, (x3, y3), (500, 400), [100, 0, 100], 5)

    d1 = int(np.sqrt((x1-150)**2+(y1-400)**2))
    d2 = int(np.sqrt((x2-325)**2+(y2-400)**2))
    d3 = int(np.sqrt((x3 - 500) ** 2 + (y3 - 400) ** 2))
    if (d2>100):
        PressKey(W)
        time.sleep(0.5)
        ReleaseKey(W)
        time.sleep(0.5)
    else:
        PressKey(S)
        time.sleep(0.5)
        ReleaseKey(S)
        time.sleep(0.5)
    cv2.putText(window1, " " + str(d1) + " ", (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 5)
    cv2.putText(window1, " " + str(d2) + " ", (300, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 5)
    cv2.putText(window1, " " + str(d3) + " ", (500, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 5)

    cv2.imshow("window_new", window1)


    if cv2.waitKey(30) == ord("q"):
        cv2.destroyAllWindows()
        break
