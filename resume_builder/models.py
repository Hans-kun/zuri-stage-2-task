from django.db import models

# Create your models here.

class Customer(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    email = models.EmailField()
    occupation = models.CharField(max_length=200)
    about = models.TextField(blank=False)

    def __str__(self):
        return self.name

class Skills(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.title


class Technical(models.Model):
    tech_stack = models.CharField(max_length=200)

    def __str__(self):
        return self.tech_stack


class Experience(models.Model):
    company_name = models.CharField(max_length=200)
    job_role = models.CharField(max_length=200)
    duration = models.IntegerField(null=True)
    job_description = models.TextField()

    def __str__(self):
        return self.company_name


class Education(models.Model):
    university_name = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    course = models.CharField(max_length=200)
    gpa = models.FloatField()

    def __str__(self):
        return self.university_name

