# import path
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('add_student/', views.add_student, name='add_student'),
    path('update_student/<int:id>/', views.update_student, name='update_student'),
    path('delete_student/<int:id>/', views.delete_student, name='delete_student'),
    path('list_student/', views.list_student, name='list_student'),
    path('', views.camera_page),
    path('save-data/', views.save_data),

]
