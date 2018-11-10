from django.urls import path
from .views import *

urlpatterns = [
    path('upload/',upload_file, name='upload_file'),
    path('save_data/',save_data,name="save_data"),

]
