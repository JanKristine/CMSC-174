import cv2
import numpy as np

# 1. Using numpy arrays, create a 800x800 black and white image having a pattern of alternating 
# white and black horizontal stripes. The width of the stripe is 100

# 2. Same as 1 but this time create vertical stripes

# 3. Challenge: Same as 1 but create a chessboard pattern

# 4. Challenge+: Do 1 to 3 but stipes are in different colors, choose your own colors.

print("1. Using numpy arrays, create a 800x800 black and white image having a pattern of alternating white and black horizontal stripes. The width of the stripe is 100.")

horizontalArray = np.zeros((800,800),np.uint8)

for i in range(len(horizontalArray)): # row
    if ((0<=i<=99) or (200<=i<=299) or (400<=i<=499) or (600<=i<=699)):    
        for j in range(len(horizontalArray)): # column
            horizontalArray[i][j] = 255
cv2.imwrite('Horizontal.png', horizontalArray)
cv2.imshow('Horizontal.png', horizontalArray)


print("2. Same as 1 but this time create vertical stripes")

verticalArray = np.zeros((800,800),np.uint8)

for i in range(len(verticalArray)): # row    
    for j in range(len(verticalArray)): # column
            if ((0<=j<=99) or (200<=j<=299) or (400<=j<=499) or (600<=j<=699)):
                verticalArray[i][j] = 255
cv2.imwrite('Vertical.png', verticalArray)
cv2.imshow('Vertical.png', verticalArray)


print("3. Challenge: Same as 1 but create a chessboard pattern")

chessArray = np.zeros((800,800),np.uint8)

for i in range(len(chessArray)): # row    
    if ((0<=i<=99) or (200<=i<=299) or (400<=i<=499) or (600<=i<=699)):
        for j in range(len(chessArray)): # column
                if ((0<=j<=99) or (200<=j<=299) or (400<=j<=499) or (600<=j<=699)):
                    chessArray[i][j] = 255
    if ((100<=i<=199) or (300<=i<=399) or (500<=i<=599) or (700<=i<=799)):
         for j in range(len(chessArray)): # column
                if ((100<=j<=199) or (300<=j<=399) or (500<=j<=599) or (700<=j<=799)):
                    chessArray[i][j] = 255
cv2.imwrite('Chess.png', chessArray)
cv2.imshow('Chess.png', chessArray)

print("4. Challenge+: Do 1 to 3 but stipes are in different colors, choose your own colors.")

diffHorizontalArr = np.zeros((800,800,3),np.uint8)

for i in range(len(diffHorizontalArr)): # row
    if ((0<=i<=99) or (200<=i<=299) or (400<=i<=499) or (600<=i<=699)):    
        for j in range(len(diffHorizontalArr)): # column
            diffHorizontalArr[i][j] = 203,192,255     # BGR
    else:
        for j in range(len(diffHorizontalArr)): # column
            diffHorizontalArr[i][j] = 204,50,153
cv2.imwrite('diffHorizontal.png', diffHorizontalArr)
cv2.imshow('diffHorizontal.png', diffHorizontalArr)

diffVerticalArr = np.zeros((800,800,3),np.uint8)

for i in range(len(diffVerticalArr)): # row   
        for j in range(len(diffVerticalArr)): # column
            if ((0<=j<=99) or (200<=j<=299) or (400<=j<=499) or (600<=j<=699)):
                diffVerticalArr[i][j] = 34,139,34     # BGR
            else:
                diffVerticalArr[i][j] = 143,188,143
cv2.imwrite('diffVertical.png', diffVerticalArr)
cv2.imshow('diffVertical.png', diffVerticalArr)

diffChessArr = np.zeros((800,800,3),np.uint8)

for i in range(len(diffChessArr)): # row    
    if ((0<=i<=99) or (200<=i<=299) or (400<=i<=499) or (600<=i<=699)):
        for j in range(len(diffChessArr)): # column
                if ((0<=j<=99) or (200<=j<=299) or (400<=j<=499) or (600<=j<=699)):
                    diffChessArr[i][j] = 237,149,100
                else:
                     diffChessArr[i][j] = 60,20,220
    if ((100<=i<=199) or (300<=i<=399) or (500<=i<=599) or (700<=i<=799)):
         for j in range(len(diffChessArr)): # column
                if ((100<=j<=199) or (300<=j<=399) or (500<=j<=599) or (700<=j<=799)):
                    diffChessArr[i][j] = 237,149,100
                else:
                     diffChessArr[i][j] = 60,20,220
cv2.imwrite('diffChess.png', diffChessArr)
cv2.imshow('diffChess.png', diffChessArr)

cv2.waitKey()
cv2.destroyAllWindows()
