"""Создать структуру файлов и папок, как написано в задании 2 (при помощи скрипта или «руками» в проводнике).
Написать скрипт, который собирает все шаблоны в одну папку templates, например:

|--my_project
   ...
   |--templates
   |   |--mainapp
   |   |  |--base.html
   |   |  |--index.html
   |   |--authapp
   |      |--base.html
   |      |--index.html
Примечание: исходные файлы необходимо оставить; обратите внимание, что html-файлы расположены в родительских
папках (они играют роль пространств имён); предусмотреть возможные исключительные ситуации; это реальная задача,
которая решена, например, во фреймворке django."""


import os
import shutil

base_dir = 'my_project'


list = []
path_f = []


for d, dirs, files in os.walk(base_dir):
    for dir in dirs:
        path = os.path.join(d, dir)
        print(path)
        last_dir = path.split("\\")
        if last_dir[-1] == 'templates':
            path_f.append(path)
print(path_f)

dir_path = os.path.join(base_dir, 'templates')
if not os.path.exists(dir_path):
    os.mkdir(dir_path)

for source in path_f:
    shutil.copytree(source, dir_path, dirs_exist_ok=True)


















