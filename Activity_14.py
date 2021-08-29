#prime or not
import math

def input_number():
    num = int(input("Enter the number\n "))
    return num
def prime(n):
   prime_flag = 0
   if(n>1):
       for i in range(2,int(math.sqrt(n))+1):
            if(n%i==0):
                prime_flag=1
                break
            return prime_flag
            
def display(prime_flag):
    if(prime_flag==0):
        print("it is prime")
    else:
        print("it is not prime")

def main():
    num = input_number()
    prime_number = prime(num)
    display(prime_number)
main()  
            
                      
