from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required

from django.http import Http404, HttpResponse, HttpResponseRedirect

from django.shortcuts import render, get_object_or_404, redirect
#from django.forms import modelformset_factory

from hours.models import  HourRegistrationModel #, BeamModel CreateBeamRequestModel, IonSpecies, Energys, 
from beamrequest.models import CreateBeamRequestModel
#from .forms import CreateBeamRequestForm #, BeamForm

from django.db.models import Sum
from django.http import JsonResponse
# Create your views here.

#home page
def summary_home_page(request):
    page_title = 'Summary'
    template_name = 'summary/home.html'
    context = {"title": page_title}
   
    return render(request, template_name, context)

def summary_chart_data(request):
    dataset = HourRegistrationModel.objects.values('hours_deliverd').exclude(hours_deliverd='0').annotate(total=Count('hours_deliverd')).order_by('week')

    hours_display_name = dict()
    for hours_tuple in HourRegistrationModel.hours_deliverd: #HOURS_CHOICES:
        hours_display_name[hours_tuple[0]] = hours_tuple[1]
        print(hours_display_name)
    chart = {
        'chart': {'type': 'pie'},
        'title': {'text': 'Hours deliverd per week'},
        'series': [{
            'name': 'Hours',
            'data': list(map(lambda row: {'name': hours_display_name[row['hours_deliverd']], 'y': row['total']}, dataset))
        }]
    }

    return JsonResponse(chart)

def pie_chart(request):
    labels = []
    data = []

    queryset = CreateBeamRequestModel.objects.order_by('Hours')[:10]
    for project_code in queryset:
        labels.append(project_code.Project_Code)
        data.append(project_code.Hours)

    return render(request, 'summary/home.html', {
        'labels': labels,
        'data': data,
    })

def bar_chart(request):
    labels = []
    data = []
#    labels1 = []
    data1 = []

    queryset = CreateBeamRequestModel.objects.values('id', 'Project_Code').annotate(Hours_total=Sum('Hours')).order_by('Project_Code')
#    queryset = HourRegistrationModel.objects.values('project_code', 'hours_deliverd').annotate(Hours_del_total=Sum('hours_deliverd')).order_by('project_code')
    for entry in queryset:
        labels.append(entry['Project_Code'])
        data.append(entry['Hours_total'])

        id = entry['id']
        queryset1 = HourRegistrationModel.objects.values('project_code', 'hours_deliverd').annotate(Hours_del_total=Sum('hours_deliverd')).order_by('project_code').filter(project_code = id)
        for entry1 in queryset1:
            data1.append(entry1['Hours_del_total'])


#        queryset1 = HourRegistrationModel.objects.values('project_code', 'hours_deliverd').annotate(Hours_del_total=Sum('hours_deliverd')).order_by('project_code')
#        for entry1 in queryset1:
#            labels1.append(entry1['hours_deliverd'])
#            data1.append(entry1['Hours_del_total'])
#            hour_del = entry1['hours_deliverd']

#        hour = entry['Hours']
#        Project_Code = entry['Project_Code']
#        print(Project_Code)
#        print(hour)
#        project_code = entry['id']

#        print(project_code)
#        print(hour_del)

    return JsonResponse(data={
        'labels': labels,
        'data': data,
        'data1': data1,
    })

    #def bar_chart(request):
    #labels = []
    #data = []

    #queryset = CreateBeamRequestModel.objects.values('Project_Code').annotate(Hours_total=Sum('Hours')).order_by('Hours')
    #for entry in queryset:
    #    labels.append(entry['Project_Code'])
    #    data.append(entry['Hours_total'])
    
    #return JsonResponse(data={
    #    'labels': labels,
    #    'data': data,
    #})