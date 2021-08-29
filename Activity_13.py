#odd nos
def input_no():
    a=int(input("enter the start number\n"))
    b=int(input("enter the stop number\n"))
    return a,b
def oddnos(a,b):
    for num in range(a,b):
        if(num%2!=0):
            print(num)
def main():
    a,b=input_no()
    oddnos(a,b)
main()
    
