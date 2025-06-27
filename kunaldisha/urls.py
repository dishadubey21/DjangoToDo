from django.contrib import admin
from django.urls import path
from .views import home,signup,signin



urlpatterns = [  
    path('', signup),
    path('', home),
    path('', signin),
    path('admin/', admin.site.urls),
]

