from django.shortcuts import render


def index_page(request):

    return render(request, 'CPModel_3/index.html')
