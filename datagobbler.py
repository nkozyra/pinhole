import argparse
import cv2
import numpy as np
import sys
from tqdm import tqdm

# green chromakey
chromaKey = np.array([0,255,0])
blocks = 100
maxFrames = 2
destination = "images/"


dataFrames = np.array((int(blocks),int(blocks)))
def process(f):
  c = cv2.VideoCapture(f)
  frame = 0
  totalBlocks = int(blocks)
  # if c.isOpened():
  while(True):
    t,data = c.read()

    height = len(data)
    width = len(data[0])
    img = np.zeros((height,width,3), np.uint8)
    hPixels = width / int(blocks)
    vPixels = height / int(blocks)
    # print vBlocks,hBlocks
    # imgCells = (blockPx) * (rows * cols)

    # vertical blocks
    for i in range(totalBlocks):
      yPos = i * vPixels
      yMax = yPos + vPixels
      for j in tqdm(range(totalBlocks)):
        xPos = j * hPixels
        xMax = xPos +hPixels
        # print yPos,yMax,xPos,xMax
        cellCount = 0
        rTot = 0
        gTot = 0
        bTot = 0
        for ii in range(yPos,yMax):
          for jj in range(xPos,xMax):
            cellCount += 1
            rTot += data[ii][jj][2]
            gTot += data[ii][jj][1]
            bTot += data[ii][jj][0]
        rAvg = rTot / cellCount
        gAvg = gTot / cellCount
        bAvg = bTot / cellCount

        cv2.rectangle(img, (xPos,yPos), (xPos+hPixels,yPos+vPixels), (bAvg,gAvg,rAvg), -1)
    cv2.imwrite(destination+str(frame)+'_image.png',img)

    frame += 1
    if frame > maxFrames:
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