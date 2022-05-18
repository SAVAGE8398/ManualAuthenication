from django.shortcuts import redirect, render
from signinapp.models import SignDB
# Create your views here.
def index(request):
    return render(request, 'index.html')
def signup(request):
    if request.method == 'POST':
        varEmail = request.POST.get('emailhtml')
        varPassword = request.POST.get('passwordhtml')
        varSubmit=SignDB(PasswordF=varPassword,EmailF=varEmail)
        varSubmit.save()
        return redirect('signin')
    return render(request, 'signup.html')
def signin(request):
    
    return render(request, 'signin.html')
def profile(request):
    return render(request, 'profile.html')
    