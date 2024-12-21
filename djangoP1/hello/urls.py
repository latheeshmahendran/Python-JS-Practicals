from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('laz', views.laz, name='laz'),
    path("<str:name>", views.greet, name="greet"),
    path("<str:name>/2", views.greet2, name="greet2"),
]
