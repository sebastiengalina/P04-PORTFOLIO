# Django
from django.http import HttpResponse
from django.template import loader, RequestContext
from django.shortcuts import get_object_or_404

# Portfolio App
from models import Project
from models import Tag


def index(request):
    data = {"projects": Project.objects.all(),
            "tags": Tag.objects.all()}
    t = loader.get_template("index.html")
    c = RequestContext(request, data)
    return HttpResponse(t.render(c))


def project(request, slug):
    p = get_object_or_404(Project, slug__exact=slug)
    data = {"project": p}
    t = loader.get_template("project.html")
    c = RequestContext(request, data)
    return HttpResponse(t.render(c))


def tag(request, slug):
    data = {"projects": Project.objects.filter(tags__name__contains=slug),
            "tag": slug,
            "tags": Tag.objects.all()}
    t = loader.get_template("tag.html")
    c = RequestContext(request, data)
    return HttpResponse(t.render(c))


def about(request):
    data = {}
    t = loader.get_template("about.html")
    c = RequestContext(request, data)
    return HttpResponse(t.render(c))
