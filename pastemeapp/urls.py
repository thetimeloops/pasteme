from django.urls import path
from pastemeapp import views

urlpatterns=[
    path('',views.index,name="index"),
    path('paster',views.paster,name="paster"),
    path('view/<str:name>',views.view,name="view")
]
