# 1.Write a Python program to calculate the area of a
# rectangle given its length and width 

# 2. Create a program that takes a user's name and age as
# input and prints a greeting message

# 3.Write a program to check if a number is even or odd+

# 4.Given a list of numbers, find the maximum and minimum
# values+

# 5.Create a Python function to check if a given string is a
# palindrome+

# 6.Calculate the compound interest for a given principal
# amount, interest rate, and time period+

# 7.Write a program that converts a given number of days
# into years, weeks, and days+

# 8.Given a list of integers, find the sum of all positive
# numbers+

# 9.Create a program that takes a sentence as input and
# counts the number of words in it+

# 10.Implement a program that swaps the values of two
# variables

l = input("Enter the length of a rectangle: ")
b = input("Enter the width of a rectange: ")

l = float(l)
b = float(b)

if l == l:
    print(l * b)
    
# ---------------------------------------------------

name = input("Enter your name: ")
age = input("Enter your age: ")
age = int(age)
print(f"Hi {name} How are you? ")

# ---------------------------------------------------

num  = input("Enter your number: ")
num = int(num)
if num%2 :
    print("This is Even number")
else:
    print("This is odd number")
    
# ---------------------------------------------------
x = [1,2,3,4,5,6,7,8,9,10]
print(min(x))
print(max(x))

# ---------------------------------------------------
print("Atharv")