from django.shortcuts import render, HttpResponse


def home(request):
    return HttpResponse("成功")


def news(request, nid):
    print(nid)
    page = request.GET.get("page")
    return HttpResponse("新闻")


def article(request):
    nid = request.GET.get("nid")
    print(nid)
    return HttpResponse("文章")