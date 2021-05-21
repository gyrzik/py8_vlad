r = open('read.txt', 'r')
w = open('write.txt', 'w')
a = r.readlines()[:1]
b = [int(x) for line in a for x in line.split()]

[fizz, buzz, num] = b

for i in range(1, num):

    if i % (fizz and buzz) == 0:
        w.write('FB ')
    elif i % fizz == 0:
        w.write('F ')
    elif i % buzz == 0:
        w.write('B ')       
    else:
        w.write(str(i) + (' '))
w.close()
r.close()