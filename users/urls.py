from django.urls import path

from . import views

urlpatterns = [
  path('', views.users_list_create_view),
  path('<int:pk>/update/', views.users_update_view),
  path('<int:pk>/destroy/', views.users_destroy_view),
  path('<int:pk>/', views.users_detail_view),
]