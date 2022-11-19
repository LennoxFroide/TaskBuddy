from django.contrib import admin
from django.urls import path, include
from todolist_app import views as todolistviews

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', todolistviews.index, name = 'index'),
    path('todolist/' , include('todolist_app.urls') ),  
    path('contact', todolistviews.contact, name = 'contact'),
    path('about', todolistviews.about, name = 'about'),
    path('account/' , include('users_app.urls') )
]
