AUTHOR = 'Eric'
SITENAME = 'ESMITHY.NET'
SITEURL = 'https://esmithy.net'

PATH = 'content'

TIMEZONE = 'America/Denver'

DEFAULT_LANG = 'en'

PLUGINS = [
    'readtime',
    'sitemap',
]

FORMATTED_FIELDS = ['title']

READTIME_WPM = 180  # for the readtime plugin

SITEMAP = {
    "format": "xml",
    "exclude": ["tag/", "category/"],
}

# Following items are often useful when publishing
#DISQUS_SITENAME = ""
#GOOGLE_ANALYTICS = ""

FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = None  # 'feeds/{slug}.atom.xml'
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

ARTICLE_URL = '{date:%Y}/{date:%m}/{date:%d}/{slug}/'
ARTICLE_SAVE_AS = '{date:%Y}/{date:%m}/{date:%d}/{slug}/index.html'
RELATIVE_URLS = True

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

DISPLAY_PAGES_ON_MENU = True

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
            Eric Smith is a software architect and developer. He currently
            works for Arcserve, and graduated with a computer science
            degree from Brigham Young University back when the World-Wide Web
            was a new thing.
        """,
        'cover': '/site/esmithy.jpg',
        'image': '/site/eric-small.png',
        'links': (
            ('github', 'https://github.com/genericmoniker'),
            ('envelope-square', 'mailto:eric@esmithy.net'),
        ),
    },
    'Ethan': {
        'description': """
            Ethan Smith is a computer science graduate from Southern Utah
            University.
        """,
        'cover': '/site/esmithy.jpg',
        'image': '/site/ethan-small.png',
        'links': (
            ('github', 'https://github.com/urd000med/'),
            ('envelope-square', 'mailto:ethan@esmithy.net'),
        ),
    },
}

MEDIUS_DEFAULT_COVER = '/site/esmithy.jpg'

MEDIUS_CATEGORIES = {
    'Event': {
        'description': 'Conferences and other happenings',
        'logo': '/site/cat-event.svg',
        'thumbnail': '/site/cat-event.svg'
    },
    'How It Works': {
        'description': 'The inner workings',
        'logo': '/site/cat-how-it-works.svg',
        'thumbnail': '/site/cat-how-it-works.svg'
    },
    'How-To': {
        'description': 'How to do something',
        'logo': '/site/cat-how-to.svg',
        'thumbnail': '/site/cat-how-to.svg'
    },
    'Opinion': {
        'description': 'General thoughts and opinions',
        'logo': '/site/cat-opinion.svg',
        'thumbnail': '/site/cat-opinion.svg'
    },
    'Project': {
        'description': 'Things I\'ve built',
        'logo': '/site/cat-project.svg',
        'thumbnail': '/site/cat-project.svg'
    },
    'Review': {
        'description': 'Thoughts on things other people did',
        'logo': '/site/cat-review.svg',
        'thumbnail': '/site/cat-review.svg'
    },
    'Story': {
        'description': 'Episodes from life and programming',
        'logo': '/site/cat-story.svg',
        'thumbnail': '/site/cat-story.svg'
    },
}
