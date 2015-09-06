import os
import sys
from django.core.wsgi import get_wsgi_application
sys.path = ['/var/www/folio/folio'] + sys.path
os.environ['DJANGO_SETTINGS_MODULE'] = 'folio.settings'

application = get_wsgi_application()