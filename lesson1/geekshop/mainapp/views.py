from django.shortcuts import render


def index(request):
    return render(request, 'mainapp/products.html')

def contacts(request):
    return render(request, 'geekshop/contact.html')
#
# def index(request):
#     return render(request, 'geekshop/index.html')