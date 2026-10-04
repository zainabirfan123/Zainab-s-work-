#loops 
i = 1 
while i <= 5: 
    name = input("Enter your name: ")
    marks = int(input("Enter your marks: "))
    if marks >= 40:
        print(f"{name} : Pass")
    i = i + 1 
print(i)  