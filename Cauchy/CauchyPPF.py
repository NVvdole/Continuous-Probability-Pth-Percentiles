# File Name: CauchyPPF.py
# Author: Verginia Mae Dole
# Date Created: 4/1/2022

from scipy.stats import cauchy

print("Cauchy Distribution Pth Percentile")
print("")
print("\u03BC = location parameter")
print("\u03C3 = scale parameter")
print("p = probability")
print("")

mu = float(input("Enter \u03BC: "))

sig = float(input("Enter \u03C3: "))
while sig <= 0.0:
    sig = float(input("Enter \u03C3: "))
    
p = float(input("Enter p: "))
while p < 0.0 or p > 1.0:
    p = float(input("Enter p: "))
print("")

xp = cauchy.ppf(p, loc = mu, scale = sig)

print("Pth Percentile")
print("Q(" + str(p) + ") = " + str(xp))
