import numpy as numpy
import cv2

# Opens video file
video=cv2.VideoCapture('test_data/1.wmv')
# Gets the fps, width, and height of the video
fps=int(video.get(cv2.CAP_PROP_FPS))
width  = int(video.get(cv2.CAP_PROP_FRAME_WIDTH)) 
height = int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))
size=(width,height)
# print(fps,width,height)

# Define the output file
fourcc=cv2.VideoWriter_fourcc('m','p','4','v')
out=cv2.VideoWriter('output.mp4',fourcc,fps,size)

# Loops through each video frame and saves to out
while(video.isOpened()):
    ret,frame = video.read()
    if ret==True:
        # print(frame)
        out.write(frame)
    else:
        break

# Frees everything up
video.release()
out.release()