import math
n = int(input("number of sides: "))
l = int(input("length of each sides: "))
print("Area: ",l**2*n/(4*math.tan(math.pi/n)))