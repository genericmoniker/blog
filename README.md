esmithy.net blog
================

This is the project for the esmithy.net technical blog.

Setup
-----

1. Install Python 3.6+
2. Make a virtualenv
3. pip install -r requirements_dev.txt
4. inv -l to see what you can do from there


MarkDown Authoring Tips
-----------------------

Pelican uses the [Markdown](http://pythonhosted.org/Markdown/) Python package.

Image (put the image file in `content/images`):

    ![Alt Text]({filename}/images/image.jpg)

*Site-related images go in `content/site` instead.*

YouTube video:

    [![My Video](http://img.youtube.com/vi/<video_id>/0.jpg){:.vid}](https://www.youtube.com/v/<video_id>)

*Note the `vid` class -- the theme uses that to overlay a play button.*

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

Metadata
--------

Look at pelicanconf.py for the current categories.


To Do
-----

* Theme

    * Center post images
    * YouTube play button
    * Category page looks horrible (maybe need thumbnails for articles?)

* Clean up content

    * Filenames
    * Images local
    * Other content (esp. software section)

* Figure out comments (migration, too)
* Full-text search ([DuckDuckGo?](https://duckduckgo.com/search_box))
* Hosting
* Build process (and optimize tasks)
* Let's Encrypt
