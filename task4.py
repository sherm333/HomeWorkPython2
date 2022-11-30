"""
Задайте список из N элементов, заполненных числами из промежутка [-N, N]. Найдите произведение элементов на указанных позициях. Позиции вводятся с клавиатуры.
"""

from random import randint


def lst(n):
    list = []
    for i in range(n):
        list.append(randint(-n, n))
    return list


n = int(input("Введите число N: "))

