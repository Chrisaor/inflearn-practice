from django.shortcuts import render


def Index(request):
    return render(request, 'kilogram/index.html')
