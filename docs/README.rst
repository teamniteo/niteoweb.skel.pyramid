============
Zulu project
============

:Project title: Zulu
:Project id: zulu
:Author: NiteoWeb Ltd.
:URL: http://zulu.com
:Docs: https://sphinx.niteoweb.com/zulu
:Source: https://niteoweb.repositoryhosting.com/svn/niteoweb_zulu
:Framework: Pyramid
:Server: <PRODUCTION SERVER NAME>

Quick Start
===========

Start hacking away on this project by running::

  $ cd ~/work
  $ svn co https://niteoweb.repositoryhosting.com/svn/niteoweb_zulu/zulu/trunk zulu
  $ cd zulu/
  $ virtualenv -p python2.6 --no-site-packages ./
  $ bin/python bootstrap.py -c development.cfg
  $ bin/buildout -c development.cfg
  $ bin/paster serve etc/development.ini


