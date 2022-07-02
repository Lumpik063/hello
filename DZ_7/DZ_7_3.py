import os
import shutil

my_project_path = os.path.abspath(os.curdir)

my_project_main = os.listdir('my_project')


for file in my_project_main:
    pyt = (my_project_path + '\\' + 'my_project' + '\\' + file + '\\' + 'templates')
    print(pyt)
    try:
        shutil.copytree(pyt, 'my_project/templates', dirs_exist_ok=True)
    except FileNotFoundError:
        pass
