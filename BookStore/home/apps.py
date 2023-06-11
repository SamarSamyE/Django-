from django.apps import AppConfig


class HomeConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'home'

    def ready(self):     # used for register signals because it is invoked when app init
        from .signals import create_and_assign_isbn_to