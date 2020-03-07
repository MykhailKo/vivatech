from django.urls import path
from . import views

urlpatterns = [
    path('', views.main_categories, name="main_category"),
    #path('<str:sub_cat_name>/', views.sub_category_list, name="sub_category_list"),
    #path('<str:sub_cat_name>/<str:item_model>/', views.item_detail, name="item_detail")
]