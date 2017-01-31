Title: Deceiving Your Readers
Date: 2013-12-28 15:56
Author: Eric
Category: Software Development
Slug: deceiving-your-readers
Status: published

APIs are user interfaces for programmers. I came across a function
recently that had a couple of user interface issues that serves as a
great example of this principle.

The function is internal to an HTTP client class, taking care of the
common logic independent of the HTTP method, and the signature looked
something like this:

```python
def _send(method, content_type):
    ...
```

This looks pretty straight-forward to programmers used to HTTP, but the
parameters are deceiving.

First of all, `content_type` is not actually a full content-type, but
rather only the content subtype. In other words, it takes whatever you
give it and prepends `'application/'`, so rather than passing in a
content-type like `'application/json'`, you'd just pass in `'json'`.
That's not a huge deal, but a programmer's user experience would be that
much smoother if the parameter name were `content_subtype`.

The other parameter, `method`, you might expect to be a string
indicating the HTTP method for the request. That would be wrong. It is
actually a function object from the [Python requests
library](http://docs.python-requests.org/en/latest/), such as
`requests.get` or `requests.post`, that will be used to actually send
the request off. Maybe `method_function` would be a better name.

Sure, sometimes you need a little context to understand that your first
thought of what something is isn't correct, and that the design choice
is actually reasonable, but little details can prevent bugs, like
slightly more precise parameter names.

As an example, the function above had a line like this in the middle of
it, written by one of the developers who was reasonably familiar with
the project:

```python
if method == 'GET' or method == 'POST':
    ...
```
