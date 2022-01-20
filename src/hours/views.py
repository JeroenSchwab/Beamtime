from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required

from django.http import Http404, HttpResponse, HttpResponseRedirect

from django.shortcuts import render, get_object_or_404, redirect

from django.views.generic import ListView

from .models import HourRegistrationModel
from .forms import HourRegistrationForm

from django.forms import modelformset_factory
from beamrequest.models import BeamRequestModel
from beamrequest.forms import BeamRequestForm

#from .forms import CreateBeamRequestForm

# Create your views here.

#home page
def hours_home_page(request):
    page_title = 'Hour registration'
    template_name = 'hours/home.html'
    context = {"title": page_title}
   
    return render(request, template_name, context)


@staff_member_required
def hours_create_page(request):
    page_title = 'Add hours'
    template_name = 'hours/create.html'

    if request.method == 'POST': # If the form has been submitted...
#            obj = get_object_or_404(BeamRequestModel, project_code = form.project_code)
            form = HourRegistrationForm(request.POST)
#            beamrequest = BeamRequestForm(request.POST)
            
            if form.is_valid():# and beamrequest.is_valid():
                print ("all validation passed")
#                project_code = form.GET.get('project_code')
                form = form.save()
#                obj = get_object_or_404(BeamRequestModel, project_code = project_code)
#                beamrequest = BeamRequestForm(request.POST or None, instance=obj)
#                beamrequest = beamrequest.save()

                return HttpResponseRedirect("/hours/home")
#                    return HttpResponseRedirect("/viewer/%s/" % (hourregistration.name))
            else:
                print ("failed")
    else:
        form = HourRegistrationForm()
#        beamrequest = BeamRequestForm()

    context = {"title": page_title, "form": form}
           
    return render(request, template_name, context)
#    return render(request, template_name, {
#        'form': form,
#        'beamrequest': beamrequest,
#        'project_code': projectcode,
#        'hours': hours_requested,
#})


#Update view
@staff_member_required
def hours_update_page(request):
    page_title = 'Update hours'
    template_name = 'hours/select_date.html'

#    obj = get_object_or_404(HourRegistrationModel, year = "2022")
#    obj = CreateBeamRequestModel.objects.get(Project_Code = project_code)
#    pc_id = obj.id
    #    for pc_id in CreateBeamRequestModel.objects.raw('SELECT id FROM beamrequest_createbeamrequestmodel WHERE Project_code = %s', [project_code]):
#    pc_id = CreateBeamRequestModel.objects.get(Project_Code = project_code)
#    print(obj)
#    print(obj.id)
#    h_id = HourRegistrationModel.objects.get(project_code = pc_id)
#    print(h_id)
    form = HourRegistrationForm(request.POST or None)
#    form = HourRegistrationForm(request.POST or None, instance=pc_id)
    if form.is_valid():
        print(form.cleaned_data)
        form.save()
        return redirect('/hours/home/')

    context = {"title": page_title, 'form': form }
#    context = {"title": page_title, 'form': form }

    return render(request, template_name, context)

#Update view
@staff_member_required
def beam_request_update_page(request, project_code):
    obj = get_object_or_404(BeamRequestModel, project_code = project_code)
#    print(obj)
    form = BeamRequestForm(request.POST or None, instance=obj)
    if form.is_valid():
        print(form.cleaned_data)
        form.save()
        return redirect('/beamrequest/home/')
    template_name = 'request/update.html'
    context = {"title": f"Update {obj.project_code}", 'form': form }
    return render(request, template_name, context)

@staff_member_required
def hbsdagourss_update_page(request):
    page_title = 'Search page'
    template_name = 'select_date.html'
    act = request.GET.get('act')#'update'
    page = request.GET.get('page')

    if request.method == 'GET':
      query = request.GET.get('q')
      act = request.GET.get('act')
      page = request.GET.get('page')
      submitbutton = request.GET.get('submit')

      if query is not None:
        lookups = Q(project_code__icontains=query) | Q(project_title__icontains=query) | Q(spokesperson_name__icontains=query)
        results = BeamRequestModel.objects.filter(lookups).distinct()
#        object_list = CreateBeamRequestModel.objects.filter(
#           Q(Project_Code__icontains=query) | Q(Project_Title__icontains=query) | Q(Spokesperson_Name__icontains=query)
#        ) # queryset -> list of python objects

#        context = {'title': page_title, 'object_list': object_list, 'submitbutton': submitbutton }
        context = {'title': page_title, 'results': results, 'submitbutton': submitbutton, "action": act, "page": page} #, 'page': page
        return render(request, template_name, context)
      else:
        context = {'title': page_title} #, 'page': page
        return render(request, template_name, context)
    else:
        context = {'title': page_title}#, 'page': page
        return render(request, template_name, context)