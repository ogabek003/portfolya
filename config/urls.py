from django.contrib import admin
from django.urls import path

from store import views


urlpatterns = [

    path(
        "admin/",
        admin.site.urls
    ),

    path(
        "",
        views.home,
        name="home"
    ),

    path(
        "biz-haqimizda/",
        views.biz_haqimizda,
        name="bhaqimizda"
    ),

    path(
        "aloqa/",
        views.aloqa,
        name="aloqa"
    ),

    path(
        "register/",
        views.register,
        name="register"
    ),

    path(
        "register/success/",
        views.register_success,
        name="register_success"
    ),

    path(
        "zakaz/",
        views.zakaz,
        name="zakaz"
    ),

    path(
        "zakaz-form/",
        views.zakaz_form,
        name="zakaz_form"
    ),

    path(
        "buyurtmalarim/",
        views.buyurtmalarim,
        name="buyurtmalarim"
    ),

    # =========================
    # PORTFOLIO
    # =========================

    path(
        "loyihalar/",
        views.loyihalar,
        name="loyihalar"
    ),

    # =========================
    # BOG'LANISH
    # =========================

    path(
        "boglanish/",
        views.boglanish,
        name="boglanish"
    ),

    path(
        "boglanish/success/",
        views.boglanish_success,
        name="boglanish_success"
    ),

]