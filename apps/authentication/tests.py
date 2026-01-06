from django.test import TestCase


def calculator(a, b, operator):
    match operator:
        case '+':
            return a + b
        case '-':
            return a - b
        case '*':
            return a * b
        case '/':
            return a / b
        case _:
            raise ValueError("Xatol topshiriq")
        
a = int(input("Birinchi sonni kiriting: "))
b = int(input("Ikkinchi sonni kiriting: "))
operator = input("Amalni kiriting (+, -, *, /): ")
print("Natija:", calculator(a, b, operator))