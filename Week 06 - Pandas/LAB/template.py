"""
RECORD CHECK  -  my version
===========================

Name  :  Zainab Irfan 
Lane  :  AI 
Date  :  4 November 2026 

Run it:   python template.py

"""
import pandas as pd



df = pd.read_csv("/Users/zainab/Downloads/Week 06 - Pandas/LAB/test2.csv")  
print(df) 

df["percent"] = ((df["value"] / df["limit"]) * 100)

df["status"] = df["percent"].apply(lambda x: "OVER LIMIT" if x > 100 else "WARNING" if x > 90 else "OK")
print(df)
print("=" * 60)
print(df[df["status"] != "OK"])
print("=" * 60)
print(df.groupby("status").size())
df.to_csv("myFile4.csv")
 
import matplotlib.pyplot as plt
statusCount = df["status"].value_counts()
statusCount.plot(kind = "bar")
plt.title("Counts per Status")
plt.xlabel("Status")
plt.ylabel("Count")
plt.savefig("status_counts_bar_chart.png")

