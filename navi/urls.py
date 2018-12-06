from django.conf.urls import url
from navi import views

urlpatterns = [
    url(r'^$', views.index, name='navi'),
    url(r'^add/', views.add,),
]
