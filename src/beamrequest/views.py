from django.shortcuts import render

from .models import CreateBeamRequestModel, IonSpecies, Energys
from .forms import CreateBeamRequestForm

# Create your views here.
# Create Retrieve Update Delete

#Search/List view
def beam_request_search_page(request):
    page_title = 'List/Search page'
    qs = CreateBeamRequestModel.objects.all() # queryset -> list of python objects
    template_name = 'beam_request_search.html'
    context = {'title': page_title, 'object_list': qs}
    return render(request, template_name, context)

#Create view
def beam_request_create_page(request):
    page_title = 'Create new Request'
    template_name = 'beam_request_create.html'
    context = {'title': page_title}
    if request.user.is_authenticated:
#      if request.method == 'POST':
       form = CreateBeamRequestForm(request.POST or None)
       if form.is_valid():
         form.save()
#         obj = CreateBeamRequest.objects.create(**form.cleaned_data)
         form = CreateBeamRequestForm
       context = {
           "title": page_title,
           "form": form
       }
       return render(request, template_name, context)
    else:
       return render(request, 'login.html')

#Retrieve view show 1 object/details
def beam_request_detail_page(request):
    page_title = 'Detail page'
    template_name = 'beam_request_detail.html'
    context = {'title': page_title, 'form': ''}
    return render(request, template_name, context)

#Update view
def beam_request_update_page(request):
    page_title = 'Updates Request'
    template_name = 'beam_request_update.html'
    context = {'form': ''}
    return render(request, template_name, context)

#Delete view
def beam_request_delete_page(request):
    page_title = 'Delete Request'
    template_name = 'beam_request_delete.html'
    context = {'form': ''}
    return render(request, template_name, context)






