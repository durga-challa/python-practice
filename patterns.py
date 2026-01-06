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