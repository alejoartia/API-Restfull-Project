from django.db import models

class Person(models.Model):
    id = models.AutoField(primary_key = True)
    first_name = models.CharField('First_name', max_length=100)
    last_name = models.CharField('Last_name',max_length=200)

    def __str__ (self):
        return '{0},{1}'.format(self.last_name,self.first_name)

