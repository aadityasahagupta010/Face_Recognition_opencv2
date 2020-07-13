import cv2,time
import webbrowser
smile_cascade=cv2.CascadeClassifier("haarcascade_smile.xml")
video=cv2.VideoCapture(0)
while True:
    check,frame=video.read()
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    smile=smile_cascade.detectMultiScale(gray,
    scaleFactor=1.8,
    minNeighbors=8)
    #init_smile=smile
    for x,y,w,h in smile:
        frame=cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),4)

    cv2.imshow("majje_bhai",frame)
    #resi=cv2.resize(img,(int(img.shape[1]/3),int(img.shape[0]/3)))
    key = cv2.waitKey(1)
    if key==ord('q'):
        break

video.release()
cv2.destroyAllWindows()
