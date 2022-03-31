# File Name: ExponentialPPF.py
# Author: Verginia Mae Dole
# Date Created: 4/1/2022

from scipy.stats import expon

print("Exponential Distribution Pth Percentile")
print("")
print("\u03BB = rate parameter")
print("p = probability")
print("")

lamb = float(input("Enter \u03BB: "))
while lamb <= 0.0:
    lamb = float(input("Enter \u03BB: "))
    
p = float(input("Enter p: "))
while p < 0.0 or p > 1.0:
    p = float(input("Enter p: "))
print("")

xp = expon.ppf(p, scale = 1.0 / lamb)

print("Pth Percentile")
print("Q(" + str(p) + ") = " + str(xp))
