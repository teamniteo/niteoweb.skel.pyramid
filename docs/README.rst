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
:Server: Omega

Quick Start
===========

.. sourcecode:: bash

  $ cd ~/work
  $ svn co https://niteoweb.repositoryhosting.com/svn/niteoweb_zulu/zulu/trunk zulu
  $ cd zulu/
  $ virtualenv -p python2.6 --no-site-packages ./
  $ bin/python bootstrap.py
  $ bin/buildout
