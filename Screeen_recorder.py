import cv2
import numpy as np
import os
import pyautogui
import os.path
from os import path

def record():
    
    file_name=input("Give a name to your output file: ")
    print("Started recording...")
    print("\npress Ctrl + c to stop")
    output = file_name+".avi"
    snap = pyautogui.screenshot()
    snaparray = cv2.cvtColor(np.array(snap), cv2.COLOR_RGB2BGR)
    # print(snap)
    # get info from img
    height, width, channels = snaparray.shape
    # Define the codec and create VideoWriter object
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter(output, fourcc, 11.0, (width, height))

    while(True):
         try:
          snap = pyautogui.screenshot()
          screendata = cv2.cvtColor(np.array(snap), cv2.COLOR_RGB2BGR)
          out.write(screendata)
        #   StopIteration(0.5)
         except KeyboardInterrupt:
          break

    out.release()   
    cv2.destroyAllWindows()
    print('file saved') 


ask=input("Hi!\nPress'S' to start recording... ")
if ask==('s' or 'S'):

    record()
