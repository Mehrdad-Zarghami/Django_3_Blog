from django.urls import path
from . import views

urlpatterns = [
    path("", views.post_list_view, name='posts_list_page'),
    path('<int:pk>/', views.post_detail_view, name='post_detail_page'),  # a custom integer url which its name is pk
    path('create/', views.post_create_view, name='post_create_page'),
]
