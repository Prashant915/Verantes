from django.contrib import admin
from .models import *
from django.utils.html import mark_safe

class Products(admin.ModelAdmin):
    class Media:
         pass
    list_display=('id','Product_Image','Title','product','catogory','Add_On_Home_Page','Add_On_Gallery')
    
    def Product_Image(self,obj):
            return mark_safe(f'<img src="/media/{obj.Image}" width="150" height="120"/>')

class Page_Banner(admin.ModelAdmin):
      list_display=('Page_Name','banner_image')

      def banner_image(self,obj):
            return mark_safe(f'<img src="/media/{obj.Image}" width="280" height="120"/>')
     # def has_delete_permission(self, request, obj=None):
     #    return False
class Testament(admin.ModelAdmin):
      list_display=('Happy_Customer','Name','Review')

      def Happy_Customer(self,obj):
            return mark_safe(f'<img src="/media/{obj.Image}" width="150" height="120"/>')
      
admin.site.register(Product)
# admin.site.register(Catagory) 
admin.site.register(All_Product,Products)
admin.site.register(Banner,Page_Banner)
admin.site.register(Testimonials,Testament)
