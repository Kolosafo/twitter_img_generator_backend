from django.db import models

# Create your models here.


class VerifiedVotes(models.Model):
    verified = models.IntegerField(default=2435, blank=False)


class ContactUs(models.Model):
    name = models.CharField(max_length=100)
    message = models.CharField(max_length=500)

    def __str__(self):
        # user_to_string = str(self.user)
        return self.name
