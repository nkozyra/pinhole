import argparse
import cv2
import numpy as nd
import sys


# green chromakey
chromaKey = nd.array([0,255,0])
blocks = 100
maxFrames = 20

def process(f):
  c = cv2.VideoCapture(f)
  i = 0
  # if c.isOpened():
  while(True):
    t,data = c.read()
    height = len(data)
    width = len(data[0])
    hBlocks = width / int(blocks)
    vBlocks = height / int(blocks)
    print vBlocks,hBlocks
    for ii in range(height):
      pass
    i += 1
    if i > maxFrames:
      break

parser = argparse.ArgumentParser(description='f')
parser.add_argument('strings', metavar='f', type=str, nargs='+',
                   help='Filename to process')
parser.add_argument('integers', metavar='b', type=int, nargs='+',
                   help='# of blocks to create')
args = parser.parse_args()
filename = sys.argv[1]
blocks = sys.argv[2]
process(filename)