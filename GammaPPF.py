# File Name: GammaPPF.py
# Author: Verginia Mae Dole
# Date Created: 4/1/2022

from scipy.stats import gamma

print("Gamma Distribution Pth Percentile")
print("")
print("\u03B1 = shape parameter")
print("\u03BB = rate parameter")
print("p = probability")
print("")

alpha = float(input("Enter \u03B1: "))
while alpha <= 0.0:
    alpha = float(input("Enter \u03B1: "))
    
lamb = float(input("Enter \u03BB: "))
while lamb <= 0.0:
    lamb = float(input("Enter \u03BB: "))
    
p = float(input("Enter p: "))
while p < 0.0 or p > 1.0:
    p = float(input("Enter p: "))
print("")

xp = gamma.ppf(p, alpha, scale = 1.0 / lamb)

print("Pth Percentile")
print("Q(" + str(p) + ") = " + str(xp))
