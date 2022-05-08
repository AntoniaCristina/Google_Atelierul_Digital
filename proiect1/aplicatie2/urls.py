from aplicatie2 import views
from django.urls import path

app_name = 'companies'

urlpatterns = [
    path('', views.CompaniesView.as_view(), name='lista_companii'),
    path('adaugare/', views.CreateCompaniesView.as_view(), name='adauga'),
    path('<int:pk>/update/', views.UpdateCopaniesView.as_view(), name='update'),
    path('<int:pk>/stergere/', views.delete_company, name='sterge'),
    path('<int:pk>/activeaza/', views.activate_company, name='activeaza'),
]