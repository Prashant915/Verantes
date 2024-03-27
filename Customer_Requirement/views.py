from django.shortcuts import render,redirect
from .models import *
from django.contrib.auth import logout,login
from .models import Profile
from django.contrib.auth.models import User
import random
from django.core.mail import send_mail
from django.conf import settings
from datetime import datetime, timedelta


def contact_form(request):
    if request.method == "POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        phone=request.POST.get('phonenumber')
        city=request.POST.get('city')
        looking_for=request.POST.get('product')
        budget=request.POST.get('budget')
        data=Customer_Detail(Name=name,Email=email,Phone_Number=phone,City=city,Looking_For=looking_for,Budget=budget)
        data.save()
        return redirect('/thankyou/')
    return render(request,'contact.html')

def signup(request):
    if request.method=='POST':
        name=request.POST['signame']
        mobile=request.POST['sigphonenumber']
        try:
            whatsapp=request.POST['whatsapp']
        except:
            whatsapp="off"
        email=request.POST['sigemail']
        pincode=request.POST['sigpincode']
        check_user=User.objects.filter(email=email).first()
        check_profile=Profile.objects.filter(mobile=mobile).first()
        if check_user or check_profile:
            context={'message':'Mobile already exist','class':'danger'}
            return render(request,'index.html',context)
        else:
            request.session['name']=name
            request.session['mobile']=mobile
            request.session['whatsapp']=whatsapp
            request.session['email']=email
            request.session['pincode']=pincode

            valid_until=str(datetime.now() + timedelta(minutes=1))
            request.session['valid_until']=valid_until
            otp=str(random.randint(100000,999999))
            request.session['otpp']=otp

            subject="Verantes account verification email"
            message=f'Your Registration of verantes account otp is {otp}'
            email_from=settings.EMAIL_HOST
            send_mail(subject,message,email_from,[email],fail_silently=False)
            return redirect('/signup-otp/')
    return render(request,'index.html')

def login_attempt(request):
    if not request.user.is_authenticated:
        if request.method=="POST":
            number=request.POST.get('logphonenumber')
            auth=Profile.objects.filter(mobile=number).first()
            
            if auth is not None:
                email=auth.email
                valid_until=str(datetime.now() + timedelta(minutes=1))
                otp=str(random.randint(100000,999999))
                request.session['valid_until']=valid_until
                request.session['mobile']=number
                request.session['email']=email
                request.session['otpp']=otp
                subject="Verantes account verification email"
                message=f'Your otp is {otp}'
                email_from=settings.EMAIL_HOST
                send_mail(subject,message,email_from,[email],fail_silently=False)
                return redirect('/login-otp/')
            if auth is None:
                print("error occured!!")
                return redirect('/login/')
        return render(request,'index.html')
    else:
        return render(request,'index.html')
    
def login_otp(request):
    mobile= request.session['mobile']
    email=request.session['email']
    context={'mobile':mobile,'email':email}
    otpp=request.session['otpp']
    valid_date=request.session['valid_until']
    valid_until=datetime.fromisoformat(valid_date)
    
    if request.method == "POST":
        otp=request.POST.get('loginotp')
        if valid_until > datetime.now():
            if str(otp)==otpp:
                profile= Profile.objects.filter(mobile=mobile).first()
                user=User.objects.get(id=profile.user.id)
                del request.session['email']
                login(request,user)
                    
                request.session.clear_expired()
                return redirect("/") 
            else:
                context={'message':'WRONG OTP!!','class':'danger','mobile':mobile,'invisible':'invisible'}
                return render(request,'index.html',context) 
        else:
            context={'message':'Your Session has Expired!Login Again!','class':'danger','mobile':mobile,'email':email,'invisible':'invisible'}
            return render(request,'index.html',context)            
    return render(request,'index.html',context)
 
def verify(request):
    name=request.session['name']
    mobile= request.session['mobile']
    whatsapp=request.session['whatsapp']
    email=request.session['email']
    pincode=request.session['pincode']

    context={'mobile':mobile,'email':email}

    otpp=request.session['otpp']

    valid_date=request.session['valid_until']
    valid_until=datetime.fromisoformat(valid_date)

    if request.method == "POST":
        otp=request.POST.get('otp')
        if valid_until > datetime.now():
            if str(otp)==otpp:
                print(request.session.get_expiry_age())
                user=User(username=name,email=email)
                user.save()
                profile=Profile(user=user,mobile=mobile,whatsapp_status=whatsapp,email=email,pincode=pincode)
                profile.save()
                profile= Profile.objects.filter(mobile=mobile).first()
                user=User.objects.get(id=profile.user.id)
                login(request,user)
                return redirect("/")
            else:
                context={'message':'WRONG OTP!!','class':'danger','mobile':mobile,'email':email,'invisible':'invisible'}
                return render(request,'index.html',context)
        else:
            context={'message':'Your Session has Expired!Register Again!','class':'danger','mobile':mobile,'email':email,'invisible':'invisible'}
            return render(request,'index.html',context)       
    return render(request,'index.html',context)

def attempt_logout(request):
    logout(request)
    return redirect('/')

def thankyou(request):
    return render(request,'thanku.html')
