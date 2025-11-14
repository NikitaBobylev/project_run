dev: 
	python manage.py runserver --settings=core.settings.local


prod: 
	python manage.py runserver --settings=core.settings.production

migrate: 
	python manage.py migrate

superuser:
	python manage.py createsuperuser

freeze:
	pip freeze > requirements.txt

