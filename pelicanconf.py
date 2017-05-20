SITENAME = 'ESMITHY.NET'
SITEURL = ''
AUTHOR = 'Eric'
ARTICLE_URL = '{date:%Y}/{date:%m}/{date:%d}/{slug}/'
ARTICLE_SAVE_AS = '{date:%Y}/{date:%m}/{date:%d}/{slug}/index.html'
RELATIVE_URLS = True

PATH = 'content'
STATIC_PATHS = ['downloads', 'extra', 'images', 'site']
EXTRA_PATH_METADATA = {
    'extra/favicon.ico': {'path': 'favicon.ico'},
    'extra/favicon-16x16.png': {'path': 'favicon-16x16.png'},
    'extra/favicon-32x32.png': {'path': 'favicon-32x32.png'},
    'downloads/inspection-printer/publish.h':
        {'path': 'downloads/inspection-printer/publish.htm'},
    'downloads/workplan/publish.h':
        {'path': 'downloads/workplan/publish.htm'},
}


TIMEZONE = 'America/Denver'

DEFAULT_LANG = 'en'

DISPLAY_PAGES_ON_MENU = True

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll - These would show at the bottom of the page in my current theme.
# LINKS = (('Pelican', 'http://getpelican.com/'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

# Theme settings - theme is a fork of the Medius theme.

THEME = 'theme'  # Relative path to theme directory.
MEDIUS_AUTHORS = {
    'Eric': {
        'description': """
            Software architect and developer.
        """,
        'cover': '/site/esmithy.jpg',
        'image': '/site/eric-small.png',
        'links': (
            ('github', 'https://github.com/genericmoniker'),
            ('envelope-square', 'mailto:eric@esmithy.net'),
        ),
    }
}

MEDIUS_DEFAULT_COVER = '/site/esmithy.jpg'

MEDIUS_CATEGORIES = {
    'Event': {
        'description': 'Conferences and other happenings',
        'logo': '/site/cat-event-thumb.png',
        'thumbnail': '/site/cat-event-thumb.png'
    },
    'How It Works': {
        'description': 'The inner workings',
        'logo': '/site/cat-how-it-works-thumb.png',
        'thumbnail': '/site/cat-how-it-works-thumb.png'
    },
    'How-To': {
        'description': 'How to do something',
        'logo': '/site/cat-how-to-thumb.png',
        'thumbnail': '/site/cat-how-to-thumb.png'
    },
    'Opinion': {
        'description': 'General thoughts and opinions',
        'logo': '/site/cat-opinion-thumb.png',
        'thumbnail': '/site/cat-opinion-thumb.png'
    },
    'Project': {
        'description': 'Things I\'ve built',
        'logo': '/site/cat-project-thumb.png',
        'thumbnail': '/site/cat-project-thumb.png'
    },
    'Review': {
        'description': 'Thoughts on things other people did',
        'logo': '/site/cat-review-thumb.png',
        'thumbnail': '/site/cat-review-thumb.png'
    },
    'Story': {
        'description': 'Episodes from life and programming',
        'logo': '/site/cat-story-thumb.png',
        'thumbnail': '/site/cat-story-thumb.png'
    },
}