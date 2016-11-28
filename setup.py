
from distutils.core import setup

setup(
    name = 'mtranslate',
    packages = ['mtranslate'],
    version = '1.4',
    description = 'Google translate console script with easy to use API',
    author = 'Arnaud Alies',
    author_email = 'arnaudalies.py@gmail.com',
    url = 'https://github.com/mouuff/mtranslate',
    download_url = 'https://github.com/mouuff/mtranslate/tarball/1.4',
    keywords = ['console', 'translate', 'translator', 'simple', 'google'],
    classifiers = [],
    entry_points={
          'console_scripts': [
              'mtranslate = mtranslate.__main__:main'
          ]
      },
)
