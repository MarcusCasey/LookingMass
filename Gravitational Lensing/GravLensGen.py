# Gravitational lensing using the Thin screen (lens) approximation and Einstein Radius

from PIL import Image
import numpy as np
import math
import cv2
import sys

def gravLensGen(image):

    # Einstein Radius Equation
    # e = ( (4*G*M) / (c^2*D) )^(1/2) = radius
    #circle center coords
    center_coordinates = (548, 554)
    color = (255, 255, 255)
    col, row = image.size
    einstein_radius = int((20/255)*(row/2))
    b = 0.0
    thickness = 1 + einstein_radius

    # for 'outside' portion
    h1 = int((b + math.sqrt(b**2 + 4*(einstein_radius**2))) / 2)
    # for 'inside' portion
    h2 = int((b - math.sqrt(b**2 + 4*(einstein_radius**2))) / 2)

    # print(h1)
    # print(h2)

    newimage = cv2.imread(openpath)
    window_name = 'image'

    for i in range(row): #height row Y
        for j in range(col): #width col X
            # Equation of a Circle to find the radius
            distanceToCenter = math.sqrt((i - center_coordinates[1])**2 + (j - center_coordinates[0])**2)
            # if distanceToCenter >= einstein_radius and distanceToCenter <= thickness:
            #     # simply creates a white circle
            #     newimage[i][j] = (255, 255, 255)

            if distanceToCenter <= einstein_radius:
                newCoordinate = Cartesian_to_Polar(center_coordinates, einstein_radius, j, i, h1, row, col) #outside
                newCoordinate1 = Cartesian_to_Polar(center_coordinates, einstein_radius, j, i, h2, row, col) #inside 
                # print(newCoordinate)
                # print(distanceToCenter)
                x = newCoordinate[0]
                y = newCoordinate[1]
                a = newCoordinate1[0]
                b = newCoordinate1[1]
                # print(x, y, j, i, a, b) #(0,255,0)#
                # print(newimage[i][j])
                # print(newimage[y][x])
                newimage[y][x] = (0,255,0)#newimage[i][j]
                newimage[b][a] = (0,255,0)#newimage[i][j]
                # if i == 555 and j == 550:
                #     sys.exit()

                

    # red(0, )
    
    cv2.imwrite(savepath, newimage)

    newimage = cv2.circle(newimage, center_coordinates, einstein_radius, color, 1)
    cv2.imshow(window_name, newimage)
    k = cv2.waitKey(0)
    if k == 27: #esc key pressed
        cv2.destroyAllWindows()

    # #Distance between two points
    # h = math.sqrt((x2- x1)**2 + (y2 - y1)**2)
    # b = h - a
    # #For an image however h1 = h2 = e
    # h1 = (b + math.sqrt(b**2 + 4*math.e**2))/2
    # print(h1)

def Cartesian_to_Polar(centerCoord, centerRadius, currentX, currentY, h, row, col):
    X = centerCoord[0] - currentX
    Y = centerCoord[1] - currentY
    # print(X, Y, currentX, currentY, centerCoord)
    r = 0

    # theta = math.atan2(Y,X)%(2*math.pi)

    r = math.sqrt(X**2 + Y**2)

    maxradius =  math.sqrt(centerCoord[0]**2 + centerCoord[1]**2)/2
    rscale = centerCoord[0] / maxradius
    tscale = centerCoord[1] / (2*math.pi)
    dx = currentX - centerCoord[0]/2
    dy = currentY - centerCoord[1]/2
    t = math.atan2(dy,dx)%(2*math.pi)
    r = math.sqrt(dx**2 + dy**2)
    
    # rnew = h - ((centerRadius**2) / h)
    # print(r, centerRadius, "rnew:", rnew)
    # print(r, theta)
    return Polar_to_Cartesian(centerCoord, centerRadius, h, currentX, currentY, r, rscale, tscale, t)

def Polar_to_Cartesian(centerCoord, centerRadius, theta, currentX, currentY, r, rscale, tscale, t):
    X = (centerRadius * math.cos(theta)) 
    Y = (centerRadius * math.sin(theta))
    
    # print(X, Y, centerRadius, math.sin(theta), theta)
    newCoord = ( int(X + currentX), int(currentY + Y) ) 
    # print(newCoord)
    return newCoord


    

openpath = "./data input/hubbledeepspace.jpg"
savepath = "./data output/hubbledeepspace.png"
testImage = Image.open(openpath)
# testImage1.save(newpath)
# testImage2 = Image.open(newpath)
gravLensGen(testImage)