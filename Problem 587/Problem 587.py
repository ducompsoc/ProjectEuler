from math import *

def calculate_n(n):
    r = 5
    d = 2 * r

    #The section between the first circle and the first quadrant axes is
    #Area of the square surrounding the circle - area of circle then divide
    #it by 4.
    lSectionArea = (d ** 2 - r ** 2 * pi) / 4
    
    #Calculate the minimum coordinate where the line y = x / n intersects
    #the first circle
    minimumCoord = calculateIntersect(n)
    #Gives the middle of the rectangle surrounding all of the circles
    #e.g. n = 3, r = 5 gives (15, 5)
    maximumCoord = (n * r, r)
    
    #Calculates the length of the line between the minimum intersect with the
    #circle and the middle of the rectangle
    lineLength = ((maximumCoord[0] - minimumCoord[0]) ** 2 + (maximumCoord[1] - minimumCoord[1]) ** 2) ** 0.5

    #The length b is the distance between the centre of the rectangle and the
    #centre of the first circle
    #e.g. n = 3, r = 5 gives 5 * 2 = 10 which is the distance from (5, 5) to (15, 5)
    b = r * (n - 1)

    #Calculates the angle between length b and the radius connecting to the
    #first intersection
    angle = cosineAngleCalculation(lineLength, b, r)
    #Then find the other side by doing 180 - angle 
    iangle = 180 - angle

    #Calculate the area of the sector between the y-axis, the line y = r and
    #in the first circle
    sectorArea = (iangle / 360) * pi * (r ** 2)
    
    #Then calculate the area of the triangle which we found the angle for
    cosineArea = 0.5 * sin(radians(angle)) * r * (r * (n - 1))

    #Then calculate the whole triangle between the origin, (n * r, 0) and
    #(n * r, r).
    triangleArea = 0.5 * r * n * r
    
    #The L-section is split by the line y = x/n, calculate the area of the
    #upper L-section.
    remainingArea = triangleArea - cosineArea - sectorArea
    #Then the lower section of the L-section must just be the L-section -
    #the calculated area
    actualArea = lSectionArea - remainingArea
    
    #Now we can just calculate the percentage area
    percent = (actualArea / lSectionArea) * 100
    #print("When n =", n, "it covers", percent, "%")
    return percent

#Just the quadratic formula to solve the intersection of the circle with
#line y = x/n
def calculateIntersect(n):
    #equation = x^2 + y^2 - 10x - 10y + 25 = 0
    ysquares = 1 + (1 / n ** 2)
    subtracty = -10 + (-10 / n)

    negative = (-(subtracty) - ((subtracty ** 2) - (4 * ysquares * 25)) ** 0.5) / (2 * ysquares)

    return (negative, (1 / n * negative))

#Cosine rule to find the angle
def cosineAngleCalculation(a, b, c):
    return degrees(acos((b ** 2 + c ** 2 - a ** 2) / (2 * b * c)))

#Loop until we reach the target
def solve(target):
    n = 1
    lastResult = 1

    while lastResult > target:
        n += 1
        lastResult = calculate_n(n)

    return n

print(solve(0.1))
