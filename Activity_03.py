str1 = input("enter the 1st string:\n")
str2 = input("enter the 2nd string:\n")
concatenated_string =str1+str2
print("concatenated string:",concatenated_string)
answer=concatenated_string*5
print(answer)

challenge
str1 = input("enter the 1st string:\n")
str2 = input("enter the 2nd string:\n")
concatenated_string =str1+" "+str2
print("concatenated string:",concatenated_string)
 
print((concatenated_string+"\n")*5)

other method
str1="good"
str2="afternoon"
concatenated_string= str1+" "+str2
print("concatenated string:",concatenated_string)
str3="{} {}".format(str1,str2)
print((str3 +"\n")*5)
