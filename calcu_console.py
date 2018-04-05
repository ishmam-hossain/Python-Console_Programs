### Ishmam Hossain
### 1st March 2018

import math


# ---------- Functions ---------------------------

# ------------- input function----------------
def take_two_inputs():
    """
    takes two input and 
    returns these two numbers 
    """
    try:
        num1 = int(input("Enter First number: ").strip())
        num2 = int(input("Enter Second number: ").strip())      
    
    except (TypeError, ValueError):
        pass
    
    else:
        return num1, num2
        
    
    
# ------------ Arithmetic functions-------------


def addition(num1, num2):
    """
    takes two input and returns the sum
    """
    return num1 + num2


def subtract(num1, num2):
    """
    takes two input and returns the difference
    """
    return num1 - num2


def multiply(num1, num2):
    """
    takes two input and returns the product
    """
    return num1 * num2


def divide(num1, num2):
    """
    takes two input and returns the division
    """
    if num2 != 0:
        return num1 / num2
    else:
        return "Invalid divisor!!"


def to_the_power(num1, num2):
    """
    takes two input and returns the exponential
    """
    return num1 ** num2

def modulo(num1, num2):
    """
    takes two input and returns the remainder
    """
    return num1 % num2


def cal_fact(n):
    """
    takes one input and returns the factorial
    """
    
    if n == 0:
        return 1
    else:
        return n * cal_fact(n - 1)
    
def percentage(num1, num2):
    """
    takes in two numbers and returns the percentage
    """    
    return (num1 * num2) / 100
    

def calc_polynomials(ar):
    
    """
    takes in an array of numbers
    returns the polynomial solution
    """
    sum_of = 0
    
    for i in range(len(ar)):
        
        sum_of += (ar[i] ** i)
            
    return sum_of


def square_root(n):
    """
    takes a value and returns the square root
    """
    return math.sqrt(n)
    
    
    


# ------------- Code starts here !! -----------------------

show_first = "Choose operation-\na for addition\ns for subtraction\n\
m for multiplication\nd for for division\n\
r for raising to power\nmd for modulo operation\n\
f for factorial\nprcnt for percentage\npol for polynomial\n\
root for Square Root\n"

print(show_first)

op = input("\n**Enter an operation: ").strip().lower()

if op == 'a':
    
    try:
        num1, num2 = take_two_inputs();
        res = addition(num1, num2)    
        print("Answer is: " + str(res))
    
    except (TypeError, ValueError):
        print("Invalid Input!")
        

elif op == 's':
    
    try:    
        num1, num2 = take_two_inputs();
        res = subtract(num1, num2)    
        print("Answer is: " + str(res))
    
    except (TypeError, ValueError):
        print("Invalid Input!")
        
        
elif op == 'm':
    
    try:
        num1, num2 = take_two_inputs();
        res = multiply(num1, num2)    
        print("Answer is: " + str(res))
    
    except (TypeError, ValueError):
        print("Invalid Input!")


elif op == 'd':
    
    try:
        num1, num2 = take_two_inputs();
        res = divide(num1, num2)    
        print("Answer is: " + str(res))
    
    except (TypeError, ValueError):
        print("Invalid Input!")


elif op == 'r':
    
    try:
        print('Enter Base & Power respectively-')
        num1, num2 = take_two_inputs();
        res = to_the_power(num1, num2)    
        print("Answer is: " + str(res))
    
    except (TypeError, ValueError):
        print("Invalid Input!")


elif op == 'md':
    
    try:
        num1, num2 = take_two_inputs();
        res = modulo(num1, num2)    
        print("Answer is: " + str(res))
    
    except (TypeError, ValueError):
        print("Invalid Input!")


elif op == 'f':
    
    try:
        n = int(input().strip())
        res = cal_fact(n)
        print("Answer is: " + str(res))
    
    except (TypeError, ValueError):
        print("Invalid Input!!")
    

elif op == 'prcnt':
    try:
        num1, num2 = take_two_inputs();
        res = percentage(num1, num2)    
        print("Answer is: " + str(res))   
        
    except (TypeError, ValueError):
        print("Invalid Input!")
        
        
elif op == 'pol':
    
    print("Enter max power of the polynomial: ", end = " ")

    try:
        max_pow = int(input())
        print("Enter the variables from low to high order: ", end = " ")
        ar = list(map(int, input().strip().split(' ')))
        res = calc_polynomials(ar)
        print("Answer is: "+ str(res))
    
            
    except (TypeError, ValueError):
        pass
       
    
elif op == 'root':
    try:
        n = int(input().strip())
        res = square_root(n)
        print("Answer is: " + str(res))
    
    except (TypeError, ValueError):
        print("Invalid Input!!")
    
    
else:
    print("Invalid Choice of operation!") 






