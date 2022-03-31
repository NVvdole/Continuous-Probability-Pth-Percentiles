# File Name: WeibullPPF.py
# Author: Verginia Mae Dole
# Date Created: 4/1/2022

from scipy.stats import weibull_min

print("Weibull Distribution Pth Percentile")
print("")
print("\u03B1 = shape parameter")
print("\u03B2 = scale parameter")
print("p = probability")
print("")

alpha = float(input("Enter \u03B1: "))
while alpha <= 0.0:
    alpha = float(input("Enter \u03B1: "))
    
beta = float(input("Enter \u03B2: "))
while beta <= 0.0:
    beta = float(input("Enter \u03B2: "))
    
p = float(input("Enter p: "))
while p < 0.0 or p > 1.0:
    p = float(input("Enter p: "))
print("")

xp = weibull_min.ppf(p, alpha, scale = beta)

print("Pth Percentile")
print("Q(" + str(p) + ") = " + str(xp))
