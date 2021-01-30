import matplotlib.pyplot as plt
import numpy as np

def _linearInterpolation(x0, y0, x1, y1, x):
    return (y0 * (x1 - x) + y1 * (x - x0)) / (x1 - x0)

def ageYoungMembership(age):
    if (age < 30):
        return 1
    elif (age < 50):
        return _linearInterpolation(30, 1, 50, 0.75, age)
    elif (age < 65):
        return _linearInterpolation(50, 0.75, 65, 0.5, age)
    elif (age < 75):
        return _linearInterpolation(65, 0.5, 75, 0.25, age)
    elif (age < 85):
        return _linearInterpolation(75, 0.25, 85, 0, age)
    else:
        return 0
    
def lifeExpectancyLowMembership(lifeExpectancy):
    if (lifeExpectancy < 2.5):
        return 1
    elif (lifeExpectancy < 7.5):
        return _linearInterpolation(2.5, 1, 7.5, 2/3, lifeExpectancy)
    elif (lifeExpectancy < 15):
        return _linearInterpolation(7.5, 2/3, 15, 0, lifeExpectancy)
    else:
        return 0

def maxDiameterLargeMembership(maxDiameter):
    if (maxDiameter > 37.0):
        return 1
    elif (maxDiameter > 19.0):
        return _linearInterpolation(37.0, 1, 19.0, 0.75, maxDiameter)
    elif (maxDiameter > 10.0):
        return _linearInterpolation(19.0, 0.75, 10.0, 0.5, maxDiameter)
    elif (maxDiameter > 5.5):
        return _linearInterpolation(10.0, 0.5, 5.5, 0.25, maxDiameter)
    elif (maxDiameter > 2.0):
        return _linearInterpolation(5.5, 0.25, 2.0, 0, maxDiameter)
    else:
        return 0

def ageRiskHighMembership(age):
    if (age > 85):
        return 1
    elif (age > 75):
        return _linearInterpolation(85, 1, 75, 0.8, age)
    elif (age > 65):
        return _linearInterpolation(75, 0.8, 65, 0.6, age)
    elif (age > 50):
        return _linearInterpolation(65, 0.6, 50, 0.2, age)
    elif (age > 30):
        return _linearInterpolation(50, 0.2, 30, 0, age)
    else:
        return 0

def sizeRiskHighMembership(maxDiameter):
    if (maxDiameter > 24.0):
        return 1
    elif (maxDiameter > 15.0):
        return _linearInterpolation(24.0, 1, 15.0, 0.6, maxDiameter)
    elif (maxDiameter > 8.0):
        return _linearInterpolation(15.0, 0.6, 8.0, 0.2, maxDiameter)
    elif (maxDiameter > 3.0):
        return _linearInterpolation(8.0, 0.2, 3.0, 0, maxDiameter)
    else:
        return 0
