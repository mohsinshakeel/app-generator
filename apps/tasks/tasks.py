import os
import subprocess
from celery import shared_task
from django.conf import settings
from datetime import datetime


def log_to_file(task_name, task_path, log_message):
    log_filename = os.path.join(task_path, 'logs', f'{task_name}.log')
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    with open(log_filename, 'a') as log_file:
        log_file.write(f'[{timestamp}] {log_message}\n')

@shared_task
def run_hourly_task():
    task_path = getattr(settings, 'CELERY_SCRIPTS_DIR')
    hourly_task = os.path.join(task_path, 'hourly', 'hourly_tasks.py')
    result = subprocess.run(['python', hourly_task], capture_output=True, text=True)
    log_to_file('hourly_task', task_path, f'{result.stdout}')

@shared_task
def run_daily_task():
    task_path = getattr(settings, 'CELERY_SCRIPTS_DIR')
    daily_task = os.path.join(task_path, 'daily', 'daily_tasks.py')
    result = subprocess.run(['python', daily_task], capture_output=True, text=True)
    log_to_file('daily_task', task_path, f'{result.stdout}')

@shared_task
def run_weekly_task():
    task_path = getattr(settings, 'CELERY_SCRIPTS_DIR')
    weekly_task = os.path.join(task_path, 'weekly', 'weekly_tasks.py')
    result = subprocess.run(['python', weekly_task], capture_output=True, text=True)
    log_to_file('weekly_task', task_path, f'{result.stdout}')

@shared_task
def run_monthly_task():
    task_path = getattr(settings, 'CELERY_SCRIPTS_DIR')
    monthly_task = os.path.join(task_path, 'monthly', 'monthly_tasks.py')
    result = subprocess.run(['python', monthly_task], capture_output=True, text=True)
    log_to_file('monthly_task', task_path, f'{result.stdout}')