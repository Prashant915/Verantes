"""
URL configuration for Verantes_site project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include,re_path
from Showcase import views
from Customer_Requirement import views as customerview
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name='homepage'),
    path('design-gallery/',views.design_gallery,name='design-gallery'),
    path('vanity-units/',views.vanity,name="vanity-units"),

    path('wordrobe/',views.wordrobe,name="wordrobe"),
    path('moduler-kitchen/',views.moduler_kitchen,name="moduler-kitchen"),
    path('barkitchen/',views.barkitchen,name='barkitchen'),
    path('contact-us/',customerview.contact_form,name="contactform"),

    path('thankyou/',customerview.thankyou,name="thankyou"),
    path('signup/',customerview.signup,name="signup"),
    path('login/',customerview.login_attempt,name="login"),
    path('signup-otp/',customerview.verify,name="signupotp"),

    path('login-otp/',customerview.login_otp,name="loginotp"),
    path('logout/',customerview.attempt_logout,name="attempt_logout"),
    path('Estimate_flow_step1/',views.estimate_flow,name="estimate1"),
    path('Estimate_flow_step2/',views.estimate_flow2,name="estimate2"),

    path('get-your-estimate/',views.final_estimation,name="final-estimation"),

    re_path(r'^chaining/', include('smart_selects.urls')),
]

urlpatterns+= static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)


admin.site.site_header = "Verantes Admin Portal"
admin.site.site_title = "Verantes Admin Portal"
admin.site.index_title = "Welcome to Verantes Admin Portal"
