
def _linearInterpolation(x0, y0, x1, y1, x):
    return (y0 * (x1 - x) + y1 * (x - x0)) / (x1 - x0)

# Fuzzy set "Young Age"
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

# Fuzzy set "Low life expectancy"
def lifeExpectancyLowMembership(lifeExp):
    if (lifeExp < 2.5):
        return 1
    elif (lifeExp < 7.5):
        return _linearInterpolation(2.5, 1, 7.5, 2/3, lifeExp)
    elif (lifeExp < 15):
        return _linearInterpolation(7.5, 2/3, 15, 0, lifeExp)
    else:
        return 0

# Fuzzy set "Large maximum diameter"
def maxDiameterLargeMembership(maxDia):
    if (maxDia > 37.0):
        return 1
    elif (maxDia > 19.0):
        return _linearInterpolation(37.0, 1, 19.0, 0.75, maxDia)
    elif (maxDia > 10.0):
        return _linearInterpolation(19.0, 0.75, 10.0, 0.5, maxDia)
    elif (maxDia > 5.5):
        return _linearInterpolation(10.0, 0.5, 5.5, 0.25, maxDia)
    elif (maxDia > 2.0):
        return _linearInterpolation(5.5, 0.25, 2.0, 0, maxDia)
    else:
        return 0

# Fuzzy set "High age-related risk"
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

# Fuzzy set "High size-related risk"
def sizeRiskHighMembership(maxDia):
    if (maxDia > 24.0):
        return 1
    elif (maxDia > 15.0):
        return _linearInterpolation(24.0, 1, 15.0, 0.6, maxDia)
    elif (maxDia > 8.0):
        return _linearInterpolation(15.0, 0.6, 8.0, 0.2, maxDia)
    elif (maxDia > 3.0):
        return _linearInterpolation(8.0, 0.2, 3.0, 0, maxDia)
    else:
        return 0