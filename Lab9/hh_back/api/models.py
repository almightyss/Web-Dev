from django.db import models

class Company(models.Model):

    name = models.CharField(max_length=255, default='Roga and Kopyta')
    description = models.TextField(default='haha')
    city = models.CharField(default='remote')
    address = models.TextField(default='remote')

    def __str__(self):
        return f"{self.name}: {self.city}"

class Vacancy(models.Model):

    name = models.CharField(max_length=255, default='sales')
    description = models.TextField(default='need sales')
    salary = models.FloatField(default=42500)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)

    def __str__(self):
            return f"{self.name} at {self.company.name} - {self.salary}"
