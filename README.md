esmithy.net blog
================

This is the project for the esmithy.net technical blog.

Tools
-----

* Python 3 - for running all the things
* Pelican - for generating the static part of the site
* Whoosh - for full-text search
* Invoke - for encapsulating build/deploy commands

MarkDown Authoring Tips
-----------------------

Image (put the image file in `content/images`):

    ![Alt Text]({filename}/images/image.jpg)

Book links to GoodReads:

    *[The Phoenix
    Project](https://www.goodreads.com/book/show/17255186-the-phoenix-project)*

Syntax highlighting:

    ```python
    print('Hello, world!')
    ```
    
Syntax highlighting with line numbers (shebang is pulled out):

    ```
    #!python
    print('Hello, world!')
    ```

Available highlighting lexers are documented 
[here](http://pygments.org/docs/lexers/).


To Do
-----

* Clean up theme

    * Clean up categories and add images
    * Center post images

* Clean up content

    * Filenames
    * Images local
    * Other content (esp. software section)

* Figure out comments (migration, too)
* Full-text search ([DuckDuckGo?](https://duckduckgo.com/search_box))
* Hosting
