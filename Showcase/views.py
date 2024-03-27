from django.shortcuts import render
from .models import *

def home(request):
    slider=All_Product.objects.filter(Add_On_Home_Page=True)
    testimony=Testimonials.objects.all()
    context={
        'slider':slider,
        'testimony':testimony
    }
    return render(request,'index.html',context)

def design_gallery(request):
    testimony=Testimonials.objects.all()
    slider2=All_Product.objects.filter(Add_On_Gallery=True)
    latest=All_Product.objects.all().order_by('id').reverse()[:6]
    Catagories=Product.objects.all()
    context={
        'slider2':slider2,
        'latest':latest,
        'testimony':testimony,
        'catagories':Catagories,
        }
    return render(request,'design-gallery.html',context)

def vanity(request):
    vanity_slider=All_Product.objects.filter(product=3).order_by('id').reverse()
    banner=Banner.objects.get(Page_Name='Vanity Unit Design')
    return render(request,'vanity-units.html',{'slider':vanity_slider,'banner':banner})

def moduler_kitchen(request):
    slider1=All_Product.objects.filter(product=1).order_by('id').reverse()
    banner=Banner.objects.get(Page_Name='Moduler Kitchen')
    return render(request,'modular-kitchen.html',{'slider1':slider1,'banner':banner})

def wordrobe(request):
    Ward_slider=All_Product.objects.filter(product=2).order_by('id').reverse()
    banner=Banner.objects.get(Page_Name='Wordrobe Designs')
    return render(request,'wordrobe.html',{'slider':Ward_slider,'banner':banner})

def barkitchen(request):
    Bar_slider=All_Product.objects.filter(product=4).order_by('id').reverse()
    banner=Banner.objects.get(Page_Name='Bar kitchen Designs')
    return render(request,'barkitchen.html',{'slider':Bar_slider,'banner':banner})

def estimate_flow(request):
    return render(request,'Estimate1.html')

def estimate_flow2(request):
    return render(request,'Estimate2.html')

def final_estimation(request):
    testimony=Testimonials.objects.all()
    slider1=All_Product.objects.filter(product=1).order_by('id').reverse()
    banner=Banner.objects.get(Page_Name='Moduler Kitchen')
    return render(request,'estimate-page.html',{'slider1':slider1,'banner':banner,'testimony':testimony,})