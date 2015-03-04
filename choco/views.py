from django.shortcuts import render
from choco.models import *
from django.contrib.auth import logout
from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.contrib.auth.hashers import make_password
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect

# Create your views here.
def index(request):
    chocobos = Chocobo.objects.all()
    #return render_to_response('base.html', {'chocobo': chocobos }, context_instance=RequestContext(request))
    return render(request, 'base.html', {'chocobo': chocobos })
    
def choco_page(request,chocobo_id):
    chocobo = Chocobo.objects.get(pk=chocobo_id)
    return render(request, 'choco_page.html', {'c': chocobo })

def user_page(request, user_id):
    chocobos = Chocobo.objects.all().filter(jockey = user_id)
    #return render_to_response('base.html', {'chocobo': chocobos }, context_instance=RequestContext(request))
    return render(request, 'user.html', {'chocobo': chocobos })    

def logout_view(request):
    logout(request)
    return redirect('home')

def login_view(request):
    error_message = None

    if request.method == 'POST':
        #create new user
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            # return an error message
            error_message = "Login or password was invalid!"


    #display page for logging in
    login_form = LoginForm()
   
    return render(request, 'login.html', dict(login_form=login_form, 
                 error_message=error_message))
                 
def register(request ):                                               
        new_user_form = NewUserForm()
        return render(request, 'register.html', {'new_user_form':new_user_form })
 
                                                
def register_view(request):
    if request.method == 'POST':
        new_user_form = NewUserForm(request.POST)
        if new_user_form.is_valid():
            username = request.POST['username']
            for u in User.objects.all() :
                if username == u.username:
                    error_message = "Username is taken."
                    return register_failed(request, error_message)
            password = make_password(request.POST['password'])
            user = User(username=username, password=password, email="null")
            user.save()
            login_user = authenticate(username=username, password=request.POST['password'])
            return redirect('home')
        else:
            error_message = "There was a problem with your application."
            return register_failed(request, error_message)
    else:
        return redirect('home')