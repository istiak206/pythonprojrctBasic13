#Declaration

def summation():
    number1 = 10
    number2 = 5
    result = number1 + number2
    print("Summation result is:" , result)

    #Calling
summation()

def substraction():
    number1 = 10
    number2 = 5
    result = number1 - number2
    print("Substraction result is:" , result)
substraction()

def multiplication():
    number1 = 10
    number2 = 5
    result = number1 * number2
    print("Multiplication result is:" , result)
multiplication()

def division():
    number1 = 10
    number2 = 5
    result = number1 / number2
    print("Division result is:" , result)
division()

#Function with argument

def subtract():
    number1 = int(input("Number1: "))
    number2 = int(input("Number2: "))
    result=number1 - number2
    print (result)

subtract()

#1 usage
def multiply(a, b):
    return a * b
print(multiply(10,2))