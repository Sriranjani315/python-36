# volume of the tromboloid and radius
import math
def input_no():
    l = float(input("enter the length\n"))
    b = float(input("enter the breadth\n"))
    h = float(input("enter the height\n"))
    return l,b,h
def volume(l,b,h):    
    k=(l*l)+(b*b)+(h*h)
    volume=((b*b)*(h*h))/(math.sqrt(k))
    
    return volume
def radius(l,b,h):
    v=volume(l,b,h)
    radius= pow((3*v/(4*(math.pi))),1/3)
    return radius
    
def display(volume,radius):    
    print("volume of tromboloid=%0.3f" %(volume))
    print("radius of the sphere=%0.3f"%(radius))

def main():
    l,b,h=input_no()
    volume_tromboloid=volume(l,b,h)
    Radius=radius(l,b,h)
    display(volume_tromboloid,Radius)

main()
