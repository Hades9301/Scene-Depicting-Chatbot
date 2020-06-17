# import the necessary packages
from imutils.video import VideoStream
from pyzbar import pyzbar
import argparse
import datetime
import imutils
import time
import pyttsx3
import cv2

import pygame,time
import sys,math
import pyttsx
from pygame import gfxdraw
import threading 
import os
PI = math.pi;


pygame.init()
screen = pygame.display.set_mode((640, 480))
back = (255,255,255);
color = (255,255,0);
i=1;

def speak():
	global i
	global text
	engine = pyttsx.init()
	engine.say(text)
	engine.runAndWait();
	i=0;

def face():
	mouth_flag = 'false';

	while i:
			
		time.sleep(0.25)
		screen.fill(back);
		pygame.gfxdraw.filled_circle(screen,320,240,100,color);
		pygame.gfxdraw.filled_circle(screen,270,210,20,(0,0,0));
		pygame.gfxdraw.filled_circle(screen,370,210,20,(0,0,0));
		if mouth_flag=='false':
			pygame.gfxdraw.arc(screen,320,240,75,25, 155, (0,0,0))
			mouth_flag='true';
		else:
			pygame.gfxdraw.line(screen,270,290,370,290,(0,0,0));
			mouth_flag='false';
			pygame.display.update();




# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-o", "--output", type=str, default="barcodes.csv",
	help="path to output CSV file containing barcodes")
args = vars(ap.parse_args())

# initialize the video stream and allow the camera sensor to warm up
print("[INFO] starting video stream...")
vs = VideoStream(src=0).start()
# vs = VideoStream(usePiCamera=True).start()
time.sleep(2.0)

# open the output CSV file for writing and initialize the set of
# barcodes found thus far
csv = open(args["output"], "w")
found = set()
text=""

# loop over the frames from the video stream
while True:
	# grab the frame from the threaded video stream and resize it to
	# have a maximum width of 400 pixels
	frame = vs.read()
	frame = imutils.resize(frame, width=400)

	# find the barcodes in the frame and decode each of the barcodes
	barcodes = pyzbar.decode(frame)

    	# loop over the detected barcodes
	for barcode in barcodes:
		global text
		# extract the bounding box location of the barcode and draw
		# the bounding box surrounding the barcode on the image
		(x, y, w, h) = barcode.rect
		cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)

		# the barcode data is a bytes object so if we want to draw it
		# on our output image we need to convert it to a string first
		barcodeData = barcode.data.decode("utf-8")
		barcodeType = barcode.type

		# draw the barcode data and barcode type on the image
		text = "{} ({})".format(barcodeData, barcodeType)
		cv2.putText(frame, text, (x, y - 10),
			cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)

		# if the barcode text is currently not in our CSV file, write
		# the timestamp + barcode to disk and update the set

		# show the output frame'
	#print (text)
	


#threading is used to perform speaking and mouth gesture operate simultaneously.
# Otherwise mouth gesture will  occur and then the sound will come.
			   

	t1 = threading.Thread(target=speak) 
	t2 = threading.Thread(target=face) 
	  th
	    # starting thread 1 
	t1.start() 
	    # starting thread 2 
	t2.start() 
	  
	    # wait until thread 1 is completely executed 
	t1.join() 
	    # wait until thread 2 is completely executed 
	t2.join() 
  







	cv2.imshow("Barcode Scanner", frame)
	key = cv2.waitKey(1) & 0xFF
 
	# if the `q` key was pressed, break from the loop
	if key == ord("q"):
		break
		















# close the output CSV file do a bit of cleanup
print("[INFO] cleaning up...")
csv.close()
cv2.destroyAllWindows()
vs.stop()
