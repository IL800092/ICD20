'''fname = str(input("Please enter your fist name:"))
lname = str.upper(input("Please enter you last name: "))

print(f"{fname} {lname}")

num1 = int(input("Please enter a number: "))
num2 = int(input("Please enter another number"))

print(num1 + num2) #add
print(num1 - num2) #subtract
print(num1 * num2) #multiply
print(num1 / num2) #divide
print(round(num1/num2)) #rounds
print(round(num1//num2)) #// rounds down
print(num1**num2) #exponent
print(num1%num2)#divide and find remainder'''

n = float(input("Enter an amount of money: $"))

toonies = n//2
remainder = n%2
print(remainder)
loonies = remainder//1
remainder = n%1
print(remainder)
quarters = remainder//0.25
remainder = n%0.25
print(remainder)
dimes = remainder//0.10
remainder = n%0.10
print(remainder)
nickle = remainder//0.05
remainder = n%0.05
print(remainder)
pennies = remainder//0.01

print(f"There are {toonies} toonies {loonies} loonies {quarters} quarters {dimes} dimes {nickle} nickles")