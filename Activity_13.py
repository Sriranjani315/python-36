#odd nos
def input_no():
    a=int(input("enter the start number\n"))
    b=int(input("enter the stop number\n"))
    return a,b
def oddnos(a,b):
    for num in range(a,b+1):
        if(num%2!=0):
            return num
def display(odd_nos):
    print("odd nos from start to stop is:",odd_nos)
def main():
    a,b=input_no()
    odd_nos=oddnos(a,b)
    display(odd_nos)
main()
