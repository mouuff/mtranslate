
from distutils.core import setup

setup(
	name = 'mou_translator',
	packages = ['mou_translator'],
	version = '1.1',
	description = 'Translation API using Google translate',
	author = 'Arnaud Alies',
	author_email = 'arnaudalies.py@gmail.com',
	url = 'https://github.com/mouuff/Google-Translate-API',
	download_url = 'https://github.com/mouuff/Google-Translate-API/tarball/1.1',
	keywords = ['translate', 'translator', 'simple', 'google'],
	classifiers = [],
	entry_points={
          'console_scripts': [
              'mou_translator = mou_translator.__main__:main'
          ]
      },
)
