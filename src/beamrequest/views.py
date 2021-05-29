from django.shortcuts import render

from .models import CreateBeamRequestModel,IonSpecies, Energys
from .forms import CreateBeamRequestForm

# Create your views here.
# Create Retrieve Update Delete

#Search/List view
def beam_request_search_page(request):
    template_name = 'beam_request_search.html'
    context = {'object_list': []}
    return render(request, template_name, context)

#Create view
def beam_request_create_page(request):

    page_title = 'Create new Request'
    template_name = 'beam_request_create.html'
    context = {'title': page_title}
    if request.user.is_authenticated:
#      if request.method=='POST':
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

#Retrieve view
def beam_request_retrieve_page(request):
    template_name = 'beam_request_retrieve.html'
    context = {'form': ''}
    return render(request, template_name, context)

#Update view
def beam_request_update_page(request):
    template_name = 'beam_request_update.html'
    context = {'form': ''}
    return render(request, template_name, context)

#Delete view
def beam_request_delete_page(request):
    template_name = 'beam_request_delete.html'
    context = {'form': ''}
    return render(request, template_name, context)

def load_energys(request):
    ionspecies_id = request.GET.get('Ion_Species_id')
    energys = Energys.objects.filter(Ion_Species_id=ionspecies_id).order_by('-name')
    return render(request, 'energys_dropdown_list_options.html', {'energys': energys})