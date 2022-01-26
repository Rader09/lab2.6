#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from datetime import date
import sys


if __name__ == '__main__':
    school = {'1а': 20, '1б': 29, '2а': 17, '2б': 18,
              '3а': 27, '3б': 15, '4а': 22, '4б': 31,
              '5а': 16, '5б': 21, '6а': 24, '6б': 23}

    for i in range(1):
        school.update({input('Название изменяемого класса: '): int(
            input('Кол-во учеников изменяемого класса: '))})
        school.update({input('Название нового класса: '): int(
            input('Кол-во учеников нового класса: '))})
        del school[input('Название расформировываемого класса: ')]
        summa = sum(school[item] for item in school)
        print('Начальная школа:', school)
        print('Количество учеников в начальной школе:', summa)