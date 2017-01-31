Title: Getting pip into your Python 3 venv
Date: 2013-09-20 21:22
Author: Eric
Category: Programming
Tags: Python
Slug: getting-pip-into-your-python-3-venv
Status: published

Python 3.3 [includes a
built-in](http://docs.python.org/dev/library/venv.html) equivalent to
the popular [virtualenv](http://www.virtualenv.org/) tool for creating
isolated Python environments. One difference with the built-in venv is
that it doesn't automatically install
[pip](http://www.pip-installer.org/) as virtualenv does. While I can
understand the decision (given Python's volatile packaging situation),
it isn't very convenient.

Here's a Windows batch file that will remedy that, using the [latest
recommended
way](http://packaging.python.org/en/latest/tutorial.html#installing-the-tools)
of getting pip. It depends on having
[curl](http://curl.haxx.se/download.html) in your path somewhere. Use it
like you would virtualenv or venv, namely, by providing the path to
where you'd like to create your new virtual environment.

```bat
@echo off

REM Python 3.3 pyvenv including pip.
REM See https://python-packaging-user-guide.readthedocs.org/en/latest/setup.html

if "%1" == "" goto :error

python -m venv %1
call %1\Scripts\activate

curl -O https://bitbucket.org/pypa/setuptools/raw/bootstrap/ez_setup.py
python ez_setup.py

curl -O https://raw.github.com/pypa/pip/master/contrib/get-pip.py
python get-pip.py

del ez_setup.py
del get-pip.py
del setuptools-*.tar.gz

goto :EOF

:error
echo Specify the path to the virtual environment you want to create.
echo venv my_env
```