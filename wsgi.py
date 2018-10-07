#!/usr/bin/env python


import os, sys

sys.path.append('/usr/local/lib/python2.7/dist-packages')

from django.core.wsgi import get_wsgi_application


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "YyBlog.settings")

application = get_wsgi_application()
