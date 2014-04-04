from django.conf import settings
from django.core.exceptions import ImproperlyConfigured
from django.shortcuts import redirect
from django.views.generic.base import TemplateView

from utdirect.templates import UTDirectContext, UTDirectTemplateAPIError

try:
    module_path, ctx_class = settings.DB_OUTAGE_CONTEXT.rsplit('.',1)
    module = __import__(module_path, fromlist=[ctx_class])
    context = getattr(module, ctx_class)
except AttributeError:
    context = UTDirectContext


class DBOutage(TemplateView):
    template_name = 'db_outage/db_outage.html'

    def get_context_data(self, **kwargs):
        ctx = super(DBOutage, self).get_context_data(**kwargs)
        msg = 'The system is down temporarily. The developers have been notified.'
        ctx.update({'msg':msg})
        try:
            new_context = context(self.request, ctx)
        except UTDirectTemplateAPIError:
            try:
                api_key = settings.API_KEY
            except AttributeError:
                raise ImproperlyConfigured(
                    'If you do not supply your own context object by setting '
                    'a DB_OUTAGE_CONTEXT in settings.py, then you must supply '
                    'an API_KEY in your settings, which will be used to call '
                    'the default UTDirecrContext.'
                )

            new_context = context(
                self.request,
                dict=ctx,
                api_key=api_key,
                page_title='Service Outage',
                window_title='Service Outage',
            )

        return new_context
