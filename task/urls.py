from . import views
from django.urls import path
urlpatterns = [
    path('',views.view_task ,name="list"),
    path("Update_task/<str:pk>/",views.update_task , name="update_task"),
    path("delete_task/<str:pk>/",views.delete_task , name="delete_task"),
]

