from django.http import Http404, HttpResponse
from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.

#home page
def home_page(request):
    page_title = 'Beamtime registration'
    template_name = 'home.html'
    context = {"title": page_title}
   
    return render(request, template_name, context)

#def hours_page(request):
#    page_title = 'Hour registration'
#    emplate_name = 'hours.html'
#    context = {"tilte": page_title}

#    return render(request, template_name, context)

#def doc_page(request):
#    page_title = 'Add documents'
#    emplate_name = 'documents.html'
#    context = {"tilte": page_title}

#    return render(request, template_name, context)