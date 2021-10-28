from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required

from django.http import Http404, HttpResponse

from django.shortcuts import render, get_object_or_404, redirect
from django.forms import modelformset_factory

from .models import CreateBeamRequestModel, IonSpecies, Energys #, BeamModel
from .forms import CreateBeamRequestForm #, BeamForm

# Create your views here.

#home page
def beam_request_home_page(request):
    page_title = 'Beam Request'
    template_name = 'request/home.html'
    context = {"title": page_title}
   
    return render(request, template_name, context)

#@login_required
#Create view
@staff_member_required
def beam_request_create_page(request):
    page_title = 'Create new Request'
    template_name = 'request/create.html'
#    DifbeamsFormset = modelformset_factory(IonSpecies, fields=('Name',))

    if request.method == 'POST':
        form = CreateBeamRequestForm(request.POST)
#        formset = DifbeamsFormset(request.POST, request.FILES)
#        beam = BeamForm(request.POST)

#        if form.is_valid()# and beam.is_valid():
        if form.is_valid() and formset.is_valid():
            print("all validation passed")
            form = form.save()
#            formset = formset.save()
#            beam = beam.save()
#        form = CreateBeamRequestForm()
#        beam = BeamForm()
        else:
            print ("failed")
    else:
        form = CreateBeamRequestForm()
#        formset = DifbeamsFormset()
#        beam = BeamForm()

    return render(request, template_name, {
        'form': form,
#        'formset': formset,
#        'beam': beam,
})
#    context = {"title": page_title, "form": form, "beam": beam}
           
#    return render(request, template_name, context)

#    def generatescripts(request):
#    if request.method == 'POST':
#        Steps = request.POST.getlist('Step')
#        Results = request.POST.getlist('Result')
#        Descriptions = request.POST.getlist('Description')

#        # FIXME: number of each field should equal
#        c = min([len(Steps), len(Results), len(Descriptions)])
#        for i in range(c):
#            # create a form instance and populate it with data from the request:
#            form = GenerateScriptsForm({'Step': Steps[i], 'Result': Results[i], 'Description': Descriptions[i]})
#            # check whether it's valid:
#            if form.is_valid():
#                form.save()
#        return HttpResponseRedirect('/thanks/')

#    else:
#        form = GenerateScriptsForm()

#    return render(request, 'page/generatescripts.html', {'form': form})

#Retrieve view show 1 object/details
@staff_member_required
def beam_request_detail_page(request, Project_Code):
    page_title = 'Detail page'
    qs = CreateBeamRequestModel.objects.filter(Project_Code = Project_Code)
    template_name = 'request/detail.html'

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
    template_name = 'request/update.html'
    context = {"title": f"Update {obj.Project_Code}", 'form': form }
    return render(request, template_name, context)

#Delete view
@staff_member_required
def beam_request_delete_page(request, Project_Code):
    obj = get_object_or_404(CreateBeamRequestModel, Project_Code = Project_Code)
    page_title = 'Delete Request'
    template_name = 'request/delete.html'
    if request.method == "POST":
        obj.delete()
        return redirect('/beamrequest/home/')
    context = {'object': obj}
    return render(request, template_name, context)

def beam_request_dif_beams(request):
    DifbeamsFormset = modelformset_factory(IonSpecies, Energys, fields=('name', 'name'))
    if request.method == 'POST':
        formset = DifbeamsFormset(request.POST, request.FILES)
        if formset.is_valid():
            formset.save()

        else:
            formset = DifbeamsFormset()
        return render(request, 'template_name', {'formset': formset})


#from django.forms import modelformset_factory
#from django.shortcuts import render
#from myapp.models import Author

#def manage_authors(request):
#    AuthorFormSet = modelformset_factory(Author, fields=('name', 'title'))
#    if request.method == 'POST':
#        formset = AuthorFormSet(request.POST, request.FILES)
#        if formset.is_valid():
#            formset.save()
#            # do something.
#    else:
#        formset = AuthorFormSet()
#    return render(request, 'manage_authors.html', {'formset': formset})