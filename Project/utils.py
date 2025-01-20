import numpy as np
import cv2



def get_limit(color):
  c = np.uint8([[color]])
  hscv = cv2.cvtColor(c, cv2.COLOR_BGR2HSV)
  lower_limit = hscv[0][0][0] - 10,100,100
  high_limit = hscv[0][0][0] + 10,255,255

  lower_limit = np.array(lower_limit,dtype=np.uint8)
  high_limit = np.array(high_limit,dtype=np.uint8)

  return (lower_limit,high_limit)