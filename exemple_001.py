# with open('file.txt', 'a') as data:
#     data.write('line 1111\n')
#     data.write('line 2222\n')


# colors = ['red', 'green', 'blue']
# data = open('file.txt', 'a')
# # data.writelines(colors) # разделителей не будет
# data.write('\nLINE 12\n')
# data.write('LINE 13')
# data.close

# exit()

# path = 'file.txt'
# data = open(path, 'r')
# for line in data:
#     print(line)
# data.close()

# import hello
# print(hello.f(1))

# или так

# import hello as h
# print(h.f(1))

# def new_string(symbol, count = 3):
#     return symbol * count

# print(new_string('!', 5))
# print(new_string('!'))
# print(new_string(4))

# def concatenatio(*params): 
#     res: str = ""
#     for item in params:
#         res += item
#     return res

# print(concatenatio('a', 's', 'd', 'w'))
# print(concatenatio('a', '1', 'd', '2'))
# # print(concatenatio('a', 's', 'd', 'w'))

#  рекурсия

# def fib(n):
#     if n in [1, 2]:
#         return 1
#     else:
#         return fib(n - 1) + fib(n - 2)

# list = []
# for e in range(1, 10):
#     list.append(fib(e))
# print(list)

# Словари

# alphabet = {}
# alphabet = \
#     {
#         'a': 'A',
#         'b': 'B',
#         'c': 'C'
#     }

# print(alphabet)
# print(alphabet['b'])

# for k in alphabet.keys():
#     print(k)

# for k in alphabet.values():
#     print(k)

# for v in alphabet:
#     print(alphabet[v])

# Множества

a = {1, 2, 3, 5, 8}
b = {2, 5, 8, 13, 21}
c = a.copy()  # c = {1, 2, 3, 5, 8}
u = a.union(b)  # u = {1, 2, 5, 8, 13, 21}
i = a.intersection(b) # i = {8, 2, 5}
dl = a.difference(b) # dl = {1, 3}
dr = a.difference(a)  # dr = {13, 21}
