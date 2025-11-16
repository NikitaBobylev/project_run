from django.apps import AppConfig


class RunsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'project_run.apps.runs'

    def ready(self):
        import project_run.apps.runs.signals