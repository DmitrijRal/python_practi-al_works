# Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn. Например, пользователь ввёл число 3.
# Считаем 3 + 33 + 333 = 369.

n = input("Введите значине n: ")
nn = n+n
nnn = n+n+n
n=int(n)
nn=int(nn)
nnn=int(nnn)
n_sum = n+nn+nnn
print(n_sum)
