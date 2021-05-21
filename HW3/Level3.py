r = open('read.txt', 'r')
w = open('write.txt', 'w')
a = r.readlines()[:1]
b = []
for line in a:
    for x in line.split():
        b.append(int(x))

[fizz, buzz, num] = b


for i in range(1, num):

    if i % fizz == 0 and i % buzz == 0:
        w.write('FB ')
        print('FB', end=' ')
    elif i % fizz == 0:
        w.write('F ')
        print('F', end=' ')
    elif i % buzz == 0:
        w.write('B ')
        print('B', end=' ')
    else:
        print(i, end=' ')
        w.write(str(i) + (' '))
w.close()
r.close()