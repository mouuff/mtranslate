#!/usr/bin/env python
# encoding: utf-8

import six

if (six.PY2):
	import urllib2
	import re
	import urllib
else:
	import urllib.request
	import urllib.parse
	import re

agent = {'User-Agent' : "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 1.1.4322; .NET CLR 2.0.50727; .NET CLR 3.0.04506.30)"}


def translate(to_translate, to_language="auto", language="auto"):
	"""
	Returns the translation using google translate
	you must shortcut the language you define (French = fr, English = en, Spanish = es, etc...)
	if you don't define anything it will detect it or use english by default
	Example:
	print(translate("salut tu vas bien?", "en"))
	hello you alright?
	"""
	base_link = "http://translate.google.com/m?hl=%s&sl=%s&q=%s"
	if (six.PY2):
		link = base_link % (to_language, language, urllib.pathname2url(to_translate))
		request = urllib2.Request(link, headers=agent)
		page = urllib2.urlopen(request).read()
	else:
		link = base_link % (to_language, language, urllib.parse.quote(to_translate))
		request = urllib.request.Request(link, headers=agent)
		page = urllib.request.urlopen(request).read().decode("utf-8")
	expr = r'class="t0">(.*?)<'
	result = re.findall(expr, page)
	if (len(result) == 0):
		return ("")
	return(result[0])


if __name__ == '__main__':
	to_translate = 'Bonjour comment allez vous?'
	print("%s >> %s" % (to_translate, translate(to_translate)))
	print("%s >> %s" % (to_translate, translate(to_translate, 'es')))
	print("%s >> %s" % (to_translate, translate(to_translate, 'ar')))

