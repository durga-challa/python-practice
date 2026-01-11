marks =[]
n = int(input("How many subjects"))
for i in range(n):
    m=int(input(f"Enter marks for subject {i+1}:"))
    marks.append(m)
total = sum(marks)
average = total/n

print("Marks:",marks)
print("Total:",total)
print("Average:",average)

if average >=75:
    print("Grade: A")
elif average >= 60:
    print("Grade: B")
elif average >= 40:
    print("Grade: c")
else:
    print("Fail")