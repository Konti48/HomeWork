n = int (input('Введите число: '))
sum = 0
while n >= 1:
    sum += n % 10
    n = n // 10
print (f"Сумма цифр введённого числа равна: {sum}")