from django.db import models

# Create your models here.
class insta_day(models.Model):
    lastday=models.IntegerField(default=0)
    def __str__(self):
        return str(self.lastday)
class insta_msg(models.Model):
    msg=models.TextField(default='')
    def __str__(self):
        return str(self.msg)
class replace_letters(models.Model):
    word=models.TextField(default='')
    options=models.TextField(default='')
    def __str__(self):
        return str(self.word)
class insta_output(models.Model):
    op=models.TextField(default='')
class instence_start_date(models.Model):
    date=models.DateTimeField()
class instabot_error(models.Model):
    error=models.TextField(default='')
