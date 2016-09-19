#!/usr/bin/env python
# -*- coding: utf-8 -*-

from mtranslate import translate


def main():
    to_translate = 'Bonjour comment allez vous?'
    print("%s >> %s" % (to_translate, translate(to_translate)))
    print("%s >> %s" % (to_translate, translate(to_translate, 'es')))
    print("%s >> %s" % (to_translate, translate(to_translate, 'ar')))

if __name__ == '__main__':
    main()
