#1 Проверить, является ли введеное число четным.
print ('Введите число:') 
a = int(input())
if (a % 2 == 0):
    print('Четное число')
else:
    print('Нечетное число')

#2 Проверить, является ли число нечетным, делится ли на три и на пять одновременно, но так, чтобы не делиться на 10.
print ('Введите число:')
a = int(input())
if (a % 2 != 0 and a % 15 == 0):
    print('Нечетное число, делится на три и на пять одновременно,и не делится на 10.')
else:
    print('Число не соответствует условиям задания')

#3 Ввести число, вывести все его делители.
a = int(input("Введите целое число: "))
print("Результат:", end = " ")
for i in range(1, a, 1):
    if (a % i == 0):
        print(i, end = " ")

#4 Ввести число, вывести его разряды и их множители.
num = int(input())
for b in str(num):
    print (b, end = ' ')
list_simple = []
simple = 2
while num > 1:
    if num % simple == 0:
        list_simple.append(simple)
        num = num/simple
    else:
        simple += 1
print(list_simple)
