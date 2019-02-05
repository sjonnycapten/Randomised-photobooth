import cv2 as cv
import random

def temp():
    blockSize = 50
    blockAmount = 8

    #the frame grabbed from the webcam
    img = cv.imread('picture.jpg',1)
    #a white canvas so the original picture is stored
    img2= cv.imread('canvas.png',1)

    partlist = []
    count1 =0
    for y in range(0, blockAmount):
        for x in range(0, blockAmount):
            part = img[(y * blockSize) + 40:((y + 1) * blockSize) + 40, (x * blockSize) + 120:((x + 1) * blockSize) + 120]
            partlist.append(part)

    random.shuffle(partlist)

    count =0
    for y in range(0, blockAmount):
        for x in range(0, blockAmount):
            #cv.imshow(str(count),partlist[count])
            img2[y * blockSize:(y + 1) * blockSize, x * blockSize:(x + 1) * blockSize] = partlist[count]
            count += 1
    cv.imwrite('output.png',img2)
    cv.destroyWindow('image')


