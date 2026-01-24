import cv2
face_casecade=cv2.CascadeClassifier(
    cv2.data.haarcascades+"haarcascade_frontalface_default.xml"
)
eye_cascade=cv2.CascadeClassifier(
    cv2.data.haarcascades+"haarcascade_eye.xml"
)
cap=cv2.VideoCapture(0)
while True:
    ret,frame =cap.read()
    if not ret:
        print("Camera not detected")
        break
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    faces=face_casecade.detectMultiScale(gray,1.3,5)
    status = "Eyes Closed"
    for (x,y,w,h) in faces:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
        roi_gray=gray[y:y+h,x:x+w]
        eyes=eye_cascade.detectMultiScale(roi_gray,1.1,4)
        if len(eyes) >= 2:
            status = "Eyes Open"
    cv2.putText(frame,status,(30,50),cv2.FONT_HERSHEY_SIMPLEX,
                1,(0,0,255),2)
    cv2.imshow("Eye Open/Close Detection",frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
