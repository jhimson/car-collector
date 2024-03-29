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
    path('cars/<int:car_id>/add_racing/', views.add_racing, name='add_racing'),
    path('accessories/', views.AccessoryList.as_view(), name='accessories_index'),
    path('accessories/<int:pk>/', views.AccessoryDetail.as_view(),
         name='accessory_detail'),
    path('accessories/create/', views.AccessoryCreate.as_view(),
         name='accessories_create'),
    path('accessories/<int:pk>/update/',
         views.AccessoryUpdate.as_view(), name='accessories_update'),
    path('accessories/<int:pk>/delete/',
         views.AccessoryDelete.as_view(), name='accessories_delete'),

    path('cars/<int:car_id>/assoc_accessory/<int:accessory_id>/',
         views.assoc_accessory, name='assoc_accessory'),

]
