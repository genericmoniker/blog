Title: Python Time 2025
Date: 2025-05-11 20:20
Modified: 2026-01-04 10:11
Author: Eric
Category: How It Works
Slug: python-time-2025
Status: published

A quick reference for time...

## Get the current time in UTC

```python
from datetime import datetime, UTC

datetime.now(UTC)
```
```
datetime.datetime(2025, 1, 28, 23, 4, 45, 419714, tzinfo=datetime.timezone.utc)
```

You might think you should use `datetime.utcnow()` but:

> Deprecated since version 3.12: Use `datetime.now()` with `UTC` instead.

Also note:

> [datetime.UTC](https://docs.python.org/3/library/datetime.html#datetime.UTC "Link to this definition")
>
> Alias for the UTC timezone singleton [`datetime.timezone.utc`](https://docs.python.org/3/library/datetime.html#datetime.timezone.utc "datetime.timezone.utc").
>
> New in version 3.11.

## Get the current time in the local time zone

```python
from datetime import datetime

datetime.now().astimezone()
```

```
datetime.datetime(2025, 1, 28, 16, 6, 8, 979640, tzinfo=datetime.timezone(datetime.timedelta(days=-1, seconds=61200), 'MST'))
```

## Get the current time in some other time zone

```python
from datetime import datetime
from zoneinfo import ZoneInfo

datetime.now().astimezone(ZoneInfo("America/Los_Angeles"))
```

```
datetime.datetime(2025, 1, 28, 15, 8, 38, 699557, tzinfo=zoneinfo.ZoneInfo(key='America/Los_Angeles'))
```

## Convert a `datetime` to local time for a specific time zone

```python
from zoneinfo import ZoneInfo

local_time = some_datetime.astimezone(ZoneInfo("America/Denver"))
```

Or to UTC:

```python
from datetime import UTC

utc_time = some_datetime.astimezone(UTC)
```

## ZoneInfo keys

Valid `ZoneInfo` keys (defined by [IANA](https://www.iana.org/time-zones)) come
from the system, and are POSIX paths from some root directory. For example, on
my Ubuntu machine this is /usr/share/zoneinfo.

```
$ ls /usr/share/zoneinfo/
Africa      Canada   EST      GMT+0      Iran               Libya      NZ-CHAT     right      US
America     CET      EST5EDT  GMT-0      iso3166.tab        localtime  Pacific     ROC        UTC
Antarctica  Chile    Etc      GMT0       Israel             MET        Poland      ROK        WET
Arctic      CST6CDT  Europe   Greenwich  Jamaica            Mexico     Portugal    Singapore  W-SU
Asia        Cuba     Factory  Hongkong   Japan              MST        posix       Turkey     zone1970.tab
Atlantic    EET      GB       HST        Kwajalein          MST7MDT    posixrules  tzdata.zi  zonenow.tab
Australia   Egypt    GB-Eire  Iceland    leapseconds        Navajo     PRC         UCT        zone.tab
Brazil      Eire     GMT      Indian     leap-seconds.list  NZ         PST8PDT     Universal  Zulu
```

Windows, however, doesn't have an IANA time zone database.

```
zoneinfo._common.ZoneInfoNotFoundError: 'No time zone found with key America/Denver'
```

The solution is to install the [tzdata](https://pypi.org/project/tzdata/)
package that is published by the Python developers.
