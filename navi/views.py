from common.mymako import render_mako_context
from navi import models

# Create your views here.

def index(request):
    temp_name = "navi/navi-header.html"
    allnavi = models.navi.objects.all()
    return render_mako_context(request, "navi/index.html", locals())

def add(request):
    # if request.method == "POST":
    return render_mako_context(request, "navi/add.html")