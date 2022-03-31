# File Name: ChiPPF.py
# Author: Verginia Mae Dole
# Date Created: 4/1/2022

from scipy.stats import chi

print("Chi Distribution Pth Percentile")
print("")
print("df = degrees of freedom")
print("p = probability")
print("")

df = int(input("Enter df: "))
while df < 1:
    df = int(input("Enter df: "))
    
p = float(input("Enter p: "))
while p < 0.0 or p > 1.0:
    p = float(input("Enter p: "))
print("")

xp = chi.ppf(p, df)

print("Pth Percentile")
print("Q(" + str(p) + ") = " + str(xp))
