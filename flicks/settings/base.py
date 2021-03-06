# This is your project's main settings file that can be committed to your
# repo. If you need to override a setting locally, use settings_local.py
from django.utils.functional import lazy

from funfactory.settings_base import *


PROD_LANGUAGES = ('de', 'en-US', 'es', 'fr', 'nl', 'pl', 'pt-BR', 'sl', 'sq',
                  'zh-TW')

# Defines the views served for root URLs.
ROOT_URLCONF = 'flicks.urls'

AUTHENTICATION_BACKENDS = (
    'django_browserid.auth.BrowserIDBackend',
    'django.contrib.auth.backends.ModelBackend',
)

# Paths that do not need a locale
SUPPORTED_NONLOCALES += ['admin', 'robots.txt']

INSTALLED_APPS = list(INSTALLED_APPS) + [
    'flicks.base',
    'flicks.users',
    'flicks.videos',

    'django.contrib.admin',

    'compressor',
    'csp',
    'django_browserid',
    'jingo_offline_compressor',
    'django_statsd',
    'jingo_minify',
    'south',
    'waffle',
]

MIDDLEWARE_CLASSES = list(MIDDLEWARE_CLASSES) + [
    'commonware.response.middleware.StrictTransportMiddleware',
    'csp.middleware.CSPMiddleware',
    'django_statsd.middleware.GraphiteRequestTimingMiddleware',
    'django_statsd.middleware.GraphiteMiddleware',
    'waffle.middleware.WaffleMiddleware',
]

TEMPLATE_CONTEXT_PROCESSORS = list(TEMPLATE_CONTEXT_PROCESSORS) + [
   'django_browserid.context_processors.browserid',
]

AUTH_PROFILE_MODULE = 'flicks.UserProfile'

# django-browserid
LOGIN_REDIRECT_URL = '/'
LOGIN_REDIRECT_URL_FAILURE = '/'
LOGOUT_REDIRECT_URL = '/'

# Because Jinja2 is the default template loader, add any non-Jinja templated
# apps here:
JINGO_EXCLUDE_APPS = [
    'admin',
    'browserid',
    'registration',
]

# Tells the extract script what files to look for L10n in and what function
# handles the extraction. The Tower library expects this.
DOMAIN_METHODS = {
    'messages': [
        ('**/flicks/**.py',
            'tower.management.commands.extract.extract_tower_python'),
        ('**/flicks/**/templates/**.html',
            'tower.management.commands.extract.extract_tower_template')
    ],
}

# # Use this if you have localizable HTML files:
# DOMAIN_METHODS['lhtml'] = [
#    ('**/templates/**.lhtml',
#        'tower.management.commands.extract.extract_tower_template'),
# ]

# # Use this if you have localizable HTML files:
# DOMAIN_METHODS['javascript'] = [
#    # Make sure that this won't pull in strings from external libraries you
#    # may use.
#    ('media/js/**.js', 'javascript'),
# ]

# Always generate a CSRF token for anonymous users
ANON_ALWAYS = True

# Email Settings
DEFAULT_FROM_EMAIL = 'firefoxflicks@mozilla.com'

# Secure Cookies
SESSION_COOKIE_SECURE = True

# Django-CSP
CSP_IMG_SRC = ("'self'",
               'data:',
               'https://d3fenhwk93s16g.cloudfront.net',
               'https://www.gravatar.com',
               'https://secure.gravatar.com',
               'http://www.google-analytics.com',
               'https://ssl.google-analytics.com',
               'http://*.mozilla.org',
               'https://*.mozilla.org',
               'http://*.mozilla.net',
               'https://*.mozilla.net',)
CSP_STYLE_SRC = ("'self'",
                 'https://fonts.googleapis.com',
                 'http://*.mozilla.org',
                 'https://*.mozilla.org',
                 'http://*.mozilla.net',
                 'https://*.mozilla.net',
                 'http://*.vimeo.com',
                 'https://*.vimeo.com',)
