from django.db import models

class Comment(models.Model):
    first_name = models.CharField(max_length=40)
    Last_name = models.CharField(max_length=50)
    photo = models.ImageField(upload_to='photo/%Y/%m/%d/')
    comment = models.CharField(max_length=500)
    city = models.CharField(max_length=50)
    country = models.CharField(max_length=30)

    def __str__(self):
        return self.first_name + ' ' + self.Last_name
