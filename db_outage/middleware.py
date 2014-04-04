import sys

import cx_Oracle
from django.conf import settings
from django.core.urlresolvers import reverse
from django.shortcuts import redirect

from timeout import timeout

_using_manage = True in ['manage.py' in arg for arg in sys.argv]

TESTING = ((_using_manage and 'test' in sys.argv) or ('nosetests' in sys.argv))


class DBOutageMiddleware(object):

    def process_request(self, request):

        # Django tests may set their own ROOT_URLCONF, in which case we may not
        # be able to resolve 'db_outage', so we'll just return None unless testing
        # this app intentionally.
        if TESTING and 'db_outage' not in sys.argv:
            return None

        if (request.path == reverse('db_outage') or
            u'static' in request.path.split('/')
            ):
            return None

        try:
            ping_db()
        except (cx_Oracle.DatabseError, TimeoutError):
            #TODO: notify devs
            return redirect('db_outage')

        return None

    @timeout(15)
    def ping_db():
#        ip, port, SID = parse_tnsnames()
#        dns_tns = cx_Oracle.makedsn(ip, port, SID)
#        db = cx_Oracle.connect(username, password, dns_tns)
#        db = cx_Oracle.connect(
#            settings.DATABASES['default']['USER'],
#            settings.DATABASES['default']['PASSWORD'],
#            dns_tns,
#            )
        user = settings.DATABASES['default']['USER'],
        pwd = settings.DATABASES['default']['PASSWORD'],
        db = cx_Oracle.connect(user + '/' + pwd + '@default')
        db.ping()
        db.close()
        return None

    #def parse_tnsnames():

