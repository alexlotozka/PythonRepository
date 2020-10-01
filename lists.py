from random import randint

"""
n = int(input())
a = [i for i in range(n)]
print(a)
#Створення списку
a = [i for i in range(10)]

a = [1, 2, 3, 4, 5, 6, 7]
b = list(map(lambda x: x**2, a))
print('a = {}\nb = {}'.format(a, b))

# Получить копию списка
a[:]
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# Получить первые пять элементов списка
a[0:5]
[0, 1, 2, 3, 4]

# Получить элементы с 3-го по 7-ой
a[2:7]
[2, 3, 4, 5, 6]

# Взять из списка элементы с шагом 2
a[::2]
[0, 2, 4, 6, 8]

# Взять из списка элементы со 2-го по 8-ой с шагом 2
a[1:8:2]
[1, 3, 5, 7]
#Можемо робити слайси за допомогою фyнкції slice
a = [i for i in range(10)]
s = slice(0,7,1)
print(a[s])"""
# A: Парні індекси
# Виведіть всі елементи списку з парними індексами (тобто A[0], A[2], A[4], ...).
# У цьому завданні не можна використовувати інструкцію if.
a = [i for i in range(10)]
print(a[0::2])

# B: Парні елементи
# Виведіть всі парні елементи списку.
a = [1, 2, 2, 3, 3, 3, 4]
b = list(filter(lambda x: x % 2 == 0, a))
print(b)

""" C: Більше попереднього
# Задано список чисел. Виведіть всі елементи списку, які більше попереднього
# елемента.
a = [1, 5, 6, 4, 3]
z = 0
counter = 0
# a = [int(i) for i in input().split()]
while counter < len(a):
    z = a[counter]
    counter += 1
    if a[counter] > z:
        print(a[counter], end=" ")"""
a = [1, 2, 3, 2, 1]
z = 0
for i in range(1, len(a) - 1):
    if a[i - 1] < a[i] > a[i + 1]:
        z += 1
print(f"There are {z} numbers which are bigger than their neighbours")


# D: Перший додатний
# Виведіть індекс першого додатного елементу в даному списку. Він обов’язково є в списку.
# У цьому завданні не можна користуватися інструкцією if. Елементи списку
# потрібно переглядати з початку до знаходження потрібного елемента.
def pershyy_dodatnyy():
    a = [randint(-10, 10) for i in range(10)]
    print(a)
    dopsht2 = 0
    for i in a:
        if i > 0:
            dopsht2 = i
            break
    return f" First positve:{dopsht2}"


print(pershyy_dodatnyy())


# E: Перший позитивний - 2
# Виведіть індекс першого додатного елементу в даному списку. Якщо такого
# елемента немає, програма повинна вивести число -1.
def pershyy_positive():
    a = [randint(-10, 10) for i in range(10)]
    print(a)
    dopshtuka2 = 0
    for i in a:
        if i > 0:
            dopshtuka2 = i
            break
        else:
            dopshtuka2 = -1

    return f" First positve or -1: {dopshtuka2}"


print(pershyy_positive())


# F: Найбільший елемент
# Задано список чисел. Виведіть значення найбільшого елементу в списку, а потім
# індекс цього елемента в списку. Якщо найбільших елементів декілька, виведіть
# індекс першого з них. Гарантується, що в списку є хоча б один елемент.
def naibilshy_dodatnyy():
    a = [randint(-10, 10) for i in range(10)]
    print(a)
    dopomizhnastuka1 = 0
    for i in a:
        if i > 0:
            if dopomizhnastuka1 < i:
                dopomizhnastuka1 = i

    return f" The biggest positve is {dopomizhnastuka1}. The index of the biggest positive is {a.index(dopomizhnastuka1)}"


print(naibilshy_dodatnyy())

# G: Більше своїх сусідів
# Задано список чисел. Визначте, скільки в цьому списку елементів, які більше
# двох своїх сусідів і виведіть кількість таких елементів.
a = [1, 2, 3, 2, 1]
z = 0
for i in range(1, len(a) - 1):
    if a[i - 1] < a[i] > a[i + 1]:
        z += 1
print(f"There are {z} numbers which are bigger than their neighbours")


# H: Найменший додатний
# Виведіть значення найменшого з усіх додатних елементів в списку. Відомо, що
# в списку є хоча б один додатній елемент, а значення всіх елементів списку по
# модулю не перевищує 1000.

def naimenshy_dodatnyy():
    a = [randint(-10, 10) for i in range(10)]
    print(a)
    dopomizhnastuka = 1000
    for i in a:
        if i > 0:
            if dopomizhnastuka > i:
                dopomizhnastuka = i

    return f" The smallest positve:{dopomizhnastuka}"


print(naimenshy_dodatnyy())
# I - найближче число
a = [10, 15, 25, 30, 150, 250]
target = 28
print(f"Найблжче число - {min(enumerate(a), key=lambda x: (abs(x[1] - target), x[0]))[1]}")

# J - шеренга
a = [165, 163, 162, 161, 157, 157, 155, 154]
target1 = 160
a.append(target1)
a.sort()
print(f"Номер Андрія в шерензі - {a.index(target1)}")

# K - кількість різних елементів
a = [1, 5, 7, 2, 5, 7, 4, 10]
unique = []
counter = 0
for i in a:
    if i not in unique:
        unique.append(i)
        counter += 1
print(f"Кількість номерів, які не повторюються - {len(unique)}")

# L - найменший непарний
a = [i for i in range(10)]
b = []
z = 0
for i in range(len(a)):
    if i % 2 != 0:
        b.append(i)
print(f"Список непарних елементів {b}")
if len(b) > 0:
    z = min(b)
    print(f"Найменший непарний - {z}")
else:
    print(f"0")

# M - переставити в зворотньому напрямку
print(' '.join(input("Введіть числа для списку: ").split()[::-1]))
# на початку ми з'єднуємо пробелом, щоб при виводі
# числа не злиплись, ми вводимо числа, розділяємо і переставляємо в звортньому напрямку


# N - переставити сусідні
a = [i for i in range(10)]
for i in range(1, len(a), 2):
    a[i - 1], a[i] = a[i], a[i - 1]
print(' '.join([str(i) for i in a]))

# O - переставити мін і мах
a = [i for i in range(10)]
q = min(a)
x = max(a)
for i in range(1, len(a)):
    a[q], a[x] = a[x], a[q]
print(f"Перестановка min і max: {' '.join([str(i) for i in a])}")


# R: Кількість співпадаючих пар
# Дан список чисел. Порахуйте, скільки в ньому пар елементів, рівних один
# одному. Вважається, що будь-які два елементи, рівні один одному утворюють
# одну пару, яку необхідно порахувати.
def spivpadajuchi_pary():
    array = [randint(1, 9) for i in range(5)]
    print(array)
    for i in array:
        if array.count(i) == 1:
            print(i)


print(spivpadajuchi_pary())


# V: Унікальні елементи
# Дан список. Виведіть ті його елементи, які зустрічаються в списку тільки один
# раз. Елементи потрібно виводити в тому порядку, в якому вони зустрічаються в
# списку.
# У цьому завданні не можна модифікувати список, використовувати допоміжні
# списки, рядки, зрізи.

def uniqueunique():
    a = [randint(-10, 10) for i in range(10)]
    print(a)
    for i in a:
        if a.count(i) == 1:
            print(f" This element {i} is unique")


print(uniqueunique())
