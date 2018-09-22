from django.utils.deprecation import MiddlewareMixin
from django.conf import settings
from CPModel_2.models import DomainConf


class MultipleDomainMiddleware(MiddlewareMixin):

    def process_request(self, request):
        host = request.META.get('HTTP_X_FORWARDED_HOST')
        # print(host)
        # print(request.META)
        # url_config = getattr(settings, 'MULTIPLE_UFL_CONFIG', None)
        domain_conf = DomainConf.objects.all()
        if domain_conf:
            for key in domain_conf:
                if key.domain in host:
                    request.urlconf = key.Template

