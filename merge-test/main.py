from utils import add, multiply, sqrt

def main():
    result = multiply(80.5,33)
    print("The result of multiplication is",result)
    
    print("You are on feature a branch")
    a = 10
    b = 50
    result = add(a,b)
    print("The result of the addition is", result)

    n=144
    result = sqrt(n)
    print("The square root of 144 =",result)

main()