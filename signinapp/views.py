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
    if request.method=='POST':
        varEmail = request.POST.get('emailhtml')
        varPassword= request.POST.get('passwordhtml')
        try:
            varlogin=SignDB.objects.get(EmailF=varEmail,PasswordF=varPassword)
        except SignDB.DoesNotExist:
            return render(request, 'signin.html') 
        else:
            request.session['LoginID']=varlogin.id  
            return redirect('profile')    
    
    return render(request, 'signin.html')
def profile(request):
    if (request.session.get('LoginID')):
        loginid=request.session.get('LoginID')
        d1=SignDB.objects.get(id=loginid)
        return render(request, "profile.html", {"sessionid":d1})
    else:
        return render(request, 'signin.html')
    