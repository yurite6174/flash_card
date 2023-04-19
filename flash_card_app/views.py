from django.shortcuts import render


def index(request):
    return render(request, "flash_card_app/index.html")
