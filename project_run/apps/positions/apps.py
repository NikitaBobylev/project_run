from django.apps import AppConfig


class PositionsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'project_run.apps.positions'

    
    def ready(self):
        import project_run.apps.positions.signals
