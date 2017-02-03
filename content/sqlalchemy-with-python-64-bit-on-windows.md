Title: SQLAlchemy with Python 64-bit on Windows
Date: 2013-11-06 20:12
Author: Eric
Category: How It Works
Tags: Bafflers, Python, WTH
Slug: sqlalchemy-with-python-64-bit-on-windows
Status: published

While hooking up SQLAlchemy for a web project, I kept running into
attribute errors for 'session\_registry'. I figured I was doing
something wrong, so I thought I'd just walk through the
[tutorial](http://docs.sqlalchemy.org/en/rel_0_9/orm/tutorial.html) as a
sanity check.

I was, apparently, insane.

    >>> u = session.query(User).filter_by(name='ed').first()
    Traceback (most recent call last):
    File "", line 1, in
    File "C:\dev\misc\SundanceAPI\sapi_env\lib\site-packages\sqlalchemy\orm\query.py", line 2282, in first
    ret = list(self[0:1])
    File "C:\dev\misc\SundanceAPI\sapi_env\lib\site-packages\sqlalchemy\orm\query.py", line 2149, in __getitem__
    return list(res)
    File "C:\dev\misc\SundanceAPI\sapi_env\lib\site-packages\sqlalchemy\orm\query.py", line 2349, in __iter__
    context = self._compile_context()
    File "C:\dev\misc\SundanceAPI\sapi_env\lib\site-packages\sqlalchemy\orm\query.py", line 2702, in _compile_context
    context = QueryContext(self)
    File "C:\dev\misc\SundanceAPI\sapi_env\lib\site-packages\sqlalchemy\orm\query.py", line 3247, in __init__
    self.session = query.session_registry
    AttributeError: 'Query' object has no attribute 'session_registry'

Tom Christensen, after joining me in some head scratching, noticed that
I was on the 64-bit build of Python, and wondered if there could be
anything strange with that.

Googling, we [found](http://wiki.openlp.org/Windows_Environment):

> TODO: Still valid? The ez\_setup.py script currently(?) installs a
> broken version of setuptools on 64-bit Windows systems.
>
> TODO: Still valid? To work around this you need to manually
> download SQLAlchemy and extract it. When extracted you need to copy
> the &lt;top\_dir&gt;/lib/sqlalchemy directory into your
> Python&lt;version&gt;\\Lib\\site-packages directory.

Sure enough, following that work-around got rid of the errors. So
thanks, openlp guys. In the end, I swapped my virtual environment out
for the 32-bit variety. It feels safer there.
