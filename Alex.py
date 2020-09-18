import math
from random import randint

"""Більшість завдань робила сама, але деякі робила з Максом."""

""" 4.22. Дано натуральное число. Определить:
 а) является ли оно четным;
 б) оканчивается ли оно цифрой 7. """
w = randint(1, 99)
divide = w % 2


def numb():
    if divide == 0:
        return f"Tshyslo {w} parne"
    else:
        return f"Tshyslo {w} ne parne"


firstd = w % 10


def simif():
    if firstd == 7:
        return f"Ending of number {w} is 7"
    else:
        return f"Ending of number {w} isn`t 7"


print(numb())
print(simif())

"""4.28. Дано трехзначное число. Определить, какая из его цифр больше:
а) первая или последняя;
б) первая или вторая;"""
e = randint(100, 999)
print(e)
first = e // 100
second = (e // 10) % 10
third = e % 10


def whatsbigger():
    if first > third:
        return f"First number {first} is bigger than third {third}"
    else:
        print(f"First number {first} is less than third {third}")
    if first > second:
        return f"First number {first} is bigger than second {second}"
    else:
        return f"First number {first} is less than second {second}"


print(whatsbigger())

"""4.30. Дано трехзначное число. Определить:
а) является ли сумма его цифр двузначным числом;
б) является ли произведение его цифр трехзначным числом;
в) больше ли числа а произведение его цифр;
г) кратна ли пяти сумма его цифр;
д) кратна ли сумма его цифр числу а."""
z = randint(100, 999)
first_num = z // 100
second_num = (z // 10) % 10
third_num = z % 10
sum = first_num + second_num + third_num
multip = first_num * second_num * third_num


def if_two_digit():
    if sum > 9 and sum < 100:
        return f"{sum} is a two-digit number!"
    else:
        return f"{sum} isn`t a two-digit number!"


def mult_of_numbers():
    if multip > 99 and multip < 1000:
        return f"Multiplication of {z}`s number = {multip}, and it`s a three-digit number"
    else:
        return f"Multiplication of {z}`s number = {multip}, and it isn`t a three-digit number"


def more_than(a):
    if multip > a:
        return f"{multip} is more than {a}"
    else:
        return f"{multip} is less than {a}"


def multiple_to_5():
    if sum % 5 == 0:
        return f"Sum of the numbers - {sum} is multiple to 5"
    else:
        return f"Sum of the numbers - {sum} isn`t multiple to 5"


def multiple_to_a(a):
    if sum % a == 0:
        return f"Sum of the numbers - {sum} is multiple to {a}"
    else:
        return f"Sum of the numbers - {sum} isn`t multiple to {a}"


print(if_two_digit())
print(mult_of_numbers())
print(more_than(50))
print(multiple_to_5())
print(multiple_to_a(4))

"""4.32. Дано четырехзначное число. Определить:
а) равна ли сумма двух первых его цифр сумме двух его последних цифр;
б) кратна ли трем сумма его цифр;
в) кратно ли четырем произведение его цифр;
г) кратно ли произведение его цифр числу а."""
q = randint(100, 999)
print(q)
first = q // 100
second = (q // 10) % 10
third = q % 10
sum = first + second + third
mult = first * second * third


def sumif():
    if sum > 9 and sum < 100:
        return f"Sum {sum} is 2-digit number"
    else:
        return f"Sum {sum} isn`t 2-digit number"


def multif():
    if mult > 99 and mult < 1000:
        return f"Mult {mult} is 3-digit number"
    else:
        return f"Mult {mult} isn`t 3-digit number"


def bigger():
    a = randint(1, 10)
    if mult > a:
        return f"Mult {mult} is bigger than {a}"
    else:
        return f"Mult {mult} isn`t bigger than {a}"


def kratneif():
    if sum % 5 == 0:
        return f"Sum {sum} kratne 5"
    else:
        return f"Sum {sum} ne kratne 5"


def kratneaif(a):
    if sum % a == 0:
        return f"Sum {sum} kratne {a}"
    else:
        return f"Sum {sum} ne kratne {a}"


print(sumif())
print(multif())
print(bigger())
print(kratneif())
print(kratneaif(3))

"""4.35.*Имеется стол прямоугольной формы с размерами
a b
(a и b — целые числа,a > b). В каком случае на столе можно разместить большее количество кар-
тонных прямоугольников с размерами c d (c и d — целые числа, c > d): при
размещении их длинной стороной вдоль длинной стороны стола или вдоль
короткой. Прямоугольники не должны лежать один на другом и не должны
свисать со стола."""


def how_better(a, b, c, d):
    # a,b - parameters of the table
    # c,d - parameters of the rectangles
    if a > b and c > d:
        z1 = (a // c) * (b // d)
        z2 = (a // d) * (b // c)
        print(f"{z1} - horizontally, {z2} - vertically")
        if z1 > z2:
            return f"If you place rectangles horizontally, you`ll place {z1} of them"
        else:
            return f"If you place rectangles vertically, you`ll place {z2} of them"
    else:
        return "Error. a must be bigger than b, c must be bigger than d"


print(how_better(6, 4, 3, 2))

"""Вася пытается высунуть голову в форточку размерами a и b см. Приняв ус-
ловно, что его голова — круглая диаметром d см, определить, сможет ли Вася
сделать это. Для прохождения головы в форточку необходим зазор в 1 см
с каждой стороны."""


def vasya_fortochka(a, b, d):
    # a,b - window`s parameters, d - diametr of the head, we also need 1 sm from each side
    if a - 1 >= d and b - 1 >= d:
        return "Window has enough space for Vasya to pull his head through."
    else:
        return "Window doesn`t have enough space for Vasya to pull his head through."


print(vasya_fortochka(5, 6, 4))

""" 4.61 Дано натуральное число n (n 9999). Выяснить, является ли оно палиндромом
("перевертышем") с учетом четырех цифр, как, например, числа 7777, 8338,

0330 и т. п. (Палиндромом называется число, десятичная запись которого чи-
тается одинаково слева направо и справа налево.)"""
n = randint(1, 9999)
firstnu = n // 1000
secondnu = (n // 100) % 10
thirdnu = (n // 10) % 10
fourthnu = (n % 100) % 10
print(n)
print(firstnu)
print(secondnu)
print(thirdnu)
print(fourthnu)


def palindrom():
    if firstnu == fourthnu and secondnu == thirdnu or firstnu == secondnu == thirdnu == fourthnu:
        return f" Number {n} is a palindrom"
    else:
        return f" Number {n} is not a palindrom"


print(palindrom())

"""Дано натуральное число n (n 9999). Выяснить, верно ли, что это число содержит ровно три одинаковые 
цифры с учетом четырех цифр, как, например, числа 3363, 4844, 0300 и т. п."""


def same3():
    z = randint(1000, 9999)
    f1 = z // 1000
    s2 = (z // 100) % 10
    t3 = (z // 10) % 10
    f4 = z % 10
    print(z)
    print(f1, s2, t3, f4)
    if (f1 == s2 and f1 == t3 or f1 == s2 and f1 == f4 or f1 == t3 and f1 == f4) \
            or (s2 == f1 and s2 == t3 or s2 == f1 and s2 == f4 or s2 == t3 and s2 == f4) \
            or (t3 == f1 and t3 == s2 or t3 == f1 and t3 == f4 or t3 == s2 and t3 == f4) \
            or (f4 == f1 and f4 == s2 or f4 == f1 and f4 == t3 or f4 == s2 and f4 == t3):
        return "There are three same digits in this number"
    else:
        return "This number doen`t contain three same numbers"


print(same3())

"""4.64 Определить, является ли заданное шестизначное число счастливым. (Счаст-
ливым называют такое шестизначное число, что сумма его первых трех цифр
равна сумме его последних трех цифр.)"""

a = randint(100000, 999999)
firstnum = a // 100000
secondnum = (a // 10000) % 10
thirdnum = (a // 1000) % 10
fourthnum = (a // 100) % 10
fifthnum = (a // 10) % 10
sixthnum = a % 10
print(a)
print(firstnum)
print(secondnum)
print(thirdnum)
print(fourthnum)
print(fifthnum)
print(sixthnum)


def luckynumber():
    sum1 = firstnum + secondnum + thirdnum
    sum2 = fourthnum + fifthnum + sixthnum
    print(f"Summ of the first three numbers is {sum1}")
    print(f"Summ of the last three numbers is {sum2}")
    if (sum1 == sum2):
        return f"This number is lucky"
    else:
        return f"This number isn`t lucky"


print(luckynumber())

"""4.96. Даны вещественные числа a, b, c. (a != 0) Выяснить, имеет ли уравнение ax^2 + bx + c = 0
вещественные корни. Если такие корни имеются, то найти их.
В противном случае ответом должно служить сообщение, что вещественных
корней нет."""


# a != 0, ax^2 + bx + c = 0
def equation(a, b, c):
    discr = pow(b, 2) - 4 * a * c
    x1 = (-b + pow(discr, 0.5)) / (2 * a)
    x2 = (-b - pow(discr, 0.5)) / (2 * a)
    print(x1, x2)
    if discr == 0:
        return f"Your equation has 1 solution: {x1}"
    elif discr > 0:
        return f"Your equation has 2 solutions: {x1}, {x2}"
    else:
        return "Your equation has no solution"


print(equation(1, 4, -21))

listnevpor = []
t = 0
while t < 10:
    r = randint(1, 10)
    listnevpor.append(r)
    t += 1
print(listnevpor)


def linear_unordered(listnevpor, shukane):
    for item in listnevpor:
        if item == shukane:
            return True


print(linear_unordered(listnevpor, 3))


def findmax(listnevpor):
    for item in listnevpor:
        if item == max(listnevpor):
            return f"Max number in {listnevpor} is {max(listnevpor)}"


def findmin(listnevpor, shukane):
    for item in listnevpor:
        if item == min(listnevpor):
            return f"Min number in {listnevpor} is {min(listnevpor)}"


print(findmax(listnevpor))
print(findmin(listnevpor))
