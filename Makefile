dev: 
	python manage.py runserver --settings=core.settings.local


prod: 
	python manage.py runserver --settings=core.settings.production

migrate: 
	python manage.py migrate --settings=core.settings.local

migrations: 
	python manage.py makemigrations --settings=core.settings.local

superuser:
	python manage.py createsuperuser --settings=core.settings.local

freeze:
	pip freeze > requirements.txt

