from django.shortcuts import render
from choco.models import *

# Create your views here.
def index(request):
    chocobos = Chocobo.objects.all()
    #return render_to_response('base.html', {'chocobo': chocobos }, context_instance=RequestContext(request))
    return render(request, 'base.html', {'chocobo': chocobos })
    
def choco_page(request,chocobo_id):
    chocobo = Chocobo.objects.get(pk=chocobo_id)
    return render(request, 'choco_page.html', {'c': chocobo })