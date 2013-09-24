#!/usr/bin/python
# -*- indent-tabs-mode: nil; tab-width: 4 -*-
# vi: et ts=4 sts=4 sw=4
import time

ITERATE_NUM = 23

def by_list(iter = ITERATE_NUM):
    array = ['s']
    for i in xrange(iter):
        array.extend(array)

# Here str is fast than list, as there's an optimization in CPython for '+='.
# Ref: 
# 1.http://stackoverflow.com/questions/18219718/python-buffer-copy-speed-why-is-array-slower-than-string
# 2.note 6 in http://stackoverflow.com/questions/18219718/python-buffer-copy-speed-why-is-array-slower-than-string
def by_str(iter = ITERATE_NUM):
    strings = 's'
    for i in xrange(iter):
        strings += strings

def main():
    time_1 = time.time()
    by_list()
    time_2 = time.time()
    by_str()
    time_3 = time.time()

    print 'by_list cost: %s\n by_str cost:%s' % (time_2 - time_1, time_3 - time_2)

if __name__ == '__main__':
    main()

