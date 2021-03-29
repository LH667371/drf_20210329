from django.db import models


# Create your models here.
class User(models.Model):
    gender_choices = (
        (0, "男"),
        (1, "女"),
        (2, "其他"),
    )
    username = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=255)
    gender = models.SmallIntegerField(choices=gender_choices, default=0)

    class Meta:
        db_table = 'user_info'
