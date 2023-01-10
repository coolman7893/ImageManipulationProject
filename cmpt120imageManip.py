#---------------------------------------------------------
# CMPT 120 Yet Another Image Processer
# Starter code for cmpt120imageManip.py
# Author: Sanjit Mann
# Date: Dec. 3rd, 2020
# Description: Contains all the functions used in our code
#---------------------------------------------------------

import cmpt120imageProj
import numpy

# DEFINE BASIC FUNCTIONS

# Define invert function
def invert(pixels):
    # Get width and height
    x1 = len(pixels)
    y1 = len(pixels[0])

    # Go through RGB values for each pixel and subtract them
    # from 255 to get inverted colour
    for x in range(x1): 
        for y in range(y1): 
            r = pixels[x][y][0] 
            g = pixels[x][y][1] 
            b = pixels[x][y][2] 
            pixels[x][y] = [255 - r, 255 - g, 255 - b]
    return pixels

# Define flip function
def flipHorizontal(pixels):
    # Get height and width
    x1 = len(pixels)
    y1 = len(pixels[0])

    # Use numpy to get shape of flipped image
    SHAPE = numpy.shape(pixels)
    SHAPE1 = numpy.zeros((SHAPE))

    # Go through each pixel and flip it with the corresponding
    # horizontal value
    for x in range(x1):
        for y in range(y1):
            SHAPE1[x1 - x - 1][y] = pixels[x][y]
            pixels[x][y] = SHAPE1[x][y]
    return pixels

# Define vertical function
def flipVertical(pixels):
    # Get width and height
    x1 = len(pixels)
    y1 = len(pixels[0])

    # Use numpy to get the shape of the flipped image
    SHAPE = numpy.shape(pixels)
    SHAPE1 = numpy.zeros((SHAPE))

    # Go through each pixel and flip it with the corresponding
    # vertical value
    for x in range(x1):
      for y in range(y1):
        SHAPE1[x][y1- y- 1] = pixels[x][y]
        pixels[x][y] = SHAPE1[x][y]
    return pixels

# DEFINE INTERMEDIATE FUNCTIONS

# Define removeRed function
def removeRed(pixels):
    # Get height and width
    x1 = len(pixels)
    y1 = len(pixels[0])

    # Go through RGB values and change the red value to 0
    for x in range(x1):
      for y in range(y1):
        g = pixels[x][y][1]
        b = pixels[x][y][2]
        pixels[x][y] = [0, g, b]
    return pixels

# Define removeGreen function
def removeGreen(pixels):
    # Get height and width
    x1 = len(pixels)
    y1 = len(pixels[0])

    # Go through RGB values and change the green value to 0
    for x in range(x1):
      for y in range(y1):
        r = pixels[x][y][0]
        b = pixels[x][y][2]
        pixels[x][y] = [r, 0, b]
    return pixels

# Define removeBlue function
def removeBlue(pixels):
    # Get height and width
    x1 = len(pixels)
    y1 = len(pixels[0])

    # Go through RGB values and change the blue value to 0
    for x in range(x1):
      for y in range(y1):
        r = pixels[x][y][0]
        g = pixels[x][y][1]
        pixels[x][y] = [r, g, 0]
    return pixels

# Define grayScale function
def grayScale(pixels):
    # Get width and height
    x1 = len(pixels)
    y1 = len(pixels[0])

    # Go through each pixel and calculate the grayscale value
    for x in range(x1):
      for y in range(y1):
        r = pixels[x][y][0]
        g = pixels[x][y][1]
        b = pixels[x][y][2]
        nRGB = (r+g+b)/3
        # Assign the new values to the pixels in the image
        pixels[x][y] = [nRGB, nRGB, nRGB]
    return pixels

# Define sepiaFilter function
def sepiaFilter(pixels):
    # Get width and height
    x1 = len(pixels)
    y1 = len(pixels[0])

    # Go through each pixel and apply the sepia filter
    # to the RGB values
    # If the value is over 255, change it to 255
    for x in range(x1):
      for y in range(y1):
        r = pixels[x][y][0]
        g = pixels[x][y][1]
        b = pixels[x][y][2]
        SRed = int(r*0.393) + int(g*0.769) + int(b * 0.189)
        if SRed > 255:
          SRed = 255
        SGreen = int(r*0.349) + int(g*0.686) + int(b*0.168)
        if SGreen > 255:
          SGreen = 255
        SBlue = int(r*0.272) + int(g*0.534) + int(b*0.131)
        if SBlue > 255:
          SBlue = 255
        # Assign the new values to the pixels in the image
        pixels[x][y] = [SRed, SGreen, SBlue]
    return pixels

# Define lowerBrightness function
def lowerBrightness(pixels):
    # Get the width and height
    x1 = len(pixels)
    y1 = len(pixels[0])
    
    # Get the RGB values and add 10 to each of them
    # If the subtracted value ends up below 0, change it to 0
    for x in range(x1):
      for y in range(y1):
        r = pixels[x][y][0]
        g = pixels[x][y][1]
        b = pixels[x][y][2]
        nR = r - 10
        if nR < 0:
          nR = 0
        nG = g - 10
        if nG < 0:
          nG = 0
        nB = b - 10
        if nB < 0:
          nB = 0
        
        # Assign the new values to the pixels in the image
        pixels[x][y] = [nR, nG, nB]
    return pixels

