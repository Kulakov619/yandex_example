a = int(input())
b = int(input())
if ((a % 2 == 0 and b % 2 == 0) or (a % 2 != 0 and b % 2 != 0)) and b % a == 0:
    print('Экзамен сдан!')
elif a % 10 == b % 10:
    print('Неплохо!')
else:
    print('В море не выходить.')

# _______________________________________________________________________________
a = input()
while a != '':
    if len(a) <= 20 and ('спаси' in a or 'Спаси' in a or 'помоги' in a or 'Помоги' in a):
        print('На помощь!')
    elif len(a) <= 20 or ('спаси' in a or 'Спаси' in a or 'помоги' in a or 'Помоги' in a):
        print('Подойти поближе.')
    else:
        print('Мимо.')
    a = input()

# _______________________________________________________________________________
a = int(input())
b = int(input())
c = int(input())
mn = min(a, b, c)
mx = max(a, b, c)
step = (a + b + c) - (mn + mx)
for i in range(mx, mn - 1, -step):
    if i % 2 != 0:
        print(2 * i + 1, end=' ')
    else:
        print(i - 1, end=' ')

# _______________________________________________________________________________
a = int(input())
mx = False
mn = False
for i in range(a):
    b = int(input())
    summ = 0
    n = 0
    for j in range(b):
        c = int(input())
        summ += c
        n += 1
    print(int(summ / n) * '*')
    if not mx:
        mx = int(summ / n)
    if not mn:
        mn = int(summ / n)
    if int(summ / n) > mx:
        mx = int(summ/n)
    if int(summ / n) < mn:
        mn = int(summ / n)
print(mn, mx)