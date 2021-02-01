from django.urls import path

from . import views

app_name = "news"
urlpatterns = [
    path('', views.index, name='index'),
    path('base_list.html', views.base_list, name='base_list'),
    path('navy.html', views.navy, name='navy'),
    path('army.html', views.army, name='army'),
    path('airforce.html', views.airforce, name='airforce'),
    path('animals.html', views.animals, name='animals'),
    path('one.html', views.one, name='one'),
    path('two.html', views.two, name='two'),
    path('three.html', views.three, name='three'),
    path('four.html', views.four, name='four'),
    path('five.html', views.five, name='five'),
    path('six.html', views.six, name='six'),
    path('<int:article_id>/', views.detail, name='detail'),

]

