def greet():
    print("Hello, welcome to python")
greet() 
#function with parameter
def greet(name):
    print("Hello",name) 
greet("Durga")
greet("friend")
#function with return value
def add(a,b):
    return a+b
result = add(10,20)
print(result)
#function to check pass/fail
def check_result(marks):
    if marks >=35:
        print("pass")
    else:
        print("fail")
check_result(40)
check_result(20)        
#function to print square of a nunmber
def square(n):
    return n*n 
print(square(5))
#break and continue
   #break (stops the loop completely)
for i in range(1,6):
    if i==3:
        break
    print(i)
#continue (skips the current iteration and continues with the next)  
for i in range(1,6):
    if i==3:
        continue
    print(i)
#pattern printing star triangle
for i in range(1,6):
    print("*"*i)
#pattern printing reverse star
for i in range(4,0,-1):
    print("*"*i)
#number pattern
for i in range(1,6):
    for j in range(1,i+1):
        print(j,end="")
    print()
