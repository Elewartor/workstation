import os

project_path = 'C:\\Users\\inten\\Desktop\\intentws2\\intentws2'
virtualenv = 'intentws2'
ip = '192.168.1.129:8000'

os.chdir(project_path)
os.system('workon '+ virtualenv +' && python manage.py runserver ' + ip)