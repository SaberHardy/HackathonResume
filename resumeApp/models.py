from django.db import models


class WhoAmI(models.Model):
    about_me = models.TextField()

    def __str__(self):
        return self.about_me[:10]


class OnlineCourses(models.Model):
    title = models.CharField(max_length=300)
    get_from = models.CharField(max_length=100)
    when = models.DateField()
    where = models.CharField(max_length=50)

    def __str__(self):
        return self.title
