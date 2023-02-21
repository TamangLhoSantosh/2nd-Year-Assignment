# importing required modules
import cv2

# Load the Haar cascade classifier
face_cascade = cv2.CascadeClassifier('Virtual/lib/python3.10/site-packages/cv2/data/haarcascade_frontalface_alt.xml')

# reading from camera
vid = cv2.VideoCapture(0)

# running until exit
while True:
    ret, frame = vid.read()
    
    if ret:
    
    # Convert the frame to grayscale for processing
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Detect faces in the grayscale frame
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

        # Draw rectangles around the detected faces
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

        # Display the processed frame with detected faces
        cv2.imshow('Face Detection', frame)

        # Check for the 'q' key to quit the program
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break
        
# After the loop release the cap object
vid.release()
# Destroy all the windows
cv2.destroyAllWindows()