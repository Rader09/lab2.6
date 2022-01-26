#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from datetime import date
import sys


if __name__ == '__main__':
    slovar1 = {1: 'alpha', 2: 'delta', 3: 'bravo', 4: 'foxtrot'}
    slovar2 = slovar1.items()
    reverb = {r: element for element, r in slovar2}
    print(reverb)