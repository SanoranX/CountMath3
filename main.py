import matplotlib.pyplot as plt
import math
import numpy as np


# Метод прямоугольников
# Разобьем отрезок на 4 равные части
def rectangle_method(x3, x2, x1, k, a, b, eps, n):
    # Вычисляем сумму средних
    sum_rect_mid = rect_mid(x3, x2, x1, k, a, b, n)
    # Вычисляем сумму левых
    sum_rect_left = rect_left(x3, x2, x1, k, a, b, n)
    # Вычисляем сумму правых
    sum_rect_right = rect_right(x3, x2, x1, k, a, b, n)
    n *= 2
    # Вычисляем всё те же суммы, только количество прямоугольников увеличиваем в 2 раза для того, чтобы проверить погрешность
    sum_rect_mid1 = rect_mid(x3, x2, x1, k, a, b, n)
    sum_rect_left1 = rect_left(x3, x2, x1, k, a, b, n)
    sum_rect_right1 = rect_right(x3, x2, x1, k, a, b, n)
    # Удваиваем количество шагов для получения большей точности и по модулю разности определяем, какая точность
    # Продолжаем вычислять пока не будет достигнута нужная точность
    while (abs(sum_rect_mid1 - sum_rect_mid) > eps and abs(sum_rect_left1 - sum_rect_left) > eps
           and abs(sum_rect_right1 - sum_rect_right) > eps):
        sum_rect_mid = sum_rect_mid1
        sum_rect_left = sum_rect_left1
        sum_rect_right = sum_rect_right1
        n *= 2
        sum_rect_mid1 = rect_mid(x3, x2, x1, k, a, b, n)
        sum_rect_left1 = rect_left(x3, x2, x1, k, a, b, n)
        sum_rect_right1 = rect_right(x3, x2, x1, k, a, b, n)
    answer = 'По методу центральных прямоугольников ответ: ' + str(
        rect_mid(x3, x2, x1, k, a, b, n)) + '. Получен за ' + str(int(n / 2)) + ' шагов.\n'
    answer += 'По методу левых прямоугольников ' + str(rect_left(x3, x2, x1, k, a, b, n)) + '. Получен за ' + str(
        int(n / 2)) + ' шагов.\n'
    answer += 'По методу правых прямоугольников ' + str(rect_right(x3, x2, x1, k, a, b, n)) + '. Получен за ' + str(
        int(n / 2)) + ' шагов.\n'
    return answer


# Сумма средних
def rect_mid(x3, x2, x1, k, a, b, n):
    # Вычисляем шаг разбиения H
    step = (b - a) / n
    summa = 0
    # вычисляем сумма средних
    for i in range(0, n):
        summa += f(a + step / 2, x3, x2, x1, k)
        a += step
    summa *= step
    return summa

# Сумма левых
def rect_left(x3, x2, x1, k, a, b, n):
    step = (b - a) / n
    summa = 0
    for i in range(0, n):
        summa += f(a, x3, x2, x1, k)
        a += step
    summa *= step
    return summa

# Сумма правых
def rect_right(x3, x2, x1, k, a, b, n):
    step = (b - a) / n
    a += step
    summa = 0
    for i in range(0, n):
        summa += f(a, x3, x2, x1, k)
        a += step
    summa *= step
    return summa

# Метод трапеций
def trapezoid_method(x3, x2, x1, k, a, b, eps, n):
    sum = trapezoid_function(x3, x2, x1, k, a, b, n)
    n *= 2
    n_sum = trapezoid_function(x3, x2, x1, k, a, b, n)
    # Добиваемся нужной точности
    while (abs(n_sum - sum) > eps):
        sum = n_sum
        n *= 2
        n_sum = trapezoid_function(x3, x2, x1, k, a, b, n)
    return 'По методу трапеций ответ: ' + str(sum) + '. Решено за ' + str(int(n / 2)) + ' шага.'


def trapezoid_function(x3, x2, x1, k, a, b, n):
    # Вычисляем шаг (длину каждой трапеции)
    step = (b - a) / n
    # x0 = a
    # xn = b
    sum = 0
    # Вычисляем по формуле из отчета
    for i in range(0, n):
        y0 = f(a, x3, x2, x1, k)
        a += step
        yn = f(a, x3, x2, x1, k)
        sum += step * (y0 + yn) / 2
    return sum

