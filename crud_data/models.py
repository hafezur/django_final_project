from django.db import models

class shop_data(models.Model):
    id=models.AutoField(primary_key=True)
    date=models.CharField(max_length=30)
    trade_code=models.CharField(max_length=30)
    high=models.CharField(max_length=30)
    low=models.CharField(max_length=30)
    open=models.CharField(max_length=30)
    close=models.CharField(max_length=30)
    volume=models.CharField(max_length=30)
