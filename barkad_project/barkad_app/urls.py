from django.urls import path
from . import views

urlpatterns = [
   path('', views.index, name="index"),
   path('about_us', views.about_us, name="about_us"),
   path('authorization', views.authorization, name="authorization"),
   path('registration', views.registration, name="registration"),
   path('feedback', views.feedback, name="feedback"),
   path('allproducts', views.products, name="allproducts"),
   path('product', views.concrete_product, name="product"),
]