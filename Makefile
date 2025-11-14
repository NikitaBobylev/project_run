dev: 
	python manage.py runserver --settings=project_run.settings.local


prod: 
	python manage.py runserver --settings=project_run.settings.production

migrate: 
	python manage.py migrate

superuser:
	python manage.py createsuperuser

freeze:
	pip freeze > requirements.txt

