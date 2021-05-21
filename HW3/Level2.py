r = open('read.txt', 'r')
a = r.readlines()[:1]
b = []
for line in a:
    for x in line.split():
        b.append(int(x))

[fizz, buzz, num] = b

for i in range(1, num):

    if i % fizz == 0 and i % buzz == 0:
        print('FB', end=' ')
    elif i % fizz == 0:
        print('F', end=' ')
    elif i % buzz == 0:
        print('B', end=' ')
    else:
        print(i, end=' ')
r.close()