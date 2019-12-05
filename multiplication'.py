#to print the multiplication of the given number
n =int(input("Enter your Number: "))
def factorial(n):
    result = 1
    for i in range(1,n+1):
        result = result * i
   factorial(n)

print("the factorial result is ", result)