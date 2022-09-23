from django.db import models


class WhoAmI(models.Model):
    about_me = models.TextField()

    def __str__(self):
        return self.about_me[:10]
