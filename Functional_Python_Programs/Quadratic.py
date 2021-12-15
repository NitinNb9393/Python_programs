"""
    * Author - Nitin Chandrakant Babar
    * Date -  15-12-2021
    * Time -  10Am
    * Title - Quadratic
"""

#cmath module using to compute the math function for complex numbers
import cmath

#initalize the variables taking from UserInput.
a=float(input("Enter the value of a: "))
b=float(input("Enter the value of b: "))
c=float(input("Enter the value of c: "))

#Math Formula for Quadratic Equation
delta= (b*b-(4*a*c))

#To finding Roots of equation
root1 = (-b+(cmath.sqrt(delta)))/(2*a)
root2 = (-b-(cmath.sqrt(delta)))/(2*a)

#Getting the vale of roots
print("Root1 of x is : ",root1)
print("Root2 of x is : ",root2)