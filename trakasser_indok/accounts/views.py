from django.shortcuts import redirect, render
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout

# Create your views here.
def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            #log the user inn
            return redirect('indoker:list')
    else:
        form = UserCreationForm()
    return render(request, 'accounts/signup.html', {
    'form': form
    })

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            if'next'in request.POST:
                return redirect(request.POST.get('next'))
            else:
                return redirect('indoker:list')
    else:
        form = AuthenticationForm()
    return render(request, "accounts/login.html", {
        'form': form
    })

def logout_view(request):
    logout(request)
    return redirect('indoker:list')