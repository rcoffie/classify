from django.shortcuts import render
from django.contrib.auth import login, authenticate
from .forms import SignUpForm
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required


# Create your views here.

@login_required(login_url='signup')
def dashboard(request):

    return render(request, 'user_engine/dashboard.html')

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.info(request,(f'welcome {username}'))
            return redirect('dashboard')
    else:
        form = SignUpForm()
    return render(request, 'user_engine/signup.html', {'form':form})


def login_request(request):
	if request.method == "POST":
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				messages.info(request,(f'welcome {username}'))
				return redirect("dashboard")
			else:
				messages.warning('invalid username or password')
		else:
			messages.warning(request,'invalid username or password')
	form = AuthenticationForm()
	return render(request, 'user_engine/login_request.html',{'form':form})

