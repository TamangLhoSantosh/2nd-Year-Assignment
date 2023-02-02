import cv2
vid = cv2.VideoCapture(0)
while True:
    ret, frame = vid.read()
    # Display the resulting frame
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    blurred_frame = cv2.GaussianBlur(gray, (5,5), 0)
    
    canny = cv2.Canny(blurred_frame, 100,150)
    cv2.imshow("Canny", canny)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
        
# After the loop release the cap object
vid.release()
# Destroy all the windows
cv2.destroyAllWindows()