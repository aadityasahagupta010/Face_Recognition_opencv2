import cv2,time
face_cascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
video=cv2.VideoCapture(0)
while True:
    check,frame=video.read()
    face=face_cascade.detectMultiScale(frame,
    scaleFactor=1.05,
    minNeighbors=5)
    for x,y,w,h in face:
        frame=cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),4)

    cv2.imshow("Bhaiya_ji_Smile",frame)
    #resi=cv2.resize(img,(int(img.shape[1]/3),int(img.shape[0]/3)))
    key = cv2.waitKey(1)
    if key==ord('q'):
        break

video.release()
cv2.destroyAllWindows()
