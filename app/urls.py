from django.urls import path
from app import views

urlpatterns = [
    #path('', views.index, name='index'),
    #path('', views.demo3, name='index'),
    #path('<int:calendar_id>/', views.detail, name='detail'),
    #path('<int:calendar_id>/results/', views.results, name='results'),
    #path('<int:calendar_id>/vote/', views.vote, name='vote'),
    #path('', views.IndexView.as_view(), name='index'),
    path('', views.displayschedule, name='index'),
    #path('', views.index2, name='index')
]