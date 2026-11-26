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

### costructor with class

# class bagsfatory:
#     def __init__(self,materail,zips,pockets):   
#         self.materail=materail
#         self.zips=zips
#         self.pockets=pockets

#     def details(self):
#         print("your bag details are-")
#         print(self.materail)
#         print(self.zips)
#         print(self.pockets)

# class reebok(bagsfatory):
#     def __init__(self, materail, zips, pockets,color):
#         super().__init__(materail, zips, pockets)
#         self.color=color
#     def  details(self):
#         super().details()
#         print(self.color)

# bag1=bagsfatory("leather",3,2)
# bag2=reebok("polyster",2,5,"black")

# # bag1.details()
# bag2.details()

### types of inheritance

### single inheritance -- inheritGE CLASS SINGLW TIME ONLY

# class Person:
#     def greet(self):
#         print("Hello")
# class Student(Person):
#     def study(self):
#         print("Studying")
# s = Student()
# s.greet()       
# s.study()

### multilevel inheritance -- chain-grandparent-parent-child

# class Vehicle:  # grangparent class
#     def start(self):
#         print("Vehicle started")
# class Car(Vehicle):  # parent class
#     def drive(self):
#         print("Car driving")
# class ElectricCar(Car):  #child class
#     def charge(self):
#         print("Charging")
# e = ElectricCar()
# e.start()       # from Vehicle
# e.drive()       # from Car
# e.charge()      # its own

### hierarchial class -- one parent many children

# class Animal:   #parent
#     def eat(self):
#         print("Eating")
# class Dog(Animal):  # child
#     def bark(self):
#         print("Woof")
# class Cat(Animal):
#     def meow(self):  # child 
#         print("Meow")

### multiple inheritance -- one child many patent

# class animal:                #parent
#     def __init__(self,name):
#         self.name= name
# class humans:                 #parent
#     def __init__(self,id):
#         self.id=id
# class robots(humans,animal):  #child
#     def __init__(self, id,name):
#         humans.__init__(id)
#         animal.__init__(self.name)

# robo=robots(977,"dominator")

### hybride inheritance -- a mix of two or more thye above

# class A:
#     def show_a(self): print("A")
# class B(A):                 # single / hierarchical
#     def show_b(self): print("B")
# class C(A):
#     def show_c(self): print("C")
# class D(B, C):              # multiple
#     pass
# d = D()
# d.show_a(); d.show_b(); d.show_c()

### polymorphism -- gives different result on same call for different data types

### thypes of polymorphism

### duck typing method

# class Dog:  
#     def speak(self):
#         print("Woof")
# class Cat:
#     def speak(self):
#         print("Meow")
# for animal in [Dog(), Cat()]:
#     animal.speak()          # same call, different result

### method overriding -- we need inheritance 

# class Shape:
#     def area(self):
#         print("Area not defined")

# class Circle(Shape):
#     def area(self):                 # overrides the parent's area()
#         print("Circle area = 3.14 * r * r")

# class Square(Shape):
#     def area(self):
#         print("Square area = side * side")

# for s in [Circle(), Square()]:
#     s.area()
    