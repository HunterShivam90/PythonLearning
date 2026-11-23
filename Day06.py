def sum(a,b):
    return a+b

print(sum(2,3))

def printHel():
    print("Hello")


printHel()

# Function which will give average of 3 number

def avg(a,b,c):
    return (a+b+c)/2


print(avg(2,3,4))

print("Apna College",end=" ")
print("Shivam Kumar Singh")

# Default Parameter
# last se default value 

def prod(a=1,b=2):
    return a*b

prod()

# Write a function to print length of a list

cities=["Delhi","Gurgaon","Mumbai","garhwa","ranchi","Jamshedpur"]


def count(list1):
    return len(list1)

print(count(cities))

#Write a function to print item of the list in the single line

def print_list(list2):
    for el in list2:
        print(el,end=" ")



# Write a function to print factorial of the number 

def fact(n):
    fact=1
    for i in range(1,n+1):
        fact=fact*i
        return fact


# Write a function to convert usd to inr


def usd(n):
    return n*90

# Recursion 


# Print n to 1 using recursion

def print1(n):
    if(n==0):
        return
    print(n)
    print1(n-1)

# Recursive function to find factorial of the number 


def fact(n):
    if(n==1):
        return 1
    return n *fact(n-1)

# Write a recursive function to calculate the sum of first n natural number 


def sum1(n):
    if(n==1):
        return 1
    return n+sum1(n-1)

