from django.shortcuts import render
from django.views.generic import TemplateView

def main_main(request):
    sarlavha = "Main"
    return render(request, "main.html", context={
        "page_title": sarlavha,
    })
def main_index(request):
    sarlavha = "Main"
    return render(request, "index.html", context={
        "page_title": sarlavha,
    })
def main_info(request):
    sarlavha = "Main"
    return render(request, "info.html", context={
        "page_title": sarlavha,
    })
