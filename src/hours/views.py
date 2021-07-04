from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required

from django.http import Http404, HttpResponse

from django.shortcuts import render, get_object_or_404, redirect

from .models import HourRegistrationModel, Operators, Monday, Tuesday
from .forms import HourRegistrationForm, Monday, Tuesday

from beamrequest.models import CreateBeamRequestModel

#from .forms import CreateBeamRequestForm

# Create your views here.

#home page
def hours_home_page(request):
    page_title = 'Hour registration'
    template_name = 'hours/home.html'
    context = {"title": page_title}
   
    return render(request, template_name, context)


#create page    
#@staff_member_required
#def hours_create_page(request):
#    page_title = 'Hour registration'
#    template_name = 'hours/create.html'
#    qs = Operators.objects.all()

#    form = HourRegistrationForm(request.POST or None)
#    if form.is_valid():
#        print(form.cleaned_data)
#        form.save()
#        form = HourRegistrationForm()
#    context = {"title": page_title, "form": form, 'object_list': qs}
    
#    return render(request, template_name, context)


@staff_member_required
def hours_create_page(request):
    page_title = 'Hour registration'
    template_name = 'hours/create.html'
    qs = Operators.objects.all()
  
    if request.method == 'POST': # If the form has been submitted...
            hourregistration_form = HourRegistrationForm(request.POST, prefix = "hourregistration")
            monday_form = Monday(request.POST, prefix = "monday")
#            tuesday_form = Tuesday(request.POST, prefix = "tuesday")
            if hourregistration_form.is_valid() and monday_form.is_valid():# and tuesday_form.is_valid(): # All validation rules pass
                    print ("all validation passed")
                    hourregistration = hourregistration_form.save()
                    monday_form.cleaned_data["hourregistration"] = hourregistration
                    monday = monday_form.save()
#                    tuesday_form.cleaned_data["hourregistration"] = hourregistration
#                    tuesday = tuesday_form.save()
#                    return HttpResponseRedirect("/viewer/%s/" % (hourregistration.name))
            else:
                    print ("failed")

    else:
        hourregistration_form = HourRegistrationForm(prefix = "hourregistration")
        monday_form = Monday(prefix = "monday")
#        tuesday_form = Tuesday(prefix = "tuesday")
    return render(request, 'hours/create.html', {'form': hourregistration_form, 'monday_form': monday_form, 'object_list': qs}) # 'tuesday_form': tuesday_form,





# class PrimaryForm(ModelForm):
#        class Meta:
#            model = Primary
#
#    class BForm(ModelForm):
#        class Meta:
#            model = B
#            exclude = ('primary',)
#
#    class CForm(ModelForm):
#         class Meta:
#            model = C
#            exclude = ('primary',)
#
#    def generateView(request):
#        if request.method == 'POST': # If the form has been submitted...
#            primary_form = PrimaryForm(request.POST, prefix = "primary")
#            b_form = BForm(request.POST, prefix = "b")
#            c_form = CForm(request.POST, prefix = "c")
#            if primary_form.is_valid() and b_form.is_valid() and c_form.is_valid(): # All validation rules pass
#                    print "all validation passed"
#                    primary = primary_form.save()
#                    b_form.cleaned_data["primary"] = primary
#                    b = b_form.save()
#                    c_form.cleaned_data["primary"] = primary
#                    c = c_form.save()
#                    return HttpResponseRedirect("/viewer/%s/" % (primary.name))
#            else:
#                    print "failed"
#
#        else:
#            primary_form = PrimaryForm(prefix = "primary")
#            b_form = BForm(prefix = "b")
#            c_form = Form(prefix = "c")
#     return render_to_response('multi_model.html', {
#     'primary_form': primary_form,
#     'b_form': b_form,
#     'c_form': c_form,
#      })