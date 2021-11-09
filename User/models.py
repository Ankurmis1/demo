from django.db import models

class User(models.Model):
    name=models.CharField(max_length=11)
    designation=models.CharField(max_length=15)
    address=models.CharField(max_length=11,null=True)

    def __str__(self):
        return self.name


