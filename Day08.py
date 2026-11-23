# delete keyword in python


# class Student:
#     name="Shivam"

# s1=Student()

# print(s1)

# del s1
# print(s1)


# # Private attribute and Methods in the Python


# class Account:
#     def __init__(self,acc_no,acc_pass):
#         self.acc_no=acc_no
#         self.__acc_pass=acc_pass



# acc1=Account("1234","hycje")

# print(acc1.__acc_pass)

# Class ke andar private wale ko ham access nhi kar skte hai
# We can also make private function....


# class Account1:
#     acc_no="86868"
#     bal=989

#     def __init__(self):

#         print(self.bal)

#     def __hello(self):
#         print("hello")

## we cant call private function from the outside 


#Inheritance in oops python


# class Car:

#     @staticmethod
#     def start():
#         print("Car Started")
    
#     @staticmethod
#     def stop():
#         print("Car Stop")



# class Toyotacar(Car):
#     def __init__(self,name):
#         self.name=name


# car1=Toyotacar("Fortuner")

# car2=Toyotacar("Endevour")

# print(car1.name)

# print(car2.name)

# print(car1.start())
# print(car2.start())


# There are three types of inheritance 


# Single Inheritance
# Multilevel Inheritance
# Multiple Inheritance-- Inherit Property from multiple class

# class A:
#     var1="Welcome to class A"

# class B:
#     var2="Welcome to class B"

# class C(A,B):
#     var3="Welcome to class C"

# c1=C()

# print(c1.var1)
# print(c1.var2)
# print(c1.var3)

# Super Method 

# class Car:
#     def __init__(self, type):
#         self.type = type

#     @staticmethod
#     def start():
#         print("car started..")

#     @staticmethod
#     def stop():
#         print("car stopped.")


# class ToyotaCar(Car):
#     def __init__(self, name,type):
#         self.name = name
#         super().__init__(type)
#         super().start()


# c1=ToyotaCar("Fortuner","Electric")

# print(c1.type)


class Person:
    name="Shivam"

    def changeName(self, name):
        self.name=name
    @classmethod
    def changeName(cls,name):
        cls.name=name

p1=Person()

p1.changeName("Rahul Kumar")

print(p1.name)

print(Person.name)

# We have to change class Attribute

# self.name ke jagah person.name="Rahul Kumar"

#person.name se class ka bhi chnage and p1 ka bhi change 

# self.__class__.name="Rahul"



class Student:
    def __init__(self, phy, chem, math):
        self.phy = phy
        self.chem = chem
        self.math = math
        self.percentage = str((self.phy + self.chem + self.math) / 3) + "%"

    def calcPercentage(self):
        self.percentage = str((self.phy + self.chem + self.math) / 3) + "%"


stu1 = Student(98, 97, 99)
print(stu1.percentage)

stu1.phy = 86
print(stu1.phy)
stu1.calcPercentage()
print(stu1.percentage)


## Upar wala ek tarika hai lekin isko karne ka ek aur acha tarika hai 


## With the help of property decorator 


#34 ke baad study

















