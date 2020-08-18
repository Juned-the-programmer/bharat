from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name="index"),
    path('product/',views.product_,name="product"),
    path('product_page/<pk>',views.product_page,name="product_page"),
]

