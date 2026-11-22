# List in python

# marks = [87, 64, 33, 95, 76]
# student = ["Karan", 85, "Delhi"]

# print(marks)
# print(len(marks))
# print(type(marks))
# print(student)
# print(marks[0])   
# print(student[2])

#List Slicing

marks = [87, 64, 33, 95, 76]

print(marks[1:4])
print(marks[:4])   
print(marks[1:])   
print(marks[-3:-1])

# List Method

nums = [2, 1, 3]
nums.append(4)
print(nums)

nums = [2, 1, 3]
nums.sort()
print(nums)

nums.sort(reverse=True)
print(nums)

nums = [2, 1, 3]
nums.reverse()
print(nums)


nums = [2, 1, 3]
nums.insert(1, 5) # insert 5 at index 1
print(nums)

nums = [2, 1, 3, 1]
nums.remove(1) # removes first 1 only
print(nums)

nums = [2, 1, 3, 1]
nums.pop(2) # removes element at index 2
print(nums)


#Tuple

# tup = (87, 64, 33, 95, 76)

# print(tup[0])
# print(tup[1:3])
# print(len(tup))


tup1 = ()
tup2 = (1,)
tup3 = (1, 2, 3)

print(type(tup2))
print(type((1)))

tup = (2, 1, 3, 1)

print(tup.index(1))
print(tup.count(1))







