#largest of 3 nos
def input_no():
    a=int(input("enter the first number\n"))
    b=int(input("enter the second number\n"))
    c=int(input("enter the third number\n"))
    return a,b,c

def compare(a,b,c):
    if (a>=b) and (a>=c): 
        return a
    elif(b>=c):
        return b
    else:
        return c
def display(a,b,c,largest):
    print("%d is the largest among %d,%d and %d"%(largest,a,b,c))

def main():
    a,b,c=input_no()
    largest=compare(a,b,c)
    display(a,b,c,largest)
main()
