# 1.  (5 баллов) Написать функцию div_by_5, принимающую 1 аргумент — число от 0 до 1000 (проверять входные данные не нужно), 
# и возвращающую True, если оно делится на 5 без остатка, и False - иначе.

def div_by_5(number):
    f = True
    for i in range(2, int(number)):
        if number % i == 0:
            f = False
    return(f)
number = int(input('Введите число! '))
print(div_by_5(number))



#     2. (15 баллов) Напишите функцию которая называется explore_list, которая принимает в качестве аргумента список из чисел 
# (проверять, что он состоит из чисел НЕ нужно) и возвращает словарь, у которого должна быть следующая структура:
# {
#     ‘less_that_15’: # список элементов, которые меньше 15,
#     ‘middle’: # средний элемент в списке по индексу (без сортировки),
#     ‘odd’: # список из всех нечетных элементов в списке,
#     ‘even’: # список из всех четных элементов в списке
# }

explore_list = [2, 25, 30, 50, 10, 100, 64, 28, 50]

def explore_list(less, middle, odd, even):

    for less in explore_list:
        if less < 15:
            return explore_list(less)
    
    if l == len(explore_list) / 2:
        middle = explore_list[l]

    odd = [i for i in explore_list if i % 2 == 0]
    even = [j for j in explore_list if j % 2]
    return(odd, even)

print(explore_list(less, middle, odd, even))

# 3. (20 баллов) Напишите функцию id_generator, которая должна сгенерировать набор числовых данных длиной в 16 символов 
# из целочисленных значений и вернуть в качестве строкового значения

from random import randint

def get_list(number: int) -> list:
    number_list = []
    for n in range(number):
        number_list.append(randint(1,100))
    return number_list

my_list = get_list(16)
print(my_list)

# 4. (15 баллов) Напишите функцию factorial, которая будет получать в качестве аргумента число и ВОЗВРАЩАТЬ факториал этого числа.

number = int(input('Enter a number'))

def factorial(number):
    
    if number == 0:
        return 1
    return factorial(number -1) * number
print(factorial(number))


# 5. (10 баллов) Создайте функцию, которая называется my_color, данная функция принимает в качестве аргумента строковое значение. 
# Полученное значение функция должна записать в файл, который будет называться my_color.txt. 
# (Каждая следующая запись должна перезаписывать предыдущие записи)


def my_color():

    file = open('my_color.txt', mode='w')
    list = []
    file.write(text)
    for i in list:
        file.write(i)
    file.close()

    return my_color()


# 6. (15 баллов) Создать функцию get_car, которая описывает автомобиль. 
# Данная функция принимает в себя два обязательных аргумента и далее ПРОИЗВОЛЬНЫЙ НАБОР ИМЕННОВАННЫХ АРГУМЕНТОВ **kwargs. 
# Обязательные аргументы это brand (марка машины) и year (год выпуска). 
# Далее из всех полученных аргументов функция должна построить словарь, 
# содержащий все свойства автомобиля, переданные в качестве аргументов

def get_car(brand, year, **kwargs):
    result = {
        'brand': brand,
        'year': year
    }
    for k, v in kwargs.items():
        result.update({k: v})
    return result
print(get_car('Honda', 2021, color='red', number=34353))


# 7. (20 баллов) Создать функцию maskify, которая заменяет все символы, кроме последних четырех, на «#».
#     Например
#     "4556364607935616”     -->     "############5616"
    #  "64607935616"          -->          "#######5616"
    #            "1"              -->    "1"
    #             "4321"              -->    "4321"

numbers =[4,5,5,6,3,6,4,6,0,7,9,3,5,6,1,6]

def maskify(num: str) -> str:
    res = ''
    len_num = len(num)
    if len_num < 4:
        return num
    else:
        for i in range(len_num-4):
            res += '#'
        res += num[-4:]
    return res
res = maskify('4556364607935616')
print(res)