# Метод симпсона
def simpson_method(x3, x2, x1, k, a, b, eps, n):
    sum = func3_realisation(x3, x2, x1, k, a, b, n)
    n *= 2
    n_sum = func3_realisation(x3, x2, x1, k, a, b, n)
    while (abs(n_sum - sum) > eps):
        sum = n_sum
        n *= 2
        n_sum = func3_realisation(x3, x2, x1, k, a, b, n)
    return 'Ответ: ' + str(sum) + '. Решено за ' + str(int(n / 2)) + ' шага.'


def func3_realisation(x3, x2, x1, k, a, b, n):
    # Вычисляем шаг
    step = (b - a) / n
    x0 = f(a, x3, x2, x1, k)
    a += step
    xn = f(b, x3, x2, x1, k)
    sum_1 = 0
    sum_2 = 0
    for i in range(1, n):
        if (i % 2 == 0):
            sum_2 += f(a, x3, x2, x1, k)
        else:
            sum_1 += f(a, x3, x2, x1, k)
        a += step
    answer = step * (x0 + xn + 2 * sum_2 + 4 * sum_1) / 3
    return answer


def f(x, x3, x2, x1, k):
    return x3 * pow(x, 3) + x2 * pow(x, 2) + x1 * x + k


def max_f2(x3, x2, a, b):
    return max((6 * x3 * a + 2 * x2), (6 * x3 * b + 2 * x2))


def printGraph(a, b):
    fig, ax = plt.subplots()
    x = np.linspace(a, b, 1000)
    y = f(x, x3, x2, x1, k)
    y1 = 0 * x
    ax.plot(x, y)
    ax.plot(x, y1)
    plt.show()


if __name__ == '__main__':

    n = 4

    answerGiven = True
    scannerline = True

    while scannerline:
        print('Ввод из файла/из строки (1/0): ')
        mes = input()
        if mes == '1':
            try:
                input_file = open('lol', 'r')
                x3, x2, x1, k = map(float, input_file.readline().split(' '))
                a, b = map(float, input_file.readline().split(' '))
                eps = float(input_file.readline())
                # n = int(pathh.readline())

                answerGiven = True
                scannerline = False
            finally:
                input_file.close()
        else:
            print('Коэффициент перед x^3: ')
            x3 = float(input())
            print('Коэффициент перед x^2: ')
            x2 = float(input())
            print('Коэффициент перед x^1: ')
            x1 = float(input())
            print('Свободный член: ')
            k = float(input())
            print('Левая граница приближения: ')
            a = float(input())
            print('Правая граница приближения: ')
            b = float(input())
            print('Погрешность: ')
            eps = float(input())
            # print('Начальное число разбиения')
            # n = int(input())
            answerGiven = True
            scannerline = False

    print('Выберите метод: \n' +
          '1. Метод прямоугольников \n' +
          '2. Метод трапеций \n' +
          '3. Метод Симпсона \n' +
          'Ваш ответ: ')
    answer = ''

    while answerGiven:
        give = input()
        if give == '1':
            printGraph(a, b)
            # n = max(round(math.sqrt(max_f2(x3,x2,a,b)*(b-a)**3/(24*eps)))+1,n)
            answer = rectangle_method(x3, x2, x1, k, a, b, eps, n)
            answerGiven = False
        elif give == '2':
            printGraph(a, b)
            # n = max(round(math.sqrt(max_f2(x3,x2,a,b)*(b-a)**3/(12*eps)))+1,n)
            answer = trapezoid_method(x3, x2, x1, k, a, b, eps, n)
            answerGiven = False
        elif give == '3':
            printGraph(a, b)
            # n = 4
            answer = simpson_method(x3, x2, x1, k, a, b, eps, n)
            answerGiven = False
        else:
            print('Ошибка: не тот номер \n' +
                  'попробуйте еще раз')
            continue

    print('Вывести в файл/консоль(1/0)')
    viv = input()
    if viv == '1':
        try:
            with open('output.txt', 'w') as file:
                file.writelines(answer)
        except:
            print("Ошибка: решений нет")
        finally:
            file.close()
    else:
        if (answer != 0):
            print(answer)
        else:
            print("Ошибка: решений нет")