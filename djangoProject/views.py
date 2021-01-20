import django.shortcuts as sc
from . import settings as sett


def home(request):
    return sc.render(request, "djangoProject/index.html", context={'key': sett.STATIC_URL})
