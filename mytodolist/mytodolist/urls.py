from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('todos/', include('todos.urls')),  # Ensure this line is included
]