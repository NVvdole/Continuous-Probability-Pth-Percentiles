# File Name: FPPF.py
# Author: Verginia Mae Dole
# Date Created: 4/1/2022

from scipy.stats import f

print("F-Distribution Pth Percentile")
print("")
print("df1 = numerator degrees of freedom")
print("df2 = denominator degrees of freedom")
print("p = probability")
print("")

df1 = int(input("Enter df1: "))
while df1 < 1:
    df1 = int(input("Enter df1: "))
    
df2 = int(input("Enter df2: "))
while df2 < 1:
    df2 = int(input("Enter df2: "))
    
p = float(input("Enter p: "))
while p < 0.0 or p > 1.0:
    p = float(input("Enter p: "))
print("")

xp = f.ppf(p, df1, df2)

print("Pth Percentile")
print("Q(" + str(p) + ") = " + str(xp))
