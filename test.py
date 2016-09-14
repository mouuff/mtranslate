#!/usr/bin/env python
# -*- coding: utf-8 -*-

#from mou_translator.core import translate
from mou_translator import translate

def main():
	to_translate = 'Bonjour comment allez vous?'
	print("%s >> %s" % (to_translate, translate(to_translate)))
	print("%s >> %s" % (to_translate, translate(to_translate, 'es')))
	print("%s >> %s" % (to_translate, translate(to_translate, 'ar')))

if __name__ == '__main__':
	main()
