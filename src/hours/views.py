from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required

from django.http import Http404, HttpResponse, HttpResponseRedirect

from django.shortcuts import render, get_object_or_404, redirect

from .models import HourRegistrationModel, Operators, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday, Day, HourRegModel
from .forms import HourRegistrationForm, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday, Day, HourRegForm

from django.forms import modelformset_factory
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
    operators = Operators.objects.all()
    days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
  
    if request.method == 'POST': # If the form has been submitted...
            hourregistration_form = HourRegistrationForm(request.POST, prefix = "hourregistration")
            monday_form = Monday(request.POST, prefix = "monday")
            tuesday_form = Tuesday(request.POST, prefix = "tuesday")
            wednesday_form = Wednesday(request.POST, prefix = "wednesday")
            thursday_form = Thursday(request.POST, prefix = "thursday")
            friday_form = Friday(request.POST, prefix = "friday")
            saturday_form = Saturday(request.POST, prefix = "saturday")
            sunday_form = Sunday(request.POST, prefix = "sunday")

            if hourregistration_form.is_valid() and monday_form.is_valid() and tuesday_form.is_valid() and wednesday_form.is_valid() and thursday_form.is_valid() and friday_form.is_valid() and saturday_form.is_valid() and sunday_form.is_valid(): # All validation rules pass
                    print ("all validation passed")
                    hourregistration = hourregistration_form.save()

                    monday_form.cleaned_data["hourregistration"] = hourregistration
                    monday = monday_form.save()

                    tuesday_form.cleaned_data["hourregistration"] = hourregistration
                    tuesday = tuesday_form.save()

                    wednesday_form.cleaned_data["hourregistration"] = hourregistration
                    wednesday = wednesday_form.save()

                    thursday_form.cleaned_data["hourregistration"] = hourregistration
                    thursday = thursday_form.save()

                    friday_form.cleaned_data["hourregistration"] = hourregistration
                    friday = friday_form.save()

                    saturday_form.cleaned_data["hourregistration"] = hourregistration
                    saturday = saturday_form.save()

                    sunday_form.cleaned_data["hourregistration"] = hourregistration
                    sunday = sunday_form.save()                    

                    return HttpResponseRedirect("/hours/home")
#                    return HttpResponseRedirect("/viewer/%s/" % (hourregistration.name))
            else:
                    print ("failed")

    else:
        hourregistration_form = HourRegistrationForm(prefix = "hourregistration")
        monday_form = Monday(prefix = "monday")
        tuesday_form = Tuesday(prefix = "tuesday") #prefix = "tuesday"
        wednesday_form = Wednesday(prefix = "wednesday")
        thursday_form = Thursday(prefix = "thursday")
        friday_form = Friday(prefix = "friday")
        saturday_form = Saturday(prefix = "saturday")
        sunday_form = Sunday(prefix = "sunday")

    return render(request, 'hours/create.html', {
        'form': hourregistration_form,
        'monday_form': monday_form,
        'tuesday_form': tuesday_form,
        'wednesday_form': wednesday_form,
        'thursday_form': thursday_form,
        'friday_form': friday_form,
        'saturday_form': saturday_form,
        'sunday_form': sunday_form,
        'operators_list': operators,
        'days_list': days,
        })



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


#### test erea

@staff_member_required
def hours_test_page(request):
    page_title = 'Hour registration'
    template_name = 'hours/test.html'
    operators = Operators.objects.all()
    days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    DayFormSet = modelformset_factory(Day, fields =['Day_Shift', 'Evening_Shift', 'Night_Shift', 'Beam', 'Source', 'Customer', 'Project_Code', 'Scheduled_Hours', 'Delivered_Hours', 'Notes'], extra = 7)
    formset = DayFormSet(prefix='weekday')  

    if request.method == 'POST': # If the form has been submitted...
            hourreg_form = HourRegForm(request.POST, prefix = "hourregistration")
            
            DayFormSet = modelformset_factory(Day, fields =['Day_Shift', 'Evening_Shift', 'Night_Shift', 'Beam', 'Source', 'Customer', 'Project_Code', 'Scheduled_Hours', 'Delivered_Hours', 'Notes'], extra = 7)
            formset = DayFormSet(prefix='weekday')
#            day_form = Day(request.POST, prefix = "sunday")

            if hourreg_form.is_valid() and day_form.is_valid(): #and tuesday_form.is_valid() and wednesday_form.is_valid() and thursday_form.is_valid() and friday_form.is_valid() and saturday_form.is_valid() and sunday_form.is_valid(): # All validation rules pass
                    print ("all validation passed")
                    hourreg = hourreg_form.save()


#                    day_form.cleaned_data["hourregistration"] = hourregistration
#                    day = day_form.save()                    

                    return HttpResponseRedirect("/hours/home")
#                    return HttpResponseRedirect("/viewer/%s/" % (hourregistration.name))
            else:
                    print ("failed")

    else:
        hourreg_form = HourRegForm(prefix = "hourregistration")
#        day_form = Day(prefix = "sunday")
#        context['formset']= formset

    return render(request, 'hours/create.html', {
        'form': hourreg_form,
    #    'day_form': day_form,
        'operators_list': operators,
        'days_list': days,
        'formset': formset,
        })

def formset_view(request):
    context ={}
  
    # creating a formset
    DayFormSet = modelformset_factory(Day, fields =['Day_Shift', 'Evening_Shift', 'Night_Shift', 'Beam', 'Source', 'Customer', 'Project_Code', 'Scheduled_Hours', 'Delivered_Hours', 'Notes'], extra = 7)
    formset = DayFormSet(prefix='weekday')
      
    # Add the formset to context dictionary
    context['formset']= formset
    return render(request, "hours/test.html", context)