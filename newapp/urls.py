from django.contrib import admin
from django.urls import path, include
from . import views
from .views import get_user_by_id, get_user_by_name

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('',include(newapp.urls))
    path('', views.index, name='home'),
    path('add/', views.ADD, name='add'),
    path('edit/', views.edit, name='edit'),
    path('update/<str:id>',views.update,name='update'),
    path('delete/<str:id>',views.delete,name='delete'),
    path('get_user_by_id/', get_user_by_id, name='get_user_by_id'),
    # path('login', views.loginUser, name='loginUser'),
    path('get_user_by_name/', get_user_by_name, name='get_user_by_name'),

]
