from django.db import models

class User(models.Model):

    GENDER = (
        ('male', 'Male'),
        ('female', 'Female')
    )

    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    age = models.PositiveIntegerField()
    gender = models.CharField(max_length=15,choices=GENDER)

    def __str__(self):
        return f"{self.last_name} {self.first_name}"


#     class Meta:
#         db_table = 'Users'

# class Book(models.Model):

#     title = models.CharField(max_length=150)
#     author = models.CharField(max_length=150)
#     genre = models.CharField(max_length=150)

#     def __str__(self):
#         return f"{self.title}"
    

#     class Meta:
#         db_table = 'Books'
