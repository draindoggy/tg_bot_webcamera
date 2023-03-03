import cv2

cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 600) # ширина кадров в видеопотоке
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480) # высота кадров в видеопотоке
while(True):
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow('вебка', frame)
    if cv2.waitKey(1) & 0xFF == ord('e'): # камера закроется, если нажать на английскую букву e
        break
cap.release()
cv2.destroyAllWindows()