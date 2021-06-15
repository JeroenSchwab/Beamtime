from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required

from django.http import Http404, HttpResponse

from django.shortcuts import render, get_object_or_404, redirect


#from .models import CreateBeamRequestModel, IonSpecies, Energys
#from .forms import CreateBeamRequestForm

# Create your views here.
@staff_member_required
def documentation_home_page(request):
    page_title = 'Documentation'
    template_name = 'documentation/home.html'
    context = {"tilte": page_title}

    return render(request, template_name, context)