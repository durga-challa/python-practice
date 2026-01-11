student = {
    "name": "durga",
    "age": 19,
    "branch": "IT"
    }
print(student) 
#acess dictionary elements
print(student["name"])
print(student["branch"])
#change dictionary elements
student["age"]=20
student["college"]="ABC college"
print(student)
#loop through a dictionary
for key, value in student.items():
    print(key,":",value)
#important dictionary functions
print(student.keys())
print(student.values())
print(student.items())
#mini project practice program
student = {}

student["name"]=input("enter name:")
student["age"]=input("enter age:")
student["branch"]=input("enter branch:")
student["college"]=input("enter college:")

print("\nStudent Details:")
for k,v in student.items():
    print(k,":",v)