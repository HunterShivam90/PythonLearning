
# class creation in python


# class Student:
#     name="Shivam"

# s1=Student()

# print(s1.name)

# class Car:
#     color="Blue"
#     brand="Mercedes"

# car1=Car()

# print(car1.color)

# print(car1.brand)

# class Student:
#     def __init__(self,fullname):
#         print(self)
#         self.name =fullname

# s1=Student("Shivam")

# print(s1)
# print(s1.name)

# s2=Student("Arjun")

# print(s2)


class Student:

    college_name="ABC College Of Engineering"

    #Default Constructor
    def __init__(self):
            print(self)

    # Parametrized Constructor
            
    def __init__(self,fullname):
        print(self)
        self.name =fullname

#Parameter ke saath jo constructor match hoga wahi constructor call hoga 

#Class is the combination of two things data and variable


class Teacher:
    name="Anonymous"
    college="NIT Jamshedpur"

    def __init__(self):
        print("Constructor is called")
    
    def Hello(self):
        print("Hello",self.name)

t1=Teacher()

print(t1.name)


# Static method is also called decorator in python ..we can use function without self



# class Car:
#      name="Hyundai"
#      @staticmethod   #Decorator...
#      def hello():
#           print("hello")


# Abstraction in oops

class Car:
    def __init__(self):
        self.acc = False
        self.brk = False
        self.clutch = False

    def start(self):
        self.clutch = True
        self.acc = True
        print("car started..")


car1 = Car()
car1.start()


# Encapsulation === Wrapping up of data and information in a single unit while controlling access to them

class Account:
    def __init__(self, bal, acc):
        self.balance = bal
        self.account_no = acc

    def debit(self, amount):
        self.balance -= amount
        print("Rs.", amount, "was debited")
        print("total balance = ", self.get_balance())

    def credit(self, amount):
        self.balance += amount
        print("Rs.", amount, "was credited")
        print("total balance = ", self.get_balance())

    def get_balance(self):
        return self.balance


acc1 = Account(10000, 12345)
acc1.debit(1000)
acc1.credit(500)





