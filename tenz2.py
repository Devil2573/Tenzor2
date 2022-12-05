import math
#1
print("Введите два числа")
x=float(input())
y=float(input())
print("Сумма = ",x+y)
print("Вычитание = ",x-y)
print("Умножение = ",x*y)
print("Деление = ",x/y)
print("x в степени y = ",x**y)
print("Деление по модулю = ",x % y)
print("Целочисленное деление = ",x//y)
#2
print("Введите своё имя")
n=str(input())
print("Здравствуйте ",n)
#3
print("Введите строку")
s=str(input())
print("Последние два символа наоборот ",s[:-3:-1])
#4
print("Введите радиус круга ")
r=int(input())
print("Площадь круга = ",math.pi*r**2)
