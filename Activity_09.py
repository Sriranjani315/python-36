#volume of tromboloid and radius of sphere
l = float(input("enter the length\n"))
b = float(input("enter the breadth\n"))
h = float(input("enter the height\n"))
k=(l*l)+(b*b)+(h*h)
import math
volume=((b*b)*(h*h))/(math.sqrt(k))
print("volume of tromboloid=%0.3f" %(volume))
radius= pow((3*float(volume)/(4*3.142)),1/3)
print("radius of the sphere=%0.3f"%(radius))
