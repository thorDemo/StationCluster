from django.utils.deprecation import MiddlewareMixin
from django.conf import settings


class MultipleDomainMiddleware(MiddlewareMixin):
    """
    作者：HelloJames
    链接：https://www.jianshu.com/p/a503cbc1505a
    來源：简书
    """
    def process_request(self, request):
        host = request.META.get('HTTP_X_FORWARDED_HOST')
        # print(host)
        # print(request.META)
        url_config = getattr(settings, 'MULTIPLE_UFL_CONFIG', None)

        if url_config:
            for key in url_config.keys():
                if key in host:
                    request.urlconf = url_config[key]

