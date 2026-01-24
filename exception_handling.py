try:
    x=int(input("Enter a number: "))
    print(x)
except:
    print("An error occurred. Please enter a valid integer.")

    #division by zero
try:
    a=int(input("Enter number"))
    b=int(input("Enter another number"))
    print(a/b)
except:
    print("Error: Division by zero is not allowed.")

    #catch specific error

try:
    a=int(input("Enter number"))
    b=int(input("Enter another number"))
    print(a/b)
except ZeroDivisionError:
    print("Cannot divide by zero.")
except ValueError:
    print("please enter numbers only")

    #else and finally

try:
    x=int(input("Enter a number: "))
except:
    print("Error")
else:
    print("You entered:", x)
finally:
    print("Done")
   
    #minin program: calculator
try:
    a= int(input("Enter first number: "))
    b= int(input("Enter second number: "))
    print("result:", a/b)
except ZeroDivisionError:
    print("Cannot divide by zero.")
except ValueError:
    print("Invalid input. Please enter numeric values.")
finally:
    print("program ended.")