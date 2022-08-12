import cv2

fish_cascade = cv2.CascadeClassifier('cascade.xml')
cap = cv2.VideoCapture('pexels-taryn-elliott-5548177.mp4')
width= int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height= int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

writer= cv2.VideoWriter('basicvideo.mp4', cv2.VideoWriter_fourcc(*'MP4V'), 20, (width,height))


while cap.isOpened():
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    fishes = fish_cascade.detectMultiScale(gray,1.3,14)

    for (x,y,w,h) in fishes:
        cv2.rectangle(frame, (x,y), (x+w, y+h), (255,0,0), 3)


    cv2.imshow('img',frame)
    writer.write(frame)
    if cv2.waitKey(10)& 0xFF == ord('q'):
        break

cap.release()
writer.release()

cv2.destroyALLWindows()