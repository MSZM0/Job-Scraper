from django.contrib import admin
from django.urls import path
from jobs_app.views import show_jobs

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', show_jobs, name='home'),
]