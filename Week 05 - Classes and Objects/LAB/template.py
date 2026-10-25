"""
RECORD CHECK  -  my version
===========================

Name  : Zainab Irfan 
Lane  :  AI 
Date  : 21/10/2026

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""


class Record:
    overlimit_count = int(0)
    def __init__(self, label , value, limit):
        self.label = label 
        self.value = value 
        self.limit = limit
    def status(self):
        percent = (self.value / self.limit) * 100 
        """this will use the formula to calculate the percentage and decide its status depending on percentage"""
        if percent >= 100:
            return "OVER LIMIT"
        elif percent >= 90:
            return "WARNING"
        else:
            return "OK"

    def over_limit(self):
        return self.value>self.limit

r1 = Record("R-001", 85.0, 100.0)
r2 = Record("R-002", 120.0, 100.0)


print("=" * 34)
print(f"  RECORD CHECK  -  {r1.label}")
print(f"value: {r1.value}")
print(f"limit: {r1.limit}")
print(f"status: {r1.status()}")

print("=" * 34)

print("=" * 34)
print(f"  RECORD CHECK  -  {r2.label}")
print(f"value: {r2.value}")
print(f"limit: {r2.limit}")
print(f"status: {r2.status()}")
print("=" * 34)


with open("new_records2.txt", "w") as f:
    f.write("R-001 , 97, 100\n")
    f.write("R-002 , 60, 100\n")
    f.write("R-003, 120, 100\n")

path = "new_records2.txt"

def load_records(path):
    records = [] 
    with open(path , "r") as f:
        for line in f:
            label, value, limit = line.strip().split(",")
            records.append(Record(label, float(value), float(limit)))

    return records 

new_records = load_records("new_records2.txt")

for record in new_records:
    print("=" * 34)
    print(f"RECORD CHECK - {record.label}")
    print(f"Value {record.value}")
    print(f"Limit {record.limit}")
    print(f"Status {record.status()}")
    print("=" * 34)

overlimit_count2 = sum(record.over_limit() for record in new_records)
print(f"{overlimit_count2} out of {len(new_records)} were over the limit")
print("=" * 34)



    



"""
    # your report lines go here

    print("=" * 34)


    def status(self):
        percent = (self.value / self.limit) * 100 
        this will use the formula to calculate the percentage and decide its status depending on percentage
        if percent >= 100:
            return "OVER LIMIT"
        elif percent >= 90:
            return "WARNING"
        else:
            return "OK"

    def over_limit(self):
        if self.status() == "OVER LIMIT":
            overlimit_count += 1 




r1 = Record("R-001", 85.0, 100.0)
r2 = Record("R-002", 120.0, 100.0)

print(r1.status())
print(r2.status())

"""

    
        
# ====================================================================== CLASS
# 1. Define a class called Record.
#
#    Threshold : __init__(self, label, value, limit) storing all three as
#                attributes. No methods yet.
#    Typical   : add a method status(self) that returns "OVER LIMIT" (100%+),
#                "WARNING" (90%+) or "OK", worked out from self.value and
#                self.limit. Give it a one-line docstring.
#    Excellent : also add over_limit_count as a class-level running total -
#                see the note below.

# your class goes here


# ==================================================================== RECORDS
# 2. Create your records.
#
#    Threshold : create at least 2 Record instances directly in the code.
#    Typical   : same, but now print each one's .status() as well.
#    Excellent : instead, write load_records(path) that reads label,value,limit
#                lines from a file and returns a list of Record objects. Make
#                your own data file, one record per line.

records = []   # replace with your code


# ==================================================================== OUTPUT
# 3. Print a report for each record.
#
#    Threshold : label, value, limit, inside a border.
#    Typical   : add the result of .status().
#    Excellent : also keep a running count of how many came back OVER LIMIT
#                across every record, and print that once, after the loop.
#                (Simplest: a plain variable outside the loop, same pattern
#                as Week 4. If you want it to live ON the object instead,
#                that is a stretch worth trying - but a variable is enough.)

for record in records:
    print()
    print("=" * 34)
    print(f"  RECORD CHECK  -  {record.label}")
    print("=" * 34)

    # your report lines go here

    print("=" * 34)


# ==========================================================================
# 4. Before you finish:
#
#    [ ] Run it and check every record's numbers by hand
#    [ ] Check every method only reads/changes its OWN object (self) -
#        nothing reaches outside itself
#    [ ] Check every method and __init__ has a one-line docstring
