from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required

from django.http import Http404, HttpResponse

from .forms import Add_file_form
from .models import Add_file_model

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


FILE_TYPES = ['png', 'jpg', 'jpeg', 'doc', 'pdf', 'txt']

def add_file(request):
    form = Add_file_form()
    if request.method == 'POST':
        form = Add_file_form(request.POST, request.FILES)
        if form.is_valid():
            add_fl = form.save(commit=False)
            add_fl.file = request.FILES['file']
            file_type = add_fl.file.url.split('.')[-1]
            file_type = file_type.lower()
            if file_type not in FILE_TYPES:
                return render(request, 'documentation/error.html')
        add_fl.save()
        return render(request, 'documentation/details.html', {'add_fl': add_fl})
    context = {"form": form,}
    return render(request, 'documentation/create.html', context)