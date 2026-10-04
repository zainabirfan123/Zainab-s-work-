"""
RECORD CHECK  -  my version
===========================

Name  : Zainab Irfan 
Lane  :  AI 
Date  : 3 October 2026

"""
#THRESHOLD 
label = input("Enter a label: ")     
used = float(input("Enter a value: "))     
total = float(input("Enter a limit: "))

print("=" * 30)
print(f"  RECORD CHECK - {label}")
print("=" * 30)
if used > total:
    status = "OVER LIMIT"
else:
    status = "OK"
print(f"USED  : {used:>10.2f}")
print(f"TOTAL : {total:>11.2f}")
print(f"STATUS: {status:>7}")

#TYPICAL 
label = input("Enter a label: ")     
used = float(input("Enter a value: "))     
total = float(input("Enter a limit: "))
difference = total - used  
percent = (used / total * 100) 
if percent > 100:
    status = "OVER LIMIT"
elif percent >= 90:
    status = "WARNING"
else:
    status = "OK"
print ("=" * 30)
print(f"  RECORD CHECK - {label}")  
print ("=" * 30)
print(f"USED   : {used:>10.2f}")
print(f"TOTAL  : {total:>11.2f}")
print(f"free   : {difference:>10.2f}") 
print(f"percent: {percent:>10.2f} %")  
print(f"STATUS : {status:>7}")

#EXCELLENT
count = 0  
while True:
    label = input("Enter a label: ")     
    used = float(input("Enter a value: "))     
    total = float(input("Enter a limit: "))
    if label == "quit":
        break 
    else:
        difference = total - used  
        percent = (used / total * 100) 
        if percent > 100:
            status = "OVER LIMIT"
            count += 1 
        elif percent >= 90:
            status = "WARNING"
        else:
            status = "OK"
        print ("=" * 30)
        print(f"  RECORD CHECK - {label}")  
        print ("=" * 30)
        print(f"USED   : {used:>10.2f}")
        print(f"TOTAL  : {total:>11.2f}")
        print(f"free   : {difference:>10.2f}") 
        print(f"percent: {percent:>10.2f} %")  
        print(f"STATUS : {status:>7}")
print(f"\nTotal number of records over the limit are : {count}")


