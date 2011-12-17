#!/bin/bash

echo 'Running tests'
bin/py setup.py test

echo '====== Running ZPTLint ======'
for pt in `find collective/listusers/ -name "*.pt"` ; do bin/zptlint $pt; done

echo '====== Running PyFlakes ======'
bin/pyflakes src/zulu
bin/pyflakes setup.py
bin/pep8 fabfile.py

echo '====== Running pep8 =========='
bin/pep8 src/zulu
bin/pep8 setup.py
bin/pep8 fabfile.py

