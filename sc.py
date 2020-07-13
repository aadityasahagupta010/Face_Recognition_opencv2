import cv2
face_cascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
img=cv2.imread("pic.jpg")
gray_im=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

face=face_cascade.detectMultiScale(gray_im,
scaleFactor=1.09,
minNeighbors=5)

for x,y,w,h in face:
    img=cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),4)

resi=cv2.resize(img,(int(img.shape[1]/3),int(img.shape[0]/3)))
cv2.imshow("dekh",resi)
cv2.waitKey(0)
cv2.destroyAllWindows()
