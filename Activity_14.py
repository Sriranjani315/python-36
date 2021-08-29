#prime or not
def input_no():
    
    num=int(input("enter the number\n"))
    return num

def prime(n):
    prime_flag=0
    if(n>1):
        import math
        for i in range(2,int(math.sqrt(n))+1):
            if(n%i==0):
                prime_flag=1
                break
            return prime_flag
def display(prime_flag):
    if(prime_flag==0):
        print("number is prime")
    else:
            print("number is not prime")
def main():
    num=input_no()
    prime_no=prime(num)
    display(prime_no)
main()
            
                      
