#  Задание 3- Задайте натуральное число N. 
# Напишите программу, которая составит список простых множителей числа N.
# Пример: при N = 12 -> [2, 3]
def is_prime(num):
    if num < 2:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False
    limit = int(num**0.5) + 1
    for divider in range(3, limit, 2):
        if num % divider == 0:
            return False
    return True


natural_n = int(input('Введите натуральное число N: '))
prime_list = []

for i in range(1, natural_n+1):
    if natural_n % i == 0 and is_prime(i):
        prime_list.append(i)

print(f'Список простых делителей {natural_n}:\n', prime_list, sep='')

#  Задание 1- Вычислить число c заданной точностью d. 
# Число Пи не просто обрезать с math.pi, а вычислить, используя формулы: 
# Нилаканта, ряды Тейлора, серию Ньютона или серию Чудновских.
# Пример:
# - при d = 0.001, π = 3.141.    10^(-10)≤ d ≤10^-

d = int(input('Введите точность: '))
calc_pi = 0
check = 0

for n in range(int(10000)):
    calc_pi += (1 / 16**n) * (4/(8*n + 1) - 2/(8*n + 4) - 1/(8*n + 5) - 1/(8*n + 6))
    if abs(check - calc_pi) < 10**(-d):
        break
    check = calc_pi

print('pi = ', round(calc_pi, d))




# - Задание 2 Задайте последовательность чисел. 
# Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности. 
# Посмотрели, что такое множество? Вот здесь его не используйте.

import random as rnd


def generate_lst(size: int) -> list:
    rnd_lst = []
    for _ in range(size):
        nmb = round(-10 + 20 * rnd.random(), rnd.randint(0, 2))
        if 0.3 > rnd.random():
            nmb = int(nmb)
        if 0.3 > rnd.random():
            nmb = str(nmb)
        rnd_lst.append(nmb)

    return rnd_lst


some_list = generate_lst(20)

unique_list = []

for item in some_list:
    if some_list.count(item) == 1:
        unique_list.append(item)

print(f'Неповторяющиеся элементы ({len(unique_list)} шт.):', unique_list)



# 4- В текстовом файле удалить все слова, которые содержат хотя бы одну цифру.
# В файле содержится, например:
# Мама сшила м0не штаны и7з бере9зовой кор45ы 893. -> Мама сшила штаны.

my_file = open("data.txt", "w+")
my_file.write("Мама сшила м9не штаны и8з бере0зовой ко34ры 99., ")
my_file.close()

with open('data.txt', encoding='utf-8') as file:
    data = list(map(str.strip, file.readlines()))

for l in range(len(data)):
    newline = data[l].split()
    for i in range(len(newline)-1, -1, -1):
        for c in newline[i]:
            if c.isdigit():
                del newline[i]
                break
    data[l] = ' '.join(newline)
        
with open('data.txt', 'w', encoding='utf-8') as file:
    for line in data:
        print(line, file = file)

print('File has been changed!')
