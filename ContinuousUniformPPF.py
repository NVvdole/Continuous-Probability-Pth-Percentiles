# File Name: ContinuousUniformPPF.py
# Author: Verginia Mae Dole
# Date Created: 4/1/2022

print("Continuous Uniform Distribution Pth Percentile")
print("")
print("a = lower bound")
print("b = upper bound")
print("p = probability")
print("")

a = float(input("Enter a: "))

b = float(input("Enter b: "))
while b <= a:
    b = float(input("Enter b: "))
    
p = float(input("Enter p: "))
while p < 0.0 or p > 1.0:
    p = float(input("Enter p: "))
print("")

xp = a + (p * (b - a))

print("Pth Percentile")
print("Q(" + str(p) + ") = " + str(xp))
