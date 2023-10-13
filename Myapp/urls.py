from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.Signup),
    path('Dashboard/',views.Dashboard),
    path('edit/',views.Edit),
    path('Remove/', views.Remove),
    path('Login/', views.Login),
    path('Logout/', views.Logout),

]
