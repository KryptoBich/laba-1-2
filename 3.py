import math
s1 = int(input("Enter the area of circle:"))
s2 = int(input("Enter the area of square:"))
if s1 >= (2 * math.pi * s2):
    print("Square fit the circle")
else:
    print("Square doesn't fit the circle")
