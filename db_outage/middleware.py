import sys

import cx_Oracle
from django.conf import settings
from django.core.mail import mail_admins
import logging

from django.db import connection
from db_outage.views import DBOutage

logger = logging.getLogger('django')

_using_manage = True in ['manage.py' in arg for arg in sys.argv]

TESTING = ((_using_manage and 'test' in sys.argv) or ('nosetests' in sys.argv))


class DBOutageMiddleware(object):

    def process_request(self, request):

        # Django tests may set their own ROOT_URLCONF, in which case we may not
        # be able to resolve 'db_outage', so we'll just return None unless testing
        # this app intentionally.
        if TESTING and 'db_outage' not in sys.argv:
            return None

        if settings.STATIC_URL in request.path:
            return None

        try:
            self.ping_db()
        except (cx_Oracle.DatabaseError) as exc:
            msg = ('Your application is having trouble connecting to the '
                    'database. Please investigate.')
            mail_admins('DatabaseError',msg)
            logger.error(exc)
            return DBOutage.as_view()(request)

        return None

    def ping_db(self):
        cursor = connection.cursor()
        cursor.execute("SELECT 1 FROM DUAL")
        cursor.close()
        return None
