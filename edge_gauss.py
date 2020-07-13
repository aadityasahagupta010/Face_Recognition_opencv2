import cv2,pandas
from datetime import datetime
first_frame=None
status_list=[None,None]
dt=[]
df=pandas.DataFrame(columns=["Start","End"])
video=cv2.VideoCapture(0)
while True:
    check,frame = video.read()
    status=0
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    gray=cv2.GaussianBlur(gray,(21,21),0)

    if first_frame is None:
        first_frame=gray
        continue

    delta_frame=cv2.absdiff(first_frame,gray)
    thresh=cv2.threshold(delta_frame,30,255,cv2.THRESH_BINARY)[1]
    thresh=cv2.dilate(thresh,None,2)
    (cnts,_)=cv2.findContours(thresh.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    for contour in cnts:
         if cv2.contourArea(contour) < 1000:
             continue
         status=1

         (x,y,w,h)=cv2.boundingRect(contour)
         cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),4)
    status_list.append(status)
    status_list=status_list[-2:]


    if status_list[-1]==0 and status_list[-2]==1:
        dt.append(datetime.now())
    if status_list[-1]==1 and status_list[-2]==2:
        dt.append(datetime.now())



    cv2.imshow("col",frame)


    key=cv2.waitKey(1)
    if key==ord('q'):
        if status==1:
            dt.append(datetime.now())
        break

for i in range(0,len(dt),2):
    df=df.append({"Start":dt[i],"End":dt[i+1]},ignore_index=True)



video.release()
cv2.destroyAllWindows()
