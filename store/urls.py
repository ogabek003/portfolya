from django.contrib import admin
from django.urls import path

from store.views import (
    home,
    biz_haqimizda,
    aloqa,
    register,
    register_success,
    zakaz,
    buyurtmalarim,
)

urlpatterns = [

    path("admin/", admin.site.urls),

    path("", home, name="home"),

    path(
        "biz-haqimizda/",
        biz_haqimizda,
        name="bizhaqimizda"
    ),

    path(
        "aloqa/",
        aloqa,
        name="aloqa"
    ),

    path(
        "register/",
        register,
        name="register"
    ),

    path(
        "register/success/",
        register_success,
        name="register_success"
    ),

    path(
        "zakaz/",
        zakaz,
        name="zakaz"
    ),

    path(
        "buyurtmalarim/",
        buyurtmalarim,
        name="buyurtmalarim"
    ),
    
]