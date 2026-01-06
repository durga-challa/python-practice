def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    if b==0:
        return "Connot divide by zero"
    return a/b
while True:
    print("\n1.Add 2.sub 3.mul 4.div 5.exit")
    choice = int(input("Enter your choice: "))
    if choice==5:
        break
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    if choice==1:
        print(add(a,b))
    elif choice == 2:
        print(sub(a,b))
    elif choice == 3:
        print(mul(a,b))
    elif choice == 4:
        print(div(a,b))
    else:
        print("Invalid choice")

#number guessing
secret =7
while True:
    guess = int(input("guess number:"))
    if guess == secret:
        print("Correct!")
        break
    else:
        print("Try again!")