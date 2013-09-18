#!/usr/bin/python
# -*- indent-tabs-mode: nil; tab-width: 4 -*-
# vi: et ts=4 sts=4 sw=4
class Test:
    def __init__(self):
        self.test = 1

    def __setitem__(self, key, item):
        setattr(self, key, item)

def main():
    test = Test()
    print test.test
    test['test'] = 2
    print test.test

if __name__ == '__main__':
    main()

