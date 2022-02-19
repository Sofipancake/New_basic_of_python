"""Задание 1
Написать скрипт, создающий стартер (заготовку) для проекта со следующей
структурой папок:

|--my_project
   |--settings
   |--mainapp
   |--adminapp
   |--authapp
Примечание: подумайте о ситуации, когда некоторые папки уже есть на диске
(как быть?); как лучше хранить конфигурацию этого стартера, чтобы в будущем
можно было менять имена папок под конкретный проект; можно ли будет при этом
расширять конфигурацию и хранить данные о вложенных папках и файлах
(добавлять детали)?"""

import os


list = ['my_project', 'my_project/settings', 'my_project/mainapp', 'my_project/adminapp', 'my_project/authapp']
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
for dir in list:
    dir_path = os.path.join(BASE_DIR, dir)
    if not os.path.exists(dir_path):
       os.makedirs(dir_path)

# Конфигурацию лучше хранить в отдельном файле и читать из файла