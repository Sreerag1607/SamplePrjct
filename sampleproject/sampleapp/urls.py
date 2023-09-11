from . import views
from django.urls import path



urlpatterns = [
    path('',views.demo,name='demo'),
    # path('about/',views.add,name="add"),
    # path('contact/',views.contact,name="contact")
]
