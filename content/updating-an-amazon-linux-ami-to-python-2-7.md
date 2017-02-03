Title: Updating an Amazon Linux AMI to Python 2.7 
Date: 2012-01-12 10:22
Author: Eric
Category: How-To
Tags: AWS, Linux, Python
Slug: updating-an-amazon-linux-ami-to-python-2-7
Status: published

I've been doing some work with Linux lately, a new thing for me, and
feel a bit like I've been thrown into the deep end and told to swim.
Today I updated Python to version 2.7 on an EC2 instance.

<!--more-->

Amazon Linux (Basic 64-bit Amazon Linux AMI 2011.09 AMI Id:
ami-1b814f72) currently comes with Python 2.6.7 on it. At first, I
thought I'd just be able to update to 2.7 with yum, but as far as I can
tell, there isn't a package for that already.

Joshua Holmes
[wrote](http://joshualholmes.wordpress.com/category/amazon-ec2/) about
updating Python, which was a great help. My experienced varied a little,
so I thought I'd share in case it is useful to someone else. For
example, I didn't want sqllite, but I did want ssl support. Also, there
were some cases where I needed to use `sudo` when logged in as ec2-user.

```
#!bash
sudo yum install make gcc gcc-c++
sudo yum install openssl-devel.x86_64
 
cd ~
wget http://python.org/ftp/python/2.7/Python-2.7.tgz
tar xfz Python-2.7.tgz
cd Python-2.7
./configure --prefix=/opt/python2.7 --with-threads --with-ssl --enable-shared
make
sudo make install

cd ~ 
echo '''
 alias python='/opt/python2.7/bin/python'
 PATH=$PATH:/opt/python2.7/bin
 ''' >> .bash_profile
source .bash_profile
 
echo '''
 /opt/python2.7/lib
 ''' >> opt-python2.7.conf
sudo mv opt-python2.7.conf  /etc/ld.so.conf.d/
sudo ldconfig
 
python -V
Python 2.7
```

Notes
-----

Line 26 is output from Python -- not something you input (if that wasn't
obvious).

The `configure` script (line 8 ) specifies which optional libraries will
be included in Python. I'm not sure what the typical list includes (for
example, which are included in the official Python install for
Windows?), but when you run `make` (line 9), it will report all the
missing libraries for Python modules ("Python build finished, but the
necessary bits to build these modules were not found"). If you use a
module with a missing library in a Python program, you'll get a runtime
error.

The `echo` lines (13-16) are editing your user profile file for bash so
that when you type 'python' you'll get the 2.7 version instead of the
default 2.6.7 version. I had a situation where I needed to run python
under `sudo`, but root doesn't have the alias, so it kept running 2.6.7.
After some unfruitful attempts to add the alias to /etc/profile (`sudo`
doesn't execute that), I just added a symlink and invoked 'python2.7'
explicitly (thanks to Chris Brinker):

```
#!bash
sudo ln -s /opt/python2.7/bin/python /usr/bin/python2.7
sudo python2.7 -V
Python 2.7
```
