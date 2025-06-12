from django.apps import AppConfig


class AUsersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.users'
    
    def ready(self):
        # Import and connect the signals
        import apps.users.signals
