from django.db import models
from tinymce.models import HTMLField
from smart_selects.db_fields import ChainedForeignKey
from django.utils.html import format_html

DESIGN_CHOICES = (
    ('Moduler Kitchen Designs','Moduler Kitchen Designs'),
    ('Wordrobe Designs', 'Wordrobe Designs'),
    ('Vanity Unit Design','Vanity Unit Design'),
    ('Bar kitchen Designs','Bar kitchen Designs'),
)
PAGE_BANNER = (
    ('Home','Home'),
    ('Design Gallery','Design Gallery'),
    ('Moduler Kitchen','Moduler Kitchen'),
    ('Wordrobe Designs', 'Wordrobe Designs'),
    ('Vanity Unit Design','Vanity Unit Design'),
    ('Bar kitchen Designs','Bar kitchen Designs'),
)
SUB_CATAGORY=(
    ('Verantes Kitchen Range','Verantes Kitchen Range'),
    ('Shutter Finishes','Shutter Finishes'),
    ('Handles','Handles'),
    ('Countertops and Backsplashes','Countertops and Backsplashes'),
    ('Cabinate and Hardware','Cabinate and Hardware'),
    ('Appliances','Appliances'),
    ('Sink and Faucets','Sink and Faucets'),
    ('Verantes wordrobe range','Verantes wordrobe range'),
    ('Wordrobe for Everyone','Wordrobe for Everyone'),
    ('Types of Wardrobes','Types of Wardrobes'),
    ('Wardrobe Shutter Types','Wardrobe Shutter Types'),
    ('The Cabinets','The Cabinets'),
    ('Add-ons','Add-ons'),
    ('Accessories','Accessories'),
    ('The Vanity Units Range','The Vanity Units Range'),
    ('Open Storage','Open Storage'),
    ('shedule meeting','shedule meeting')
)
class Product(models.Model):
    name = models.CharField(max_length=255,choices=DESIGN_CHOICES)
    Image=models.ImageField(upload_to="Catagories", blank=False, null=False,default=None)
    Link=models.URLField(max_length=200,blank=False,null=False, default=None)
    def __str__(self):
        return str(self.name)
    # def has_module_permission(self, request):
    #     return False

class Catagory(models.Model):
    product = models.ForeignKey( Product, on_delete=models.CASCADE)
    name = models.CharField(max_length=255,choices=SUB_CATAGORY)

    def __str__(self):
        return str(self.name)

    
class All_Product(models.Model):
    Image=models.ImageField(upload_to="Products", blank=False, null=False)
    Title=models.CharField(max_length=60)
    Description=HTMLField(max_length=200)
    product = models.ForeignKey(Product , on_delete=models.CASCADE,default=None)
    catogory = ChainedForeignKey(
        Catagory,
        chained_field="product",
        chained_model_field="product",
        show_all = False , 
        auto_choose=True ,
        null=True,
        blank=True,
        default=None)
    Add_On_Home_Page=models.BooleanField(default=False)
    Add_On_Gallery=models.BooleanField(default=False)
   
class Banner(models.Model):
    Page_Name=models.CharField(max_length=255,choices=PAGE_BANNER,unique=True)
    Image=models.ImageField(upload_to="Banner", blank=False, null=False)
    Title=models.CharField(max_length=60)
    def __str__(self):
        return str(self.Page_Name)

class Testimonials(models.Model):
    Image=models.ImageField(upload_to="Testimonials", blank=False, null=False)
    Name=models.CharField(max_length=40)
    Subtitle=models.CharField(max_length=60)
    Review=HTMLField(max_length=300)

class DemoModel(models.Model):
    @property
    def semantic_autocomplete(self):
        html = self.get_img()
        return format_html(html)