from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseForbidden, HttpResponseBadRequest


def index(request):
    return render(request, "index.html")

def top(request):
    return render(request, "top.html")

codes = {"bb": "1AbAbAbAb","dance":"2AbAbAbAb","tir":"3AbAbAbAb","mem":"4AbAbAbAb","laser":"5AbAbAbAb","lava":"6AbAbAbAb"} #должен барть код(индивидуальный номер) игры из БД
#создается QR-код и посылается на площдку в столбик
def game(request,key):
    if key == codes["bb"]:
        return render(request,"bb.html")
    elif key == codes["dance"]:
        return render(request,"dance.html")
    elif key == codes["tir"]:
        return render(request, "tir.html")
    elif key == codes["mem"]:
        return render(request, "mem.html")
    elif key == codes["laser"]:
        return render(request, "laser.html")
    elif key == codes["lava"]:
        return render(request, "lava.html")
    else:
        return HttpResponseForbidden("Неверный игровой ключ")

def games(request):
    return render(request, "games.html")
