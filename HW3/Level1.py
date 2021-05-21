# Каждый пишет сумму списка при помощи for и while

# l = [5, 6, 15, 2, 8]
# sum = 0
# for i in l:
#     sum += i
# print (sum)


# l = [5, 6, 15, 2, 8]
# i = 0
# sum = 0
# while i < len(l):
#     sum += l[i]
#     i += 1
# print(sum)

# Написать программу, которая выводит сама себя

# t = open ('Уровень 1.py')
# text = t.read()
# print(text)
# t.close()

#Написать программу, которая выводит саму себя задом наперед

# t = open('Уровень 1.py')
# text = t.read()
# for line in reversed(text):
#     print(line, end = '')
# t.close()

#Банкомат выдает сумму максимально возможными купюрами

# k = int(input())
# INF = 10 ** 10
# F = [10 ** 10] * (k + 1)
# A = [1000, 500, 200, 100, 50, 20, 10]
# F[0] = 0
# for k in range (1, k + 1):
#     for i in range(len(A)):
#         if k - A[i] >= 0 and F[k - A[i]] < F [k]:
#             F[k] = F [k - A[i]]
#     F[k] += 1
# Ans = []
# while k != 0:
#     for i in range(len(A)):
#         if k - A[i] >= 0 and F[k] == F [k - A[i]] + 1:
#             Ans.append(A[i])
#             k -= A[i]
# print(Ans)

#Банкомат выдает сумму мелкими, но не больше 10 штук каждой мелкой купюры

