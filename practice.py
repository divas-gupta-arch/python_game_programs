## anylise your age group

# age=int(input("enter your age:"))
# if (age>=0 and age<18):
#     print("you are minor")
# elif (age>=18 and age<60):
#     print("you are adult")
# elif age>=60:
#     print("you are a senior citizen")
# else:
#     print("invalid input please give the valid input")

##check which number is greater

# num1=float(input("enter a frist no. :"))
# num2=float(input("enter a second no. :"))
# if num1>num2:
#     print(f"frist no {num1} is grater ")
# elif num2>num1:
#     print(f"second no {num2} is grater")
# elif num1==num1:
#     print(f"frist and sencond no. are equal {num1}={num2}")
# else:
#     print("try again invalid input12")

## gives gender based on input

# gender=input("entere your gender,\n for male(m) and for female(f):")
# if gender=="m"or gender=="M":
#     print("good morning sir")
# elif gender=="f"or gender=="F":
#     print("good morninig ma'am")
# else:
#     print("invalid input")

##checking year is leap year or not

# year=int(input("enter year:"))
# if year%100==0 and year%400==0:
#     print("leap year")
# elif year%100 !=0 and year%4==0:
#     print("leap year")
# else:
#     print("not a leap year")

##indexing of string

# str=input("enter your name:")
# for i in range(len(str)):
#     print(str[i])

##break and continue statment

# for i in range(1,11):
#     if i==4:
#         continue
#     if i==23:
#         break
#     print(i)
# else:
#     print("thanks")

##print hello n times
# n=int(input("tell your no. -:"))

## natural no. upto n
# num=int(input("enter a no. -:"))
# for i in range(1,num+1):
#     print(i)

## revese the number
# num=int(input("enter a num-:"))
# for i in range(num,0,-1):
#     print(i)

##table of num
# num=int(input("enter a num-:"))
# for i in range(1,11):
#     print(f"{num}x{i}={num*i}")

##sum of n natural numbers
# a=0 #for sum/sub we use value of variable 0 
# sum=int(input("till where you want sum-:"))
# for i in range(1,sum+1):
#     a=a+i
# print(a)

##factoral 
# f=1 #for div/mul we put value of variable 1
# num=int(*input("factoral-:"))
# for i in range(1,num+1):
#     f=f*i
# print(f)

##print the sum of odd and eve number separately
# oddsum=0
# evesum=0
# n=int(input("enter a num-:"))
# for i in range(1,n+1):
#     if(i%2==0):
#         evesum=evesum +i
#     else:
#         oddsum= oddsum+i
# print(f"oddsum={oddsum}")
# print(f"evesum={evesum}")

##factors of num
# n=int(input("enter a num-:"))
# for i in range(1,n+1):
#     if(n%i==0):
#         print(i)

## check no is perfect or not(sum of factors== number itself)  
# per=0      
# n=int(input("enter a no. -:"))
# for i in range(1,n):
#     if n%i==0:
#         per= per+i
# if per==n:        
#     print(f"perfect no. is{per}")
# else:
#     print("not a perfect number")    

# ##check no is prime or not
# n=int(input("enter a no. -:"))
# count=0
# for i in range(1,n+1):
#     if n%i==0 :
#         count=count+1
# if count==2:
#     print("prime no.")
# else:
#     print("composit no.")        
    
##revarsing of str without using bulitin func
# a="python"
# rev=""
# for i in range(len(a)-1,-1,-1):
#     rev=rev +(a[i])
# print(rev)

##check is palendrom
# a=input("enter a str:")
# pal=""
# for i in range(len(a)-1,-1,-1):
#     pal=pal +(a[i])
# if pal==a:
#     print("palindrome")
# else:
    # print("not a palindrome")

##count a specal char,letters &digits in str(by builtin func)
# a="fyrsrhv565698-0@#$%^&*()"
# let=0
# dig=0
# chr=0
# for i in a:
#     if i.isdigit():
#         dig +=1
#     elif i.isalpha():
#         let +=1
#     else:
#         chr +=1
# print(f" letter :{let},digits :{dig},characters:{chr}")

##through asci/unicode
# let=0
# dig=0
# chr=0
# for i in a:
#     if ord(i)>=48 and ord(i)<=90:
#         dig +=1
#     elif (ord(i)>=65 and ord(i)<=90) or (ord(i)>=97 and ord(i)<=122):
#         let +=1
#     else:
#         chr +=1
# print(f" letter :{let},digits :{dig},characters:{chr}")

## while loop
# a=1
# while a<=20:
#     print(a)
#     a+=1

##print every letters of  digit in rev. ord in next line
# a=int(input("enter a number:"))
# while a>0:
#     print(a%10)
#     a=a//10
    

## reverse the digit 
# a=int(input("enter a number:"))
# rev=0
# while a>0:
#     rev=rev*10 +(a%10)
#     a=a//10
# print(rev)   

# a=int(input("enert a vlue:"))
# rev=0
# b=a
# while a>0:
#     rev=rev*10 +a%10
#     a=a//10
##if we want to compare in while loop
## we needed to store the value of input into another variable
##b/z a become 0 in converson into rev ord
# if b==rev:
#     print("palindrome")
# else:
#     print("not palindrome")

#functions
# def add(a,b):
#     print(a+b)
# add(22,9)

##func for palindrome
# def pal(a):
#     b=a
#     rev=0
#     while a>0:
#         rev=10*rev +a%10
#         a=a//10
#     if b==rev:
#         print("palindrome")    
#     else:
#         print("not a palindrome")
# b=int(input("enter a num-:"))
# pal(b)
