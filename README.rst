===============
HOW TO USE THIS
===============

Create a skeleton for your new project
======================================

::

    $ svn export http://svn.github.com/niteoweb/niteoweb.skel.pyramid.git <shortname>
    $ cd <shortname>
    $ mv src/zulu src/<shortname>


Commit skeleton to repository
=============================

::

    $ svn mkdir https://niteoweb.repositoryhosting.com/svn/niteoweb_<shortname>/<shortname> -m "create package dir"
    $ svn mkdir https://niteoweb.repositoryhosting.com/svn/niteoweb_<shortname>/<shortname>/{trunk,tags,branches} -m "create svn structure"
    $ svn co https://niteoweb.repositoryhosting.com/svn/niteoweb_<shortname>/<shortname>/trunk ./
    $ ln -s development.cfg buildout.cfg
    $ svn add *


Customize
=========

 * Use search&replace to replace all placeholder strings with meaningful ones:
   Zulu, zulu, TODO.
 * Remove this entire paragraph ("How to use this") from README.rst.
 * Start coding :).


Initialize buildout and start paster
====================================

::

    $ virtualenv -p python2.6 --no-site-packages ./
    $ bin/python bootstrap.py
    $ bin/buildout
    $ bin/paster serve etc/development.ini



#################### REMOVE ALL BUT THE FOLLOWING LINE ####################

See `docs/README.rst <https://sphinx.niteoweb.com/zulu>`_
