#largest of 3 nos
def input_no():
    a=int(input("enter a\n"))
    b=int(input("enter b\n"))
    c=int(input("enter c\n"))
    return a,b,c

def compare(a,b,c):
    if (a>=b) and (a>=c): 
        return a
    elif (b>=a) and (b>=c):
        return b
    else:
        return c

def main():
    a,b,c=input_no()
    largest=compare(a,b,c)
    print("largest of all three nos is %d"%(largest))
main()
