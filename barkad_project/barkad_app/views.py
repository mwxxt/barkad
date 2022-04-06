from django.shortcuts import render


def index(request):
    return render(request, "barkad_app/index.html")


def about_us(request):
    return render(request, "barkad_app/about_us.html")


def authorization(request):
    return render(request, "barkad_app/authorization.html")


def registration(request):
    return render(request, "barkad_app/registration.html")


def feedback(request):
    return render(request, "barkad_app/feedback.html")


def products(request):
    return render(request, "barkad_app/allproducts.html")


def concrete_product(request):
    return render(request, "barkad_app/product.html")
