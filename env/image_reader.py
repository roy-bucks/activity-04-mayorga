import cv2
from tkinter import filedialog, Tk

root = Tk()
root.withdraw()

#open the Finder/File Explorer
#To select the image file 
filepath = filedialog.askopenfilename()


#select the image flag
print("Select image flag")
print("1. color")
print("2. grayscale")
print("3. unchange")

flagInput = int(input())

if flagInput == 1:
    flag = 1
elif  flagInput == 2:
    flag = 0
elif flagInput == 3: 
    flag = -1
else: 
    flag = 1


#this approach close the window on MAC
cv2.startWindowThread()

#Begin reading the image 
image = cv2.imread(filepath, flag)

#Create a GUI window to display the image on screen
#cv2.imshow(window_title, image_array)
cv2.imshow("Keqing", image)

#Hold the window screen until a window close input is detected 
cv2.waitKey(0)

#Remove/delete created window from the screen and memory 
cv2.destroyAllWindows()