# Define highBrightness function
def highBrightness(pixels):
    # Get the width and height
    x1 = len(pixels)
    y1 = len(pixels[0])

    # Get the RGB values and add 10 to each of them
    # If the added value ends up over 255, change it to 255
    for x in range(x1):
      for y in range(y1):
        r = pixels[x][y][0]                              
        g = pixels[x][y][1]                              
        b = pixels[x][y][2]                              
        nR = r + 10                              
        if nR > 255:                              
          nR = 255                              
        nG = g + 10                              
        if nG > 255:                              
          nG = 255                             
        nB = b + 10                              
        if nB > 255:                              
          nB = 255                      

        # Assign the new values to the pixels in the image         
        pixels[x][y] = [nR, nG, nB]
    return pixels

# DEFINE ADVANCED FUNCTIONS

# Define rotateLeft funtion
def rotateLeft(pixels):
    # Get the height and width of the image
    x1 = len(pixels)
    y1 = len(pixels[0])

    # Create a blank image and flip the x1 and y1 values
    NI = cmpt120imageProj.createBlackImage(y1, x1)
    SHAPE = numpy.shape(NI)
    SHAPE1 = numpy.zeros((SHAPE))
    
    # Go through the pixels and rotate the image
    for x in range(x1):
      for y in range(y1):
        SHAPE1[y1 - y - 1][x1 - x - 1] = pixels[x1 - x - 1][y]
    cmpt120imageProj.saveImage(SHAPE1, "rotatedLeft.jpg")
    return SHAPE1
  
# Define rotateRight function
def rotateRight(pixels):
    # Get the height and width
    x1 = len(pixels)
    y1 = len(pixels[0])

    # Create a blank image to flip x1 and y1 values
    NI = cmpt120imageProj.createBlackImage(y1, x1)
    SHAPE = numpy.shape(NI)
    SHAPE1 = numpy.zeros((SHAPE))
    
    # Go through each pixel and rotate the image
    for x in range(x1):
      for y in range(y1):
        SHAPE1[y1 - y - 1][x1 - x - 1] = pixels[x][y1 - y -1]
    cmpt120imageProj.saveImage(SHAPE1, "rotatedRight.jpg")
    return SHAPE1

# Define binarize function
def binarize(pixels):
    # Use the grayscale function to get the grayscaled image
    grayScale(pixels)

    # Get the height and width
    x1 = len(pixels)
    y1 = len(pixels[0])

    # Calculate initial threshold
    thresh1LessImg = cmpt120imageProj.createBlackImage(x1,y1)
    thresh1MoreImg = cmpt120imageProj.createBlackImage(x1,y1)
    lessAVG = 0
    moreAVG = 0
    Sum = 0
    
    for a in range(x1):
      for b in range(y1):
        pix = int(pixels[a][b][0])
        Sum += pix
    thresh1 = int(int(Sum)/(x1*y1))

    for c in range(x1):
      for d in range(y1):
        if int(pixels[c][d][0]) <= thresh1:
          thresh1LessImg[c][d] = pixels[c][d]
        else:
          thresh1MoreImg[c][d] = pixels[c][d]

    for e in range(x1):
      for f in range(y1):
        lessAVG += int(thresh1LessImg[e][f][0])
        moreAVG += int(thresh1MoreImg[e][f][0])

    # Get the new threshold by averaging the two averages
    lessAVG1 = int(lessAVG/(x1*y1))
    moreAVG1 = int(moreAVG/(x1*y1))
    threshnew = int((lessAVG1 + moreAVG1)/2)
    
    # Create the background and foreground
    if int(thresh1 - threshnew) <= 255:
      threshreal = threshnew
    else:
      thresh1LessImg 
      thresh1MoreImg
      for g in range(x1):
        for h in range(y1):
          if int(pixels[g][h][0]) <= thresh1:
            thresh1LessImg[g][h] = pixels[g][h]
          else:
            thresh1MoreImg[g][h] = pixels[g][h]

      # Calculate average of the pixel colour channel for the background and foreground
      for i in range(x1):
        for j in range(y1):
          lessAVG += int(thresh1LessImg[i][j][0])
          moreAVG += int(thresh1MoreImg[i][j][0])
      lessAVG1 = int(lessAVG/(x1*y1))
      moreAVG1 = int(moreAVG/(x1*y1))
      
      # Calculate the real threshold
      threshreal = int(lessAVG1 + moreAVG1/2)

    # Go through the pixels again and convert to binary using the new threshold
    for k in range(x1):
      for l in range(y1):
        if int(pixels[k][l][0]) <= threshreal:
          pixels[k][l] = [0,0,0]
        else:
          pixels[k][l] = [255,255,255]
    return pixels

# Define pixelate funtion
def pixelate(pixels):
  # Get the length and width
  x1 = len(pixels)
  x2 = x1 - x1%4
  y1 = len(pixels[0])
  y2 = y1 - y1%4

  # Average surrounding pixels and pixelate the image
  for x in range(0,x2,4):
    for y in range(0,y2,4):
      r = 0
      g = 0
      b = 0
      for l in range(x,x+4):
        for q in range(y,y+4):
          r += pixels[l][q][0]
          g += pixels[l][q][1]
          b += pixels[l][q][2]
      for z in range(x,x+4):
        for m in range(y,y+4):
          pixels[z][m] = [r/16,g/16,b/16]