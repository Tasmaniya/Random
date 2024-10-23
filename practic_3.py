'''
print("Number 1")
import random

numbers = [random.randint(-10,10) for _ in range(5)]
print(numbers)

for i in range(len(numbers)):
    numbers[i] = numbers[i]**2
print(numbers)
'''


'''
import random
print("Number 2")

numbers = [random.randint(-10,10) for _ in range(15)]
print(numbers)

proverka = []

for i in numbers:
    if numbers.count(i) > 1:
        if i not in proverka:
            proverka.append(i)
print(proverka)
'''



'''
import random
print("Number 3")

numbers = [random.randint(-10,10) for _ in range(15)]
print(numbers)

numbers_2 = [random.randint(-10,10) for _ in range(15)]
print(numbers_2)

numbers_3 = []

for i in numbers_2:
    if i not in numbers:
        numbers_3.append(i)
print(numbers_3)
'''


'''
import random
print("Number 4")

numbers = [random.randint(18,20) for _ in range(10)]
print(numbers)

for i in range(len(numbers)):
    if numbers[i] == 20:
        numbers[i] = 200
print(numbers)
'''


'''
import random
print("Number 5")

numbers = [random.randint(15,20) for _ in range(10)]
print(numbers)

numbers_1 = []

for i in numbers:
    if i == 15:
        break
    elif i % 2 == 0:
        numbers_1.append(i)
print(numbers_1)
'''


'''

negative, zero, positive = [], [], []

while True:
    num = input("Введите целое число: ")
    if num == '':
        break
    elif float(num) % 1 == 0:
        if float(num) < 0:
            negative.append(num)
        elif float(num) == 0:
            zero.append(num)
        else:
            positive.append(num)
    else:
        print("Некорректно введено число, введите целое число")

for i in negative:
    print(i)

for i in zero:
    print(i)

for i in positive:
    print(i)
'''
