#!/usr/bin/env python
# -*- coding: utf-8 -*-


def find_log(total,base):
    log = base
    cont = 0
    while log <= total:
        log = log * base
        cont = cont + 1

    return cont 


log = find_log(1000000000,2)

print " log é {} ".format(log)