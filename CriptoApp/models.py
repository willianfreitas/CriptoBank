from django.db import models

class Client(models.Model):
    idclient = models.AutoField(primary_key=True)
    name = models.CharField(max_length=45, blank=True, null=True)
    email = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'client'


class Registers(models.Model):
    idregisters = models.AutoField(primary_key=True)
    idwallet = models.IntegerField()
    cripto = models.CharField(max_length=45, blank=True, null=True)
    value = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'registers'


class Wallet(models.Model):
    idwallet = models.AutoField(primary_key=True)
    idclient = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'wallet'
