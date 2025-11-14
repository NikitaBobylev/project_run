dev: 
	python manage.py runserver --settings=project_run.settings.local


prod: 
	python manage.py runserver --settings=project_run.settings.production

migrate: 
	python manage.py migrate --settings=project_run.settings.local

migrations: 
	python manage.py makemigrations --settings=project_run.settings.local

superuser:
	python manage.py createsuperuser --settings=project_run.settings.local

freeze:
	pip freeze > requirements.txt

