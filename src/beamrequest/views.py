from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required

from django.http import Http404, HttpResponse, HttpResponseRedirect

from django.shortcuts import render, get_object_or_404, redirect
from django.forms import modelformset_factory

from .models import BeamRequestModel, IonSpecies, Energys #, BeamModel
from .forms import BeamRequestForm #, BeamForm

from hours.forms import HourRegistrationModel

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
    page_title = 'Add request'
    template_name = 'request/create.html'
    project_code = ''
#    DifbeamsFormset = modelformset_factory(IonSpecies, fields=('Name',))

    if request.method == 'POST':
        form = BeamRequestForm(request.POST)
#        hours = HourRegistrationModel(project_code)
#        formset = DifbeamsFormset(request.POST, request.FILES)
#        beam = BeamForm(request.POST)

#        if form.is_valid()# and beam.is_valid():
        if form.is_valid(): # and formset.is_valid():
            print("all validation passed")
            form = form.save()
#            pc = BeamRequestModel.objects.latest('project_code')
#            print('id: ', pc)
#            hours = hours.save(pc)
            return HttpResponseRedirect("/beamrequest/home")
#            formset = formset.save()
#            beam = beam.save()
#        form = CreateBeamRequestForm()
#        beam = BeamForm()
        else:
            print ("failed")
    else:
        form = BeamRequestForm()
#        formset = DifbeamsFormset()
#        beam = BeamForm()

#    return render(request, template_name, {
#        'form': form,

#})
    context = {"title": page_title, "form": form}
           
    return render(request, template_name, context)

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
def beam_request_detail_page(request, project_code):
    page_title = 'Detail page'
    qs = BeamRequestModel.objects.filter(project_code = project_code)
    template_name = 'request/detail.html'

    context = {'title': page_title, 'object_list': qs}
    return render(request, template_name, context)

#Update view
@staff_member_required
def beam_request_update_page(request, project_code):
    template_name = 'request/update.html'
    obj = get_object_or_404(BeamRequestModel, project_code = project_code)
#    print(obj)
    form = BeamRequestForm(request.POST or None, instance=obj)
    if form.is_valid():
        print(form.cleaned_data)
        form.save()
        return redirect('/beamrequest/home/')

    context = {"title": f"Update {obj.project_code}", 'form': form }
    return render(request, template_name, context)

#Delete view
@staff_member_required
def beam_request_delete_page(request, project_code):
    obj = get_object_or_404(BeamRequestModel, project_code = project_code)
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