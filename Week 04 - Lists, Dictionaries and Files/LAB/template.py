"""
RECORD CHECK  -  my version
===========================

Name  : Zainab Irfan
Lane  :  AI 
Date  : 14 October 2026 

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




def check_record(value, limit):
    difference = limit - value
    percent = (value / limit) * 100 
    return difference, percent 

difference1, percent1 = check_record(87.0, 100.0)
print(f"difference : {difference1} \npercent : {percent1}")



def print_report(label, value, limit, difference, percent,status):
    print("=" * 34)
    print(f"RECORD CHECK - {label}")
    print("=" * 34)
    print(f"Used    : {value:>10.2f} ")
    print(f"Total   : {limit:>10.2f}")
    print(f"Free    : {difference:>10.2f}")
    print(f"Percent : {percent:>10.2f}")
    print(f"Status  : {status:>10}")
    print("=" *34)
    
   


records = [
    {"label" : "R-001", "value" : 87.0, "limit" : 100.0},
    {"label" : "R-002", "value" : 120.0, "limit": 100.0},
    {"label" : "R-003", "value" : 45.0, "limit" : 100.0},


]

    
with open("Records.txt", "w") as r:
    for record in records:
        r.write(
            f"{record['label']},{record['value']},{record['limit']}\n"
        )


def load_records(path):
    """Read label,value,limit lines from a file and return a list of dicts."""
    records = []
    try:
        with open(path) as f:
            for line in f:
                label, value, limit = line.strip().split(",")
                records.append({
                    "label": label,
                    "value": float(value),
                    "limit": float(limit)
                })
    except FileNotFoundError:
        print("file not found")
        return []
    return records




overlimit_count = 0

records = load_records("Records.txt")

with open("Results.txt", "w") as output:
    for record in records:
        label = record["label"]
        value = record["value"]
        limit = record["limit"]

        difference, percent = check_record(value, limit)
        status = status_of(percent)

        print_report(
            label, value, limit, difference, percent, status
        )

        output.write(f"{label},{status}\n")

        if status == "OVER LIMIT":
            overlimit_count += 1

print(f"Number of records over the limit: {overlimit_count}")




