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

#class search_page(TemplateView):
#    page_title = 'Search'
#    template_name = 'search.html'
#    context = {"title": page_title}
    
#    return render(request, template_name, context)

#class search_results_page(ListView):
#    model = CreateBeamRequestModel
#    template_name = 'search_results.html'

#    def get_queryset(self):
#        query = self.request.GET.get('q')
#        object_list = CreateBeamRequestModel.objects.filter(
#            Q(Project_Code__icontains=query) | Q(Project_Title__icontains=query) | Q(Spokesperson_Name__icontains=query)
#        )
#        return object_list

#    def get_action(self):
#        action = self.request.GET.get('action')
#        return action

#Search/List view
def search_page(request):
    page_title = 'Search page'
    template_name = 'search.html'
    act = request.GET.get('act')#'update'
    page = request.GET.get('page')

    if request.method == 'GET':
      query = request.GET.get('q')
      act = request.GET.get('act')
      page = request.GET.get('page')
      submitbutton = request.GET.get('submit')

      if query is not None:
        lookups = Q(Project_Code__icontains=query) | Q(Project_Title__icontains=query) | Q(Spokesperson_Name__icontains=query)
        results = CreateBeamRequestModel.objects.filter(lookups).distinct()
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


#def searchposts(request):
#    if request.method == 'GET':
#        query= request.GET.get('q')

 #       submitbutton= request.GET.get('submit')

  #      if query is not None:
  #          lookups= Q(title__icontains=query) | Q(content__icontains=query)

#            results= Post.objects.filter(lookups).distinct()

#            context={'results': results, 'submitbutton': submitbutton}

#            return render(request, 'search/search.html', context)

#        else:
#            return render(request, 'search/search.html')

#    else:
#        return render(request, 'search/search.html')
