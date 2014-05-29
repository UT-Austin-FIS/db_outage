DB Outage:
=====

This application will detect a database outage, and will handle it gracefully by rendering a default error page using the UTDirect context.

Usage
=====

To include this app in your PyPE project, simply pull it into your project via svn:externals.

> path: extra/db_outage

> URL: https://github.com/UT-Austin-FIS/db_outage/tags/1.0/db_outage

Setup
------

1. Add "db_outage" to your INSTALLED_APPS setting like this::

```python
      INSTALLED_APPS = (
          ...
          'db_outage',
      )
```

2. Add the db_outage middleware to your MIDDLEWARE_CLASSES in settings. It needs to be near the top, if not the very top of your middleware stack::

```python
      MIDDLEWARE_CLASSES= (
          'db_outage.middleware.DBOutageMiddleware',
          ...
      )
```

3. Add DB_OUTAGE_CONTEXT to your settings.py. This should be a path to a class that carries the core of your page context logic. It will likely be a subclass of the django RequestContext object.::
_IMPORTANT:_ The context object you supply MUST NOT require oracle database access.

```python
   DB_OUTAGE_CONTEXT = 'path.to.your.desired.ContextObject'
```

4. Add DB_OUTAGE_MESSAGE to your settings.py. This is a custom message that will be displayed when a database outage occurs.::

```python
   DB_OUTAGE_MESSAGE =(
      'The <your application name> system is currently unavailable. We are working '
      'to restore service'
   )
```
