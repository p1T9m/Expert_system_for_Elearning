from django.apps import AppConfig


class SecondExpertConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "second_expert"

    def ready(self):
        import users.signals
