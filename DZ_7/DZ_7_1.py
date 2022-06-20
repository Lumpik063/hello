import os
from pathlib import Path

my_project = os.path.abspath(os.curdir)
print(my_project)
folders = ['settings', 'mainapp', 'adminapp', 'authapp']

for i in folders:
    p = Path(f'{my_project}/my_project/{i}')
    p.mkdir(parents=True, exist_ok=True)

# Строка 10 как раз нам для того, чтобы избежать ошибок, связанных с отсутствием или наоборот наличием папок с таким названием.
# Хранить, думаю, лучше всего в JSON.