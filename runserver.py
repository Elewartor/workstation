import os

project_path = 'C:\\Users\\IntentRefurbish\\Desktop\\workstation\\workstation\\intentws2'
virtualenv = 'itentws2'
ip = '192.168.1.89:8000'

os.chdir(project_path)
os.system('workon '+ virtualenv +' && python manage.py runserver ' + ip)