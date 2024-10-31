from django.db import models

class User(models.Model):

    first_name = models.CharField(max_length=150, blank=False)
    last_name = models.CharField(max_length=150, blank=False)
    phone_number = models.CharField(max_length=100, blank=False)
    mail = models.EmailField(blank=True,null=True)
    order_number = models.PositiveIntegerField(blank=False,null=False)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    class Meta:
        db_table = 'Users'

class Menu(models.Model):

    FOODS = (
        ('pizza', 'Pizza'),
        ('somsa', 'Somsa'),
        ('cheese', 'Cheese'),
    )
    food = models.CharField(max_length=150, choices=FOODS)

    DRINKS = (
        ('fruit juice', 'Fruit Juice'),
        ('drink1', 'Drink1'),
        ('drink2','Drink2')
    )
    drinks = models.CharField(max_length=250, choices=DRINKS)


    def __str__(self):
        return f'{self.food} and {self.drinks}'

    class Meta:
        db_table = 'Menu'


class OrderInfo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='User')
    orders = models.ForeignKey(Menu, on_delete=models.CASCADE, related_name='Menu')


    def __str__(self):
        return f'{self.user} bought {self.orders}'

    class Meta:
        db_table = 'OrderInfo'
