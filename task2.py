#! python3
# Have the user input a number 
# Determine if the number is positive, negative or 0 
# 2 points

# Inputs:
# number

# Outputs:
# - "positive"
# - "negative"
# - "zero"
x = int(input(""))

if x > 0:
    print("positive")
elif x == 0:
    print("zero")
else:
    print("negative")