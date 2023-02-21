from django.apps import AppConfig


class BuildConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'build'

    def ready(self):
        from .import updateVotes
        updateVotes.start()
