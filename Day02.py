# str1="This is a string"
# str2='This is also a string'
# str3="""This is also a string"""


# str4="This is a string.\nWe are creating in a python."

# print(str4)

# String Concatenation

# str1="apna"
# str2="college"

# str3=str1+str2

# print(str3)

#Length of string 

# print(len(str1))

#Indexing in string

# str1="Shivam"

# ch=str1[2]

# print(ch)

# only access not manipulate 

# Slicing-- Accessing part of the string

# str1="Shivam Kumar Singh"

# str2=str1[1:4] #End string isnot included

# str2=str1[:4] #0 se 4
# str2=str1[1:] #1 se len(str1)

#We can also do slicing with negative indexing

# print(str2)


s = "I am a coder."

print(s.endswith("er.")) # returns True if string ends with substr
print(s.capitalize()) # capitalizes 1st char
print(s.replace("coder", "developer")) # replaces all occurrences of old with new (syntax: s.replace(old, new))
print(s.find("coder")) # returns 1st index of 1st occurrence (syntax: s.find(word))
print(s.count("am")) # counts the occurrence of substr in string


light = "yellow"

if light == "red":
    print("Stop")
elif light == "yellow":
    print("Look")
elif light == "green":
    print("GO")
else:
    print("Light is broken")











