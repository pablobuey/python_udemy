
#inputs 
num1 = input("Enter a number:")
num2 = input("Enter a second number:")

#casting to int
num1 = int(num1)
num2 = int(num1)

#calculator
sum = num1 + num2
subs = num1 - num2
mult = num1 * num2
div = num1 / num2

#print
results = f"""
{num1} + {num2}  = {sum}.
{num1} - {num2}  = {subs}.
{num1} * {num2}  = {mult}.
{num1} / {num2}  = {div}.
"""

print(results)
