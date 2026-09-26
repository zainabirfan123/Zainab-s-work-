"""
RECORD CHECK  -  my version
===========================

Name  : Zainab 
Lane  :  AI 
Date  : 25 September 2026 


"""

label = input("Enter a label : ")
first = float(input("Enter the first number : "))
second = float(input("Enter the second number : "))
difference = second - first 
percent = (first / second) * 100
print(f"difference = {difference:.2f}")
print(f"percent = {percent:.2f}")


print("=" * 30)
print(f"  RECORD CHECK - {label}")
print("=" * 30)
print(f"First number  : {first:>10.2f}")
print(f"Second number : {second:>10.2f}")
print("=" * 30)

print(f"difference : {difference:>+10.2f}")
print(f"percent    : {percent:>10.2f} %")











