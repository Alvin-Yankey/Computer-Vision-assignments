
import cv2  # import libraries

dark_image = cv2.imread(r'My photo.jpg')  # get image an image named 'My photo' from the folder

copy = dark_image.copy()  # make a copy of the image and name it new

brighter = cv2.convertScaleAbs(copy, alpha=2, beta=0)  # convert image to Abs and apply alpha=2 and beta=0

cv2.imshow('brighter image', brighter)  # show the darker image

cv2.imshow('dark image', dark_image)  # display the original image

while True:
    if cv2.waitKey(2) == ord("x"):  # wait for the condition of pressing key 'x'
        cv2.destroyAllWindows()  # close all windows if the above condition is met
        break  # end the operation
