from django.urls import path
from . import views

app_name = "main"

urlpatterns = [
    path("", views.home_view, name="home_view"),
    path('riyadh/', views.riyadh_view, name='riyadh_view'),
    path('qassim/', views.qassim_view, name='qassim_view'),
    path('shamaliyah/', views.ash_shamaliyah_view, name="ash_shamaliyah_view"),
    path('sharqiyah/', views.ash_sharqiyah_view, name="ash_sharqiyah_view"),
    path('asir/', views.asir_view, name="asir_view"),
    path('bahah/', views.bahah_view, name="bahah_view"),
    path('hail/', views.hail_view, name="hail_view"),
    path('jizan/', views.jizan_view, name="jizan_view"),
    path('najran/', views.najran_view, name="najran_view"),
    path('madinah/', views.madinah_view, name="madinah_view"),
    path('makkah/', views.makkah_view, name="makkah_view"),
    path('tabuk/', views.tabuk_view, name="tabuk_view"),
    path('jouf/', views.jouf_view, name="jouf_view"),
    path("about/us/", views.about_view, name="about_view"),
    path('set-language/<str:lang>/', views.set_language, name='set_language'),
    path('set-theme/<str:mode>/', views.set_theme, name='set_theme'),
]