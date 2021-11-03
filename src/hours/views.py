from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required

from django.http import Http404, HttpResponse, HttpResponseRedirect

from django.shortcuts import render, get_object_or_404, redirect

from django.views.generic import ListView

from .models import HourRegistrationModel
from .forms import HourRegistrationForm

from django.forms import modelformset_factory
from beamrequest.models import CreateBeamRequestModel
from beamrequest.forms import CreateBeamRequestForm

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
    page_title = 'Hour registration'
    template_name = 'hours/create.html'

#    data = CreateBeamRequestModel.objects.all()
#    projectcode = {"Project_Code": data}
#    projectcode = CreateBeamRequestModel.objects.all()
#    hours_requested = {"Hours": data}

#    operators = Operators.objects.all()
  
    if request.method == 'POST': # If the form has been submitted...
            form = HourRegistrationForm(request.POST)
            
            if form.is_valid():
                print ("all validation passed")
                form = form.save()

                return HttpResponseRedirect("/hours/home")
#                    return HttpResponseRedirect("/viewer/%s/" % (hourregistration.name))
            else:
                print ("failed")
    else:
        form = HourRegistrationForm()
        
    return render(request, template_name, {
        'form': form,
#        'project_code': projectcode,
#        'hours': hours_requested,
})


#Update view
@staff_member_required
def hours_update_page(request, project_code):
#    obj = get_object_or_404(CreateBeamRequestModel, Project_Code = project_code)
    pc_id = CreateBeamRequestModel.objects.get(Project_Code = project_code)
    print(pc_id)
    h_id = pc_id
    print(h_id)
#    form = HourRegistrationForm(request.POST or None, instance=obj)
    form = HourRegistrationForm(request.POST or None, instance=pc_id)
    if form.is_valid():
        print(form.cleaned_data)
        form.save()
        return redirect('/hours/home/')
    template_name = 'hours/update.html'
    #context = {"title": f"Update {obj.Project_Code}", 'form': form }
    context = {"title": f"Update {project_code}", 'form': form }
    return render(request, template_name, context)

