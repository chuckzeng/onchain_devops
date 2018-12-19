from django.conf.urls import url
from navi import views

urlpatterns = [
    url(r'^$', views.index, name='navi'),
    url(r'^add/', views.add),
    url(r'^manage/', views.manage),
    url(r'^delete/', views.delete),
    url(r'^edit/', views.edit),
    url(r'^save/', views.save),
]