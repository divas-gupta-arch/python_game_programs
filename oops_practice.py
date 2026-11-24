# print("hello welcome to object oriented programing")

### classes

## accesing attributes and methods
# class animal:
#     type= "cat"          # attribute
#     def sound(self):     # method
#         print("meow")

# print(animal().type)  #acess attributes
# animal().sound()      # call method

### objects

# class fruit:
#     name= "apple"
#     def condition(self):
#         print("fruits are fresh")
# f=fruit()
# print(f.name)  #accessing attributes
# f.condition()

### constructor

# class bags:
#     def __init__(self,materail,zips,pockets):   ## here self store the addresses of objects
#         self.materail=materail
#         self.zips=zips
#         self.pockets=pockets

#     def info(self):
#         print(f"materail={self.materail}; zips={self.zips}; pockets={self.pockets}")

# safari=bags("polyster",6,3)
# campus=bags("lather",2,1)
# safari.info()
# print(campus.pockets)

### type of attributes

# class Student:
#     college = "CCSU"            # class attribute
#     def __init__(self, name, age):
#         self.name = name        # instance attribute
#         self.age = age          # instance attribute

# s1 = Student("Dominator",20)
# s2 = Student("Rahul",21)

# print(s1.name)   
# print(s2.name)   
# s1.name = "Aman"          # changes s1 only
# print(s2.name)            # Rahul (unchanged)

# print(s1.college, s2.college)   # CCSU CCSU
# Student.college = "DU"          # change it through the class
# print(s1.college, s2.college)   # DU DU (changed for everyone)

### methods

# class animal:
#     a= 12
#     def __init__(self,name):
#         self.name=name
#     def hello(self):    # instance/object method.. its capture the location of object 
#         print(f"how are you my name is {self.name}")

#     @classmethod 
#     def details(cls):  # class method.. its capture the location of class
#         print(f" hello sir i am {cls.a}")

#     @staticmethod
#     def speak():       # static method.. its cant capture any location
#         print("hello i am a static method")

# obj=animal("lion")
# obj.hello()
# animal.details()
# animal.speak()

### ineritance

# class animal:   # parent/base class
#     a=13
#     def __init__(self,name):
#         self.name= name
#     def details(self):
#         print(f"hello your name is: {self.name}")

# class humans(animal):   # child/derived class can able to access the attributes and methods por parent/base class
#     pass

# obj=animal("lion")
# obj2=humans("harsh")
# obj2.details()
# print(obj2.a)