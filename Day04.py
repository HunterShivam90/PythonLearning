
info={
    "name":"Shivam",
    "learning":"Coding",
    "class":"Btech",
    "Subjects":["Physics","Chemistry","Biology"]
}

print(info)

print(type(info))

print(info["name"])

info["name"]="Priyanshi"
info["surname"]="Singh"
print(info)

student={
    "name":"Shivam",
    "Subject":{
        "Physics":90,
        "Chemistry":98,
        "Math":78

    }
}

print(student)

print(student.keys())

print(len(student))

print(student.values())

print(student.items())

student.update({"city":"delhi"})

print(student)


#Sets in python


collection={1,2,3,4}

print(type(collection))

#Set ignore duplicate values 

print(len(collection))

#How to create Empty set

collection1=set() 

print(type(collection1))

collection1.add(1)
collection1.add(2)
collection1.add((1,2,3))
collection1.add("Shivam")

collection1.clear()

collection2={"hello","ApnaCollege","garhwa","ranchi","Jharkhand"}

collection2.pop()

#randomly value pop





