import cv2
from subprocess import Popen
#import Button
import hussle_image
def startCam():
    while (1):
        count = 1;
        #use 1 for extern webcam
        cap = cv2.VideoCapture(0)

        cap.set(3,1000)
        cap.set(4,1000)

        while(1):
            # Capture frame-by-frame
            ret, frame = cap.read()

            ''' Display the resulting frame
                and draw a rectangle in the middel of the frame
                this rectangle is only correctly placed on a VGA webcam'''

            cv2.rectangle(frame, (114, 34), (525, 445), (255, 255, 255), 10)
            cv2.imshow('frame',frame)

           # if Button.readbutton() ==1 or cv2.waitKey(1) & 0xFF == ord('q'):
            if cv2.waitKey(1) & 0xFF == ord('q'):
                cap.release()
                cv2.destroyWindow('frame')
                cv2.imwrite('picture.jpg', frame)
                hussle_image.temp()

               #use this function to start the printer

               # p = Popen("C:\Program Files (x86)\IrfanView\print.bat", cwd=r"C:\Users\janka\PycharmProjects\opencv_tutorial")
                #stdout, stderr = p.communicate()
                break


