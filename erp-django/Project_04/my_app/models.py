from django.db import models

class Project(models.Model):
    # id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=150)
    # price = models.DecimalField(max_digits=10, decimal_places=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.name}'
