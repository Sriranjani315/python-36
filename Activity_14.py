#prime or not
def input_no():
    num=int(input("Enter the number:"))
    return num
def prime(n):
    flag=0
    for i in range(2,int(math.sqrt(n)+1)):
        if(n%i==0):
            flag=1
            break
        else:
            continue
    return flag
def result(flag):
    if(flag==0):
        print("It is a prime number")
    else:
        print("It is not a prime number")
def main():
    num=input_no()
    flag=prime(num)
    result(flag)
main()
            
                      
