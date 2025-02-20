import math

def add(a,b):
    ### adds two numbers
    res = a+b
    return res

def multiply(a,b):
    ### multiplies two numbers

    res = a * b
    return res

def sqrt(a):
    ### calculates the square root of a number using built in math function
    
    res = math.sqrt(a)
    return res
    
if(__name__ == "__main__"):
    print("You are into utils.py")
    result = add(10, 20)
    print(result)


