from django.conf import settings
from django.core.exceptions import ImproperlyConfigured
from django.views.generic.base import TemplateView

try:
    module_path, ctx_class = settings.DB_OUTAGE_CONTEXT.rsplit('.',1)
    module = __import__(module_path, fromlist=[ctx_class])
    context = getattr(module, ctx_class)
except AttributeError:
    raise ImproperlyConfigured(
        'You must supply a path your own context object by setting a '
        'DB_OUTAGE_CONTEXT in your settings.py file.'
    )


class DBOutage(TemplateView):
    template_name = 'db_outage/db_outage.html'

    def get_context_data(self, **kwargs):
        ctx = super(DBOutage, self).get_context_data(**kwargs)
        try:
            msg = settings.DB_OUTAGE_MESSAGE
        except AttributeError:
            raise ImproperlyConfigured(
                'You must add a DB_OUTAGE_MESSAGE to your settings. Example: '
                'We are experiencing technical difficulties. Our IT staff has '
                'been notified.'
            )
        ctx.update({'msg':msg})
        return context(
            self.request,
            ctx,
            title='Service Outage',
            page_title='Service Outage',
            window_title='Service Outage',
        )
