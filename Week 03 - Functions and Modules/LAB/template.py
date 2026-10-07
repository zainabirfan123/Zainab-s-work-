"""
RECORD CHECK  -  my version
===========================

Name  :  Zainab Irfan 
Lane  :  AI 
Date  :  7 October 2026 

Run it:   python template.py

"""



def status_of(percent):
    """this function tells the status of the percentage"""
    if percent >= 100:
        return "OVER LIMIT"
    elif percent >= 90: 
        return "WARNING"
    else:
        return "OK"




def check(value, limit):
    """this function calculates the difference between value and limit and value as a percentage of limit """
    difference = value - limit 
    percent = (value/ limit) * 100
    return difference , percent 



def print_report(label, value, limit, difference, percent,status):
    print("=" * 34)
    print(f"RECORD CHECK - {label}")
    print("=" * 34)
    print(f"Used    : {value:>10.2f} ")
    print(f"Total   : {limit:>10.2f}")
    print(f"Free    : {difference:>10.2f}")
    print(f"Percent : {percent:>10.2f}")
    print(f"Status  :{status:>10}")
    print("=" *34)
    
   
overlimit_count = 0 

while True:
    label = input("Enter the label or quit to stop : ")

    if label == "quit":
        break 
    else:
        value = float(input("Enter your value: "))
        limit = float(input("Enter your limit: "))
        difference , percent = check(value, limit)
        status = status_of(percent)

        print_report(label, value, limit, difference, percent, status)

        if status == "OVER LIMIT":
            overlimit_count += 1 


print(f"Number of records that are over the limit {overlimit_count}")



