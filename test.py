a = input()
b = input()
c = input()
x = a + b + c
if 'лимон' not in a and 'Лимон' not in a:
    x = a
if 'лимон' not in b and 'Лимон' not in b and len(b) <= len(x):
    if len(b) == len(x):
        if b > x:
            x = b
    else:
        x = b
if 'лимон' not in c and 'Лимон' not in c and len(c) <= len(x):
    if len(c) == len(x):
        if c > x:
            x = c
    else:
        x = c
print(len(x), x)