CSP_FONT_SRC = ("'self'",
                'https://themes.googleusercontent.com',
                'http://*.mozilla.org',
                'https://*.mozilla.org',
                'http://*.mozilla.net',
                'https://*.mozilla.net',)
CSP_SCRIPT_SRC = ("'self'",
                  'http://browserid.org',
                  'https://browserid.org',
                  'http://login.persona.org',
                  'https://login.persona.org',
                  'https://platform.twitter.com',
                  'https://connect.facebook.net',
                  'http://www.google-analytics.com',
                  'https://ssl.google-analytics.com',
                  'http://*.mozilla.org',
                  'https://*.mozilla.org',
                  'http://*.mozilla.net',
                  'https://*.mozilla.net',
                  'http://*.vimeo.com',
                  'https://*.vimeo.com',
                  'https://*.vimeocdn.com',)
CSP_FRAME_SRC = ('https://vid.ly',
                 'http://platform.twitter.com',
                 'https://platform.twitter.com',
                 'https://www.facebook.com',
                 'http://*.vimeo.com',
                 'https://*.vimeo.com',
                 'https://*.vimeocdn.com',)
CSP_OPTIONS = ('eval-script', 'inline-script')

# Activate statsd patches to time database and cache hits.
STATSD_PATCHES = [
    'django_statsd.patches.db',
    'django_statsd.patches.cache',
]

# Video preview settings
PREVIEW_PATH = lambda inst, filename: 'previews/images/%s_%s' % (inst.id, filename)
MAX_FILEPATH_LENGTH = 100

# Google Analytics
GA_ACCOUNT_CODE = ''

# Allow robots to crawl the site.
ENGAGE_ROBOTS = True

# Gravatar Settings
GRAVATAR_URL = 'https://secure.gravatar.com'
DEFAULT_GRAVATAR = MEDIA_URL + 'img/anon_user.png'

# django-compressor
COMPRESS_PARSER = 'compressor.parser.HtmlParser'


def lazy_compress_offline_context():
    """
    Add browserid_js to context used during minification, as context processors
    aren't used during this process, breaking the browserid JS embed.
    """
    from functools import partial
    from django_browserid.context_processors import browserid_js
    from django_browserid.forms import BrowserIDForm

    return {
        'browserid_js': partial(browserid_js, BrowserIDForm())
    }
COMPRESS_OFFLINE_CONTEXT = lazy(lazy_compress_offline_context, dict)()


# Promo video shortlinks
PROMO_VIDEOS = {
    'noir': {
        'en-us': '3q4s0q',
        'fr': '9j6k9j',
        'de': '7r0d1f',
        'es': '5m9i4w',
        'ja': '8r9w3d',
        'lij': '8y4r4v',
        'nl': '8d0f4b',
        'pl': '8u7s6j',
        'sl': '6e3t9x',
        'sq': '7c9p0d',
        'zh-cn': '0i8v1n',
        'zh-tw': '3r1o8k'
    },
    'dance': {
        'en-us': '3x8n2e',
        'fr': '2s8o4r',
        'de': '5i1u9r',
        'es': '8r3y6e',
        'ja': '5o7b0l',
        'lij': '7a8r6a',
        'nl': '0m4s3u',
        'pl': '4v1w8v',
        'sl': '6v3h2g',
        'sq': '0o5k7n',
        'zh-cn': '9w8d4k',
        'zh-tw': '5q2v4y'
    },
    'twilight': {
        'en-us': '6d9t7l',
        'fr': '4k0a3w',
        'de': '8n1f7u',
        'es': '0y9t0e',
        'ja': '3f9o1c',
        'lij': '5i0n9p',
        'nl': '8c5a2f',
        'pl': '3d8u9p',
        'sl': '9e2i0u',
        'sq': '3c8y0t',
        'zh-cn': '4w9f9x',
        'zh-tw': '3m0y4x'
    }
}
