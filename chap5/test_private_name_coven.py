#!/usr/bin/python
# -*- indent-tabs-mode: nil; tab-width: 4 -*-
# vi: et ts=4 sts=4 sw=4
class Foo:
    def __priv(self):
        print "I'm private"

def main():
    foo = Foo()
    getattr(Foo, '_Foo__priv')(foo)

if __name__ == '__main__':
    main()

