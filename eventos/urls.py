from django.urls import path

from . import views

urlpatterns = [
    path("", views.home, name='home'),
    path('<int:evento_id>/', views.detalhes, name='detalhes'),
    path('cadastro_evento/', views.cadastro_evento, name="cadastro_evento"),

]