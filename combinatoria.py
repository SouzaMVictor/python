# quantos numeros de 4 dígitos eu posso formar com numeros de 0 a 9?

# count = 0
# for n1 in range (10):
#     for n2 in range (10):
#         for n3 in range (10):
#             for n4 in range(10):
#                 count += 1
# print(count)

#  _  _  _  _
# 10 10 10 10
# combinatoria = 10x10x10x10 =  10000


#  _  _  _  _
# 10  9  8  7
# permutação  : 10x9x8x7 = 5040

# simulação: executar as possibilidades
# -- exeplo de codigo ali em cima


count = 0
for n1 in range (10):
    for n2 in range (10):
        if n2 == n1:
            continue
        for n3 in range (10):
            if n3 == n1 or n3 == n2:
                continue
            for n4 in range(10):
                if n4 == n1 or n4 == n2 or n4 == n3:
                    continue
                count += 1
print(count)
