settings.py    app 设置'management.apps.ManagementConfig',

新建文件夹 app.py

from django.apps import AppConfig


class ManagementConfig(AppConfig):
    name = ' management'

