DB Outage:
=====

This application will detect a database outage, and will handle it gracefully by rendering a default error page using the UTDirect context.

Usage
=====

To include this app in your PyPE project, simply pull it into your project via svn:externals.

> path: extra/db_outage

> URL: https://github.com/UT-Austin-FIS/outage/tags/1.2/outage

Setup
------

1. Add "db_outage" to your INSTALLED_APPS setting like this::

```python
      INSTALLED_APPS = (
          ...
          'db_outage',
      )
```

2. Add the db_outage middleware to your MIDDLEWARE_CLASSES setting like this::

```python
      MIDDLEWARE_CLASSES= (
          ...
          'db_outage.middleware.DBOutageMiddleware',
      )
```

3. Add DB_OUTAGE_CONTEXT object to your settings.py. This should be a class that carries the core of your page context logic. If not supplied, the UTDirectContext will be used, but you will need to supply the api key in your settings (eg: API_KEY = 'your_api_key')::
_IMPORTANT:_ The context object you supply MUST NOT require oracle database access.

```python
   DB_OUTAGE_CONTEXT = 'path.to.your.desired.context.object'
```

4. Add an DB_OUTAGE_DEFAULT_REDIRECT to your settings.py. This should be the name of a url pattern which will be used to redirect any users attempting to access the db_outage url directly when there is no outage occuring.::

```python
   DB_OUTAGE_DEFAULT_REDIRECT = 'url_name' # e.g.: 'home'
```

5. Include the db_outage URLconf in your project urls.py like this::

```python
    url(r'^apps/services/requests/', include(db_outage.urls)),
```

