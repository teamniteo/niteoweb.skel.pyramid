#!/bin/bash

echo 'Running tests'
bin/py setup.py test

echo '====== Running PyFlakes ======'
bin/pyflakes src/zulu
bin/pyflakes setup.py
bin/pep8 fabfile.py

echo '====== Running pep8 =========='
bin/pep8 src/zulu
bin/pep8 setup.py
bin/pep8 fabfile.py

