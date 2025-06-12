from django.shortcuts import render


def Index(request):
    """ View to render the index page """

    return render(request, 'home/index.html')
