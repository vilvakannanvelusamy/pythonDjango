from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('form/', include('myformapp.urls')),
    path('admin/', admin.site.urls),
]


