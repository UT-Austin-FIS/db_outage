import sys

import cx_Oracle
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
            query_dual_table()
        except (cx_Oracle.DatabseError, TimeoutError):
            #TODO: notify devs
            return redirect('db_outage')

        return None

    @timeout(15)
    def query_dual_table():
        #TODO: query dual table here
        pass
