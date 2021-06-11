from django.http import Http404, HttpResponse
from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.

#main page
def main_page(request):
    page_title = 'Beamtime registration'
    template_name = 'main.html'
    context = {"title": page_title}
   
    return render(request, template_name, context)

    #login page
#def login_page(request):
#    page_title = 'Login'
#    template_name = 'registration/login.html'
#    context = {"title": page_title}
   
#    return render(request, template_name, context)