Title: Clean HTML from Microsoft Word: Rube Goldberg Method
Date: 2012-06-06 21:52
Author: Eric
Category: Project
Tags: Microsoft Office, Python
Slug: clean-html-from-microsoft-word-rube-goldberg-method
Status: published

Wouldn't it be nice to be able to save nice clean HTML from Microsoft
Word? Here's a way that is only *slightly* convoluted.

<!--more-->

If you use the "Web Page, Filtered" option from Word, you get buried in
piles of CSS cruft, but as noted
[here](http://stackoverflow.com/questions/67964/what-is-the-best-free-way-to-clean-up-word-html),
you can use the Publish &gt; Blog menu to generate pretty clean HTML...
to a blog. So, just sign yourself up for a free blog account somewhere,
figure out how to enable remote publishing, and um... *BZZZZT!* Next
idea please!

So here's a Python script that is a small MetaWebLog server. Run it
locally on your machine and publish straight to your hard drive!

### How to use it

1.  Save the script below as mwl.py
2.  Run "python mwl.py" from a command prompt
3.  From the Office menu thingy, choose **Publish** &gt; **Blog**
4.  Go ahead and click **Register Now** when prompted to register a blog
    account
5.  For the blog provider, pick "Other" and click **Next**
6.  In the "API" drop-down, choose "MetaWebLog"
7.  For "Blog Post URL", enter "http://localhost:8585"
8.  You can optionally put whatever you want for the "User Name" and
    "Password", and check the "Remember Password" box so that Word won't
    keep nagging you for credentials
9.  If all goes well, Word should report "Account registration
    successful."
10. Where it says "Enter Post Title Here", type what you want your file
    to be named (it will be saved in your Documents folder, and a .html
    extension will be added)\
    **WARNING**: It will overwrite any existing file at that location!
11. Click the **Publish** button, and your wonderfully clean HTML file
    will be saved

**Update 10 Jun 2012**: The script outputs UTF-8 now.

```python
# mwl.py - by Eric Smith - http://esmithy.net

from SimpleXMLRPCServer import SimpleXMLRPCServer
import os.path

PORT = 8585
BLOG_URL = "http://localhost:{0}".format(PORT)
HTML = u'{0}{1}'

def get_user_blogs(key, username, password):
    return [{'url':BLOG_URL, 'blogid':'1', 'blogName':'Save HTML'}]
    
def new_post(blogid, username, password, struct, publish):
    filename = _get_filename(struct['title'])
    _write_html(filename, struct['title'], struct['description'])
    return struct['title']

def get_post(postid, username, password):
    filename = _get_filename(postid)
    print 'Reading HTML from ' + filename
    struct = {'title':postid}
    with open(filename, 'r') as f:
        struct['description'] = f.read()
    return struct

def edit_post(postid, username, password, struct, publish):
    filename = _get_filename(postid)
    _write_html(filename, struct['title'], struct['description'])
    return True

def _get_filename(n):
    return os.path.expanduser('~/Documents/{0}.html'.format(n))
    
def _write_html(filename, title, body):
    print 'Saving HTML to ' + filename
    with open(filename, 'w') as f:
        f.write(HTML.format(title, body).encode("utf-8"))

def main():
    server = SimpleXMLRPCServer(('localhost', PORT))
    server.register_introspection_functions()
    server.register_function(get_user_blogs, 'blogger.getUsersBlogs')
    server.register_function(new_post, 'metaWeblog.newPost')
    server.register_function(get_post, 'metaWeblog.getPost')
    server.register_function(edit_post, 'metaWeblog.editPost')
    print "Listening on port {0}".format(PORT)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass

if __name__ == '__main__':
    main()
```
