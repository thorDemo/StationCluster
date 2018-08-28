from django.shortcuts import render


def index_page(request):
    print(request.META.get('HTTP_X_FORWARDED_HOST'))
    return render(request, 'CPModel_2/index.html')
