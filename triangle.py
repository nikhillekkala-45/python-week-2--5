import math
a = float(input("Enter side a of the triangle: "))
b = float(input("Enter side b of the triangle: "))
c = float(input("Enter side c of the triangle: "))
s = (a + b + c) / 2
area = math.sqrt(s * (s - a) * (s - b) * (s - c))
print("The area of the triangleis:",area)

