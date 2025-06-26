from django.contrib import admin
from django.urls import path
from .views import home,signup,signin

urlpatterns = [
    path("", home),
    path('signup/', signup),
    path('signin/', signin),
    path('admin/', admin.site.urls),
]

