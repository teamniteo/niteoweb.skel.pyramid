# -*- coding: utf-8 -*-
"""Installer for this package."""

from setuptools import setup
from setuptools import find_packages

import os


# shamlessly stolen from Hexagon IT guys
def read(*rnames):
    return open(os.path.join(os.path.dirname(__file__), *rnames)).read()

version = read('src', 'niteoweb', 'zulu', 'version.txt').strip()

setup(name='niteoweb.zulu',
      version=version,
      description="A portal for young entrepreneurs in Slovenia.",
      long_description=read('docs', 'README.rst') +
                       read('docs', 'HISTORY.rst') +
                       read('docs', 'LICENSE.rst'),
      classifiers=[
        "Programming Language :: Python",
        "Framework :: Pylons",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Internet :: WWW/HTTP :: WSGI :: Application",
        ],
      keywords='web wsgi bfg pylons pyramid',
      author='NiteoWeb Ltd.',
      author_email='info@niteoweb.com',
      url='http://www.niteoweb.com',
      license='BSD',
      packages=find_packages('src', exclude=['ez_setup']),
      package_dir={'': 'src'},
      include_package_data=True,
      zip_safe=False,
      test_suite='zulu',
      install_requires=[
          # list project dependencies
          'niteoweb.fabfile',
          'setuptools',
      ],
      entry_points="""\
      [paste.app_factory]
      main = zulu:main
      """,
#      paster_plugins=['pyramid'],
      )
