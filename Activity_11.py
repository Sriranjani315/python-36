#addition of two nos using 4 functions
def input_no():
    num1=int(input("enter the first number\n"))
    num2=int(input("enter the second number\n"))
    return num1,num2

def add(a,b):
    return a+b

def display(a,b,c):
    print(f"{a}+{b}={c}")

def main():
    num1,num2=input_no()
    answer=add(num1,num2)
    display(num1,num2,answer)
main()
