from django.urls import path
from . import views

urlpatterns = [
    path('', views.alltodo, name = 'alltodo'),
    path('delete/<int:pk>', views.deleteItem, name = 'deleteItem'),
    path('update/<int:pk>', views.updateItem, name = 'updateItem')
]