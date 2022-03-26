from django.urls import path

from . import views

urlpatterns = [
  path('', views.sellers_list_create_view),
  path('<int:pk>/update/', views.sellers_update_view),
  path('<int:pk>/destroy/', views.sellers_destroy_view),
  path('<int:pk>/', views.sellers_detail_view),
]