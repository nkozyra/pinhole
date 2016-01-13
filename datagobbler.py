import argparse
import cv2
import numpy as nd
import sys


# green chromakey
chromaKey = nd.array([0,255,0])

def process(f):
  c = cv2.VideoCapture(f)
  i = 0
  # if c.isOpened():
  while(True):
    data = c.read()
    print data
    # for i in range(len)
    i += 1
    if i > 20:
      break

parser = argparse.ArgumentParser(description='f')
parser.add_argument('strings', metavar='f', type=str, nargs='+',
                   help='Filename to process')
parser.add_argument('integers', metavar='b', type=int, nargs='+',
                   help='# of blocks to create')
args = parser.parse_args()
filename = sys.argv[1]
process(filename)