from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required

from django.http import Http404, HttpResponse

from django.shortcuts import render, get_object_or_404, redirect

from .models import HourRegistrationModel
from .forms import HourRegistrationForm

from beamrequest.models import CreateBeamRequestModel
from .models import Operators
#from .forms import CreateBeamRequestForm

# Create your views here.

#home page
def hours_home_page(request):
    page_title = 'Hour registration'
    template_name = 'hours/home.html'
    context = {"title": page_title}
   
    return render(request, template_name, context)


#cfreate page    
@staff_member_required
def hours_create_page(request):
    page_title = 'Hour registration'
    template_name = 'hours/create.html'
    qs = Operators.objects.all()

    form = HourRegistrationForm(request.POST or None)
    if form.is_valid():
        print(form.cleaned_data)
        form.save()
        form = HourRegistrationForm()
    context = {"title": page_title, "form": form, 'object_list': qs}
    
    return render(request, template_name, context)

