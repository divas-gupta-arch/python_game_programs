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

###indexing of string

# str=input("enter your name:")
# for i in range(len(str)):
#     print(str[i])

###break and continue statment

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

### while loop
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

###functions
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

###data structueres
## list
# fruits=["apple","mango","grapes"]
# fruits.pop()
# print(fruits)

##tarversing on list(loop on list)
##by value

# a=[10,20,30,40,50,"hello"]
# for i in a:
#     print(i)

##by index
# for i in range(0,len(a)):
    # print(f"{i} : {a[i]}")

## ques
# l=[ 3,-1, 4,-5, 9]
# pos=[]
# neg=[]
# for i in l:
#     if i>=0:
#             pos.append(i)
#     else:
#             neg.append(i)
# print(f"positive elements are:{pos}")
# print(f"negative elements are:{neg}")  

##avg
# l=[10,20,30,40]
# sum=0
# for i in l:
#     sum=sum+i
# print(f"avg={sum/len(l)}")

##greatest element index
# l=[20,18,25,70,60]
# lar=l[0]
# index=0
# for i in range(len(l)):
#     if l[i]>lar:
#         lar=l[i]
#         index=i
# print(f'grater element is:{lar}, index is:[{index}]')

## second largest
# l=[4,8,2,9,12,10]
# lar=l[0]
# sec_lar=l[0]
# for i in l:
#     if i>lar:
#         sec_lar=lar
#         lar=i
#     elif i>sec_lar:
#         sec_lar=i    
# print(f"second largest is:{sec_lar} & largest is:{lar}")

##check list is shorted or not
# a=[10,20,30,40,70,50]
##a=[10,20,30,40,50]
# for i in range(len(a)-1):
#     if a[i]>=a[i+1]:
#         print("list is not shorted")
#         break
# else:
#     print("list is shorted")

##tuples
# a=("mon","tue",123,4321,"mon","sat")
# print(a[0])
# print(a.count("mon"))
# print(a.index("mon"))# frist accurance

## use case(unpacking tuple)
# def student():
#     return ("divas",19,"divas@gmail.com")
# info=student()
# name,age,gmail=info
# print(name)

###sets
# s={1,2,5,7,2,8,1,4,6}
# p={6,2,1,4}
# print(f"set is:{s};{p}")
# s.add(22)
# print(f"on adding single item in set:{s}")
# p.update([20,30])
# print(p)
# print(f"on adding multiple item in set:{p}")
# s.discard(2)
# print(s)
# print(f"union set are:{s|p}")
# print(f"intersection of set are: {s&p}")
# print("difference of set are:",s-p)
# print(f"symmetric difference:{s^p}")

#######################################################
# print(hash("hello"))#unique value for particular item
#######################################################

##loops on set
# a={30,40,40,90,8,80,95}
# for i in a:
#     print(i)


### dicitonary
# d={"name":"dominator","age":22,"contry":"france"}
# print(d["name"])
# d["inc"]=600#creating a new key value pair
# print(d)
# d.update({"inc":10000})
# d.pop("contry")
# print(d)
# d.popitem()#pop last inserted key-value pair
# print(d)
# print(d.get("grade"))#none b/z can't exixt in dict
# c=d.copy()
# print(d.items())
# d.clear()
# print(d)
# print(f"copy dict c=d:{c}")
# c.setdefault("name","kepler")#update if key value does't exist else return default value
# print(c)
##creating a new dict from itterable vslues(list/tupl)
# q=c.fromkeys(["a","b"],90707)
# print(q)
##reversing/loops
# d={10:100,20:200,30:300,40:400}
# for i in d:
#     print(f"keys ({i}) : values ({d[i]})")

##questions
# d1={"a":1}# d1+d2
# d2={"b":3}
# d1.update(d2)
# print(d1)
##or
# for i in d2:
#     d1[i]=d2[i]#aads new key:value if common then updates its
# print(d1)

##sum of all values
# d={10:100,20:200,30:300,40:400}
# sum=0
# for i in d:
#     sum=sum+d[i]
# print(sum)
## count no. of repetive keys in dict
# l=["a","b","c","a","a","b","c","b","b","c","d"]
# d={}
# for i in l:
#     if i in d.keys():
#         d[i]=d[i]+1
#     else:
#         d[i]=1
# print(d)
##aad two dict if key value pair exixt aad their value
# d1={'a':10,'b':20,"c":30}
# d2={'c':40,'d':50,'e':60}
# for i in d2:
#     if i in d1.keys():
#         d1[i]=d1[i]+d2[i]
#     else:
#         d1[i]=d2[i]
# print(d1)

### exception handling
# a=int(input("enter your 1st num-:"))
# b=int(input("enter your 2nd num-:"))
# try:
#     print(a/b)
# except Exception as err:
#     print(f"sorry an error occured as:{err}")
# else:
#     print("no error occured")
# finally:
#     print("if the're error or the're no error i will run no matter what is the condition is ")
# name=input("enter your name-:")
# print(f"Hello! your name is -:{name}") 

##rasie an manuall error
# age=int(input("enter your age:"))
# if age <18:
#     raise TypeError("you are not eligible")
# print("you're eligible")

###File Handling
# with open("sample.txt","w") as f:
#     data=input("enter a data you want to write in file-:")
#     f.write(data)

##reading a file
# with open("sample.txt","r") as f:
#     print(f.read())

## appending a newdata 
# with open("sample.txt","a") as f:
#     data=input("enter a data you want to append in file-:")
#     f.write(f"\n{data}")


