from django.shortcuts import render


def index_page(request):

    return render(request, 'CPModel_1/index.html')
