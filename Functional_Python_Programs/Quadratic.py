"""
    * Author - Nitin Chandrakant Babar
    * Date -  15-12-2021
    * Time -  10Am
    * Title - Quadratic
"""

import cmath

a=float(input("Enter the value of a: "))
b=float(input("Enter the value of b: "))
c=float(input("Enter the value of c: "))

delta= (b*b-(4*a*c))

root1 = (-b+(cmath.sqrt(delta)))/(2*a)
root2 = (-b-(cmath.sqrt(delta)))/(2*a)

print("Root1 of x is : ",root1)
print("Root2 of x is : ",root2)
