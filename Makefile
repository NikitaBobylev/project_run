run: 
	python manage.py runserver

migrate: 
	python manage.py migrate

superuser:
	python manage.py createsuperuser

freeze:
	pip freeze > requirements.txt

