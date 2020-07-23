#!/usr/bin/env python
# -*- coding: utf-8 -*-

def regressiva(value):
    print value
    if value <= 1:
        return
    else:
        regressiva(value - 1)

def fatorial_number(value):
    if value == 0:
        return 1
    else:
        return value * fatorial_number(value -  1)


regressiva(10)
fatorial = fatorial_number(5)
print("fatorial é {} ".format(fatorial))