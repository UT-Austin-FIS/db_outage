DB Outage:
==========

This application will detect an Oracle database outage, and will handle it
gracefully by rendering a default error page.

Usage
=====

To include this app in your PyPE project, simply pull it into your project via
`svn:externals`.

> path: extra/db_outage

> URL: https://github.com/UT-Austin-FIS/db_outage/tags/v1.0/db_outage

Setup
-----

1. Add "`db_outage`" to your `INSTALLED_APPS` setting like this:

      ```python
            INSTALLED_APPS = (
                # ...
                'db_outage',
                # ...
            )
      ```

1. Add the `db_outage` middleware to your `MIDDLEWARE_CLASSES` in settings. It
   needs to be near the top, if not the very top of your middleware stack:

      ```python
            MIDDLEWARE_CLASSES = (
                'db_outage.middleware.DBOutageMiddleware',
                # ...
            )
      ```

3. Add `DB_OUTAGE_CONTEXT` to your `settings`. This should be a path to a class
   that carries the core of your page context logic. It will likely be 
   subclass of the Django `RequestContext` object.
   _IMPORTANT:_ The context object you supply MUST NOT require oracle database
   access.

      ```python
         DB_OUTAGE_CONTEXT = 'path.to.your.desired.ContextObject'
      ```

4. Add `DB_OUTAGE_MESSAGE` to your settings. This is a custom message that will
   be displayed when a database outage occurs:

      ```python
      DB_OUTAGE_MESSAGE = (
          'The <your application name> system is currently unavailable. '
          'We are working to restore service.'
      )
      ```

Releases
========

* v1.1 (2015/01/22)
  * Adding support for Django 1.7
* v1.0 (2014/05/29)
  * initial release with support for at least:
    * Python 2.6 - 2.7
    * Django 1.4
