a = int(input())
n = 1
s = ''
for i in range(a):
    for j in range(a):
        if j == 0:
            s = str(n)
        else:
            s = s + '\t' + str(n)
        n = n + 1
    print(s)
    s = ''


a = int(input())
b = int(input())
c = int(input())
for i in range(a, b + 1, c):
    for j in range(a, b + 1, c):
        print(i, '+', j, '=', i + j, end='\t')
    print()
