from django.urls import path
from . import views

urlpatterns = [
    path('test1/', views.HeloApiView.as_view()),
    path('test1/<int:pk>/', views.HeloDetailApiView.as_view()),
]