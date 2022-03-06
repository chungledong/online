from django.shortcuts import render

# Create your views here.
# Create your views here.
def homeView(request):
    template_name = 'home.html'
    return render(request, template_name, {} )