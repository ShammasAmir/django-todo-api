from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_todos),
    path('cbv/', views.TodosListApiView.as_view()),
]