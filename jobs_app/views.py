import json
import os
from django.shortcuts import render
from django.conf import settings

def show_jobs(request):
    file_path = os.path.join(settings.BASE_DIR, 'jobs.json')
    jobs_data = []
    if os.path.exists(file_path):
        with open(file_path, 'r', encoding='utf-8') as f:
            jobs_data = json.load(f)
            
    return render(request, 'jobs_app/index.html', {'jobs': jobs_data})