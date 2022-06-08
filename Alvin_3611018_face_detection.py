import cv2  # import cv2 to use its libraries

cap = cv2.VideoCapture(0)  # create a camera view finder element in a windows form with the first camera device attached

cascade_path = 'C:/Program Files/Python310/Lib/site-packages/cv2/data/' \
               'haarcascade_frontalcatface.xml'  # denote the location of the cascade files in use
face_cascade = cv2.CascadeClassifier(cascade_path)  # initialize the default haar cascade files in open cv

while True:  # set the assertion of the conditions above and continue if assertion is true
    _, faces_detected = cap.read()  # obtain frames from the camera
    faces = face_cascade.detectMultiScale(faces_detected, scaleFactor=1.1, minNeighbors=4, minSize=(45, 45),
                                          flags=cv2.CASCADE_SCALE_IMAGE)  # identify face pixels in the frames obtained

    for x, y, width, height in faces:  # set a preamble dimension for all instances with a face
        cv2.rectangle(faces_detected, (x, y), (x + width, y + height), color=(255, 255,
                                                                              255),
                      thickness=2)  # place a white square border on each face element recognized

    cv2.imshow("faces", faces_detected)  # display a viewfinder with a label 'faces' showing results of face recognition

    if cv2.waitKey(1) == ord("x"):  # wait for a condition when the button x is pressed

        break  # stop the operation if the above condition is satisfied

cap.release()  # set the camera device status to available
cv2.destroyAllWindows()  # close all opened windows
