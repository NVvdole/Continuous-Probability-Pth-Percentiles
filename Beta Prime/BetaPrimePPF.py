# File Name: BetaPrimePPF.py
# Author: Verginia Mae Dole
# Date Created: 4/1/2022

from scipy.stats import betaprime

print("Beta Prime Distribution Pth Percentile")
print("")
print("\u03B11 = first shape parameter")
print("\u03B12 = second shape parameter")
print("p = probability")
print("")

alpha1 = float(input("Enter \u03B11: "))
while alpha1 <= 0.0:
    alpha1 = float(input("Enter \u03B11: "))
    
alpha2 = float(input("Enter \u03B12: "))
while alpha2 <= 0.0:
    alpha2 = float(input("Enter \u03B12: "))
    
p = float(input("Enter p: "))
while p < 0.0 or p > 1.0:
    p = float(input("Enter p: "))
print("")

xp = betaprime.ppf(p, alpha1, alpha2)

print("Pth Percentile")
print("Q(" + str(p) + ") = " + str(xp))
