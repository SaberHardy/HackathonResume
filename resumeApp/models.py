from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title


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


class ProfessionalExperience(models.Model):
    # options = (
    #     ("Online", "Online"),
    #     ("University", "University"),
    #     ("Freelancer", "Freelancer"),
    # )

    title = models.CharField(max_length=200)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    when = models.DateField()
    where = models.CharField(max_length=50)
    description = models.TextField()

    def __str__(self):
        return self.title


class SkillsFramework(models.Model):
    name = models.CharField(max_length=100)
    percent = models.IntegerField(default=10)

    def __str__(self):
        return self.name
