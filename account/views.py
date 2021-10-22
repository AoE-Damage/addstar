# from addstar.account.models import bloggers
from django.http.response import HttpResponse
from django.shortcuts import render
from .filters import BloggerFilter
from .models import bloggers, zayavki

# Create your views here.


def home(request):
    context = {}
    return render(request, "account/main.html", context)


def search(request):

    blogger = bloggers.objects.all()
    myFilter = BloggerFilter(request.GET, queryset=blogger)
    blogger = myFilter.qs
    context = {"bloggers": blogger, "myFilter": myFilter}
    return render(request, "account/search.html", context)


def contact(request):
    context = {}
    return render(request, "account/contact.html", context)


def contact_blogger(request, pk):
    blogger = bloggers.objects.get(id=pk)
    context = {"blogger": blogger}
    if request.method == "POST":
        zayavka = zayavki()
        name = request.POST.get("contact-name")
        phone_number = request.POST.get("contact-phone-number")
        text = request.POST.get("contact-text")
        zayavka.name = name
        zayavka.text = text
        zayavka.phone_number = phone_number
        zayavka.save()

        return render(request, "account/success.html")

    return render(request, "account/contact_blogger.html", context)


def success(request):
    return render(request, "account/success.html")
