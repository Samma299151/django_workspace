from django.db import models

# Create your models here.
class Customer(models.Model):
    customer_code = models.CharField(
        max_length=6,
        primary_key=True)
    customer_name = models.CharField(max_length=20)
    customer_telno = models.CharField(max_length=13)
    customer_postalcode = models.CharField(max_length=8)
    customer_address = models.CharField(max_length=40)
    class Meta:
        db_table = 'customer'