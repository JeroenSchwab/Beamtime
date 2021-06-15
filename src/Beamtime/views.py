from django.http import Http404, HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q
from django.views.generic import TemplateView, ListView


from beamrequest.models import CreateBeamRequestModel
# Create your views here.

#home page
def home_page(request):
    page_title = 'Beamtime registration'
    template_name = 'home.html'
    context = {"title": page_title}
   
    return render(request, template_name, context)

class search_page(TemplateView):
    template_name = 'search.html'


class search_results_page(ListView):
    model = CreateBeamRequestModel
    template_name = 'search_results.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        object_list = CreateBeamRequestModel.objects.filter(
            Q(Project_Code__icontains=query) | Q(Project_Title__icontains=query) | Q(Spokesperson_Name__icontains=query)
        )
        return object_list

#    def get_action(self):
#        action = self.request.GET.get('action')
#        return action

