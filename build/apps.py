from django.apps import AppConfig


class BuildConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'build'

    def ready(self):
        pass
        # from .import updateVotes
        # updateVotes.start()
