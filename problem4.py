#! python3
# Have the user enter in 3 numerical values, representing the side lengths of a triangle. 
# Determine if the values are close enough to make a right triangle. 
# Note: You will need to decide which length is the possibly hypotenuse as the numbers
# are being entered in a random order.
# It is close enough if the expected length of the hypotenuse and the actual length 
# differ by no more than 2% 
# (2 marks)

# Inputs:
# - 3 numbers, in any order

# Outputs:
# - "that is a right triangle"
# - "that is an acute triangle"
# - "that is an obtuse triangle"
import math

x = float(input(""))
y = float(input(""))
z = float(input(""))

if x > y and x > z:
    hypotenuse = x
    side1 = y
    side2 = z
elif y > x and y > z:
    hypotenuse = y
    side1 = x
    side2 = z
elif z > x and z > y:
    hypotenuse = z
    side1 = x
    side2 = y
elif x == y == z:
    hypotenuse = 0
    side1 = 0
    side2 = 0
    print("that is an acute triangle")

step1 = side1**2 + side2**2
real_hyp = math.sqrt(step1)

if side1**2 + side2**2 == hypotenuse**2 and (hypotenuse - real_hyp > 0.02*hypotenuse or hypotenuse - real_hyp < -0.02*hypotenuse):
    print("that is a right triangle")
elif side1**2 + side2**2 > hypotenuse**2:
    print("that is an acute triangle")
elif side1**2 + side2**2 < hypotenuse**2:
    print("that is an obtuse triangle")
