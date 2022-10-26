import cv2

def video_cap(cap):
    
    # Capture frame-by-frame
    ret, frame = cap.read()
    #while True:
    # Display the resulting frame
    cv2.imshow('frame',frame)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        # When everything done, release the capture
        cap.release()
        cv2.destroyAllWindows() 

#cap = cv2.VideoCapture("/dev/video1") # check this  
#while True:
    #video_cap(cap)


    