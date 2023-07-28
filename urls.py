from django.contrib import admin
from django.urls import path
from .views import *


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home,name="list"),
    path('update_task/<str:pk>/', update_task, name="update_task"),
    path('delete/<str:pk>/', delete_task, name="delete"),
    # path('base',base,name="base")


]
