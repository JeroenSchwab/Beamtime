from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required

from django.http import Http404, HttpResponse

from django.shortcuts import render, get_object_or_404, redirect


from .models import CreateBeamRequestModel, IonSpecies, Energys
from .forms import CreateBeamRequestForm

# Create your views here.

#home page
def beam_request_home_page(request):
    page_title = 'Beam Request'
    template_name = 'beam_request_home.html'
    context = {"title": page_title}
   
    return render(request, template_name, context)

#Search/List view
#@staff_member_required
#def beam_request_search_page(request):
#    page_title = 'Search page'
#    qs = CreateBeamRequestModel.objects.all() # queryset -> list of python objects
#    template_name = 'beam_request_search.html'
#    context = {'title': page_title, 'object_list': qs}
#    return render(request, template_name, context)

#@login_required
#Create view
@staff_member_required
def beam_request_create_page(request):
    page_title = 'Create new Request'
    template_name = 'beam_request_create.html'

    form = CreateBeamRequestForm(request.POST or None)
    if form.is_valid():
        print(form.cleaned_data)
        form.save()
        form = CreateBeamRequestForm()
    context = {"title": page_title, "form": form}
           
    return render(request, template_name, context)


#Retrieve view show 1 object/details
@staff_member_required
def beam_request_detail_page(request, Project_Code):
    page_title = 'Detail page'
    qs = CreateBeamRequestModel.objects.filter(Project_Code = Project_Code)
    template_name = 'beam_request_detail.html'

    context = {'title': page_title, 'object_list': qs}
    return render(request, template_name, context)

#Update view
@staff_member_required
def beam_request_update_page(request, Project_Code):
    obj = get_object_or_404(CreateBeamRequestModel, Project_Code = Project_Code)
    form = CreateBeamRequestForm(request.POST or None, instance=obj)
    if form.is_valid():
        print(form.cleaned_data)
        form.save()
        return redirect('/beamrequest/home/')
    template_name = 'beam_request_update.html'
    context = {"title": f"Update {obj.Project_Code}", 'form': form }
    return render(request, template_name, context)

#Delete view
@staff_member_required
def beam_request_delete_page(request, Project_Code):
    obj = get_object_or_404(CreateBeamRequestModel, Project_Code = Project_Code)
    page_title = 'Delete Request'
    template_name = 'beam_request_delete.html'
    if request.method == "POST":
        obj.delete()
        return redirect('/beamrequest/home/')
    context = {'object': obj}
    return render(request, template_name, context)