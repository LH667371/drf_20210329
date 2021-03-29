from django.urls import path

from api import views

urlpatterns = [
    path('user/<str:id>/', views.userAPIView.as_view()),
    path('user/', views.userAPIView.as_view()),
]
