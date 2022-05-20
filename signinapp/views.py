from django.shortcuts import redirect, render
from signinapp.models import SignDB
# Create your views here.
def index(request):
    if(request.session.get('uid')):
        uid=request.session['uid']
        d1=SignDB.objects.get(id=uid)
        
        return render(request, 'index.html',{'uid':d1})
    
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
            u=SignDB.objects.get(EmailF=varEmail,PasswordF=varPassword)
        except SignDB.DoesNotExist:
            return render(request, 'signin.html') 
        else:
            request.session['uid']=u.id  
            return redirect('profile')    
    
    return render(request, 'signin.html')

def profile(request):
    if(request.session.get('uid')):
        uid=request.session['uid']
        d1=SignDB.objects.get(id=uid)
        return render(request,'profile.html',{'uid':d1})
    else:
        return render(request,'signin.html')
    

def logout(request):
    try:
        del request.session['uid']    
    except KeyError:        
        pass
    return redirect('signin')