num1 = int(input("Введите первое число "))
num2 = int(input("Введите второе число "))
while num1 != 0 & num2 != 0:
    num1 = num2
    num2 = num1 % num2
print(num1)
