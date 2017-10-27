import math

#PASS FROM DEGREES TO RADIANS
def degreesToRad(degrees):

    return (degrees * math.pi) / 180

#PASS FROM RADIANS TO DEGREES
def radToDegrees(rad):

    return (rad * 180) / math.pi

#TAYLOR SERIE OF SIN
def sin(k, x):

    result = x

    for n in range(1, k):
        result += ((-1) ** n) / (math.factorial(2 * n + 1)) * (x ** (2 * n + 1))

    return result

#TAYLOR SERIE OF COS
def cos(k, x):

    result = 1.0

    for n in range(1, k):
        result += ((-1) ** n) / (math.factorial(2 * n)) * (x ** (2 * n))

    return result

print (sin(40, math.pi))
print (math.sin(math.pi))
