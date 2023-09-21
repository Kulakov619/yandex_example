# Конструкции оператора IF
a = input()
if a > 2:
    print('Больше 2')
elif a == 2:
    print('Равно 2')
else:
    print('Меньше 2')
print('__________________________')

b = input()
if a > 10 and b < 5:
    print('a > 10 И b < 5')
if a > 10 or b < 5:
    print('a > 10 ИЛИ b < 5')
print('__________________________')

a = []
if not a:
    print('пустой список')
a = {}
if not a:
    print('пустой словарь')
a = True
if not a:
    print('a = True')
print('__________________________')

a = 'fjsjdkfnsd'
if 'f' in a:
    print('символ f есть в строке')

a = 'ds'
b = 'as'
print(a + 'sdaf' + b)


print ('Привет Яндекс!')