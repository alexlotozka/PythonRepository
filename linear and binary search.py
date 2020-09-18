from random import randint
import math


def linear_search(listvpor, shukane):
    for item in listvpor:
        if item == shukane:
            return True


print(linear_search([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 5))

listnevpor = []
t = 0
while t < 10:
    r = randint(1, 60)
    listnevpor.append(r)
    t += 1
print(listnevpor)


def linear_unordered(listnevpor, shukane):
    for item in listnevpor:
        if item == shukane:
            return True


print(linear_unordered(listnevpor, 3))


def findmax1(listnevpor):
    for item in listnevpor:
        if item == max(listnevpor):
            return f"Max number in {listnevpor} is {max(listnevpor)}"


def findmax():
    max = listnevpor[0]
    min = listnevpor[0]
    for item in listnevpor:
        if max < item:
            max = item
        if min > item:
            min = item
    return f"Max number in {listnevpor} = {max} , Min number in {listnevpor} = {min}"


print(findmax())


def findmin1(listnevpor):
    for item in listnevpor:
        if item == min(listnevpor):
            return f"Min number in {listnevpor} is {min(listnevpor)}"


print(findmax1(listnevpor))
print(findmin1(listnevpor))



# def binary_search(shukane, listvpor):
#     left = -1
#     right = math.inf
#     while left < right - 1:
#         mid = (right + left) // 2
#         if shukane > listvpor[mid]:
#             left = mid
#         else:
#           right = mid
#         if left >= 0 and listvpor == shukane:
#             return left
#         else: return -1
#
# print(binary_search(6 , [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))


def bin_search(value):
    a = []
    for i in range(10):
        a.append(randint(1,20))
    a.sort()
    print(a)

    mid = len(a) // 2
    low = 0
    high = len(a) - 1

    while a[mid] != value and low <= high:
        if value > a[mid]:
            low = mid + 1
        else:
            high = mid - 1
        mid = (low + high) // 2

    if low > high:
        print("No value")
    else:
        print(f"The searched number`s index is = {mid}")


print(bin_search(5))