age = int(input("Enter your age: "))
if age>=18:
    print(" you are eligible to vote")
else:
    print("you are not eligible to vote")
    

#for loop using print numbers 1 to 5

for i in range(1,6):               
    print(i)
#voting eligibility loop + condition combo

for i in range(1,4):
    age = int(input("Enter age: "))
    if age>=18:
        print("you are eligible to vote")
    else:
        print("you are not eligible to vote")


#even number

for i in range(1,11):
    if i%2==0:
        print(i)
        
#odd number

for i in range(1,21):
    if i%2==1:
        print(i)
        
#practice task

for i in range(10,0,-1):
    print(i)

#check pass/fail for 5 students

for i in range(1,6):
    marks = int(input("Enter marks: "))
    if marks>=35:
        print("you are passed")
    else:
        print("you are failed")

#while loop

i = 1
while i<=5:
    print(i)
    i += 1
#simple login chech
password =""
while password != "python":
    password = input("Enter password: ")
print("login successful")
    
#print numbers 5 to 1
i=5
while i>=1:
    print(i)
    i -= 1
    
    #age repeatedly 
age =0
while age<18:
    age = int(input("Enter age:"))
    print("you are 18 or above")


    
