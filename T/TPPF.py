# File Name: TPPF.py
# Author: Verginia Mae Dole
# Date Created: 4/1/2022

from scipy.stats import t

print("T-Distribution Pth Percentile")
print("")
print("df = degrees of freedom")
print("p = probability")
print("")

df = float(input("Enter df: "))
while df <= 0.0:
    df = float(input("Enter df: "))
    
p = float(input("Enter p: "))
while p < 0.0 or p > 1.0:
    p = float(input("Enter p: "))
print("")

xp = t.ppf(p, df)

print("Pth Percentile")
print("Q(" + str(p) + ") = " + str(xp))
