from django.urls import path
from . import views
# ! ROUTE

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('cars/', views.cars_index, name='index'),
    path('cars/<int:car_id>/', views.cars_detail, name='detail'),
    # new route used to show a form and create a cat
    path('cars/create/', views.CarCreate.as_view(), name='cars_create'),
    # Add the new routes below
    path('cars/<int:pk>/update/', views.CarUpdate.as_view(), name='cars_update'),
    path('cars/<int:pk>/delete/', views.CarDelete.as_view(), name='cars_delete'),

]
