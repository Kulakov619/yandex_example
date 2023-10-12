a = input()
b = input()
c = input()

d = a + b + c

if 'лимон' not in a and 'Лимон' not in a:
    d = a
if 'лимон' not in b and 'Лимон' not in b:
    if len(b) < len(d):
        d = b
    elif len(b) == len(d):
        if b >= d:
            d = b
if 'лимон' not in c and 'Лимон' not in c:
    if len(c) < len(d):
        d = c
    elif len(c) == len(d):
        if c >= d:
            d = c

if d != a + b + c:
    print(len(d), d)
