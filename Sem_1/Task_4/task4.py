# Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек, 
# если разрешается сделать один разлом по прямой между дольками 
# (то есть разломить шоколадку на два прямоугольника). Числа вводятся построчно.

# *Пример:*

# 3 2 4 -> yes
# 3 2 1 -> no
n = int(input('Ширина в дольках: '))
m = int(input('Длинна в дольках: '))
k = int(input('Желаемое количество долек за один разлом: '))