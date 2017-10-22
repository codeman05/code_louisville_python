from django.shortcuts import render


def site_homepage(request):
    return render(request, 'site_homepage.html')
