from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class ExtendedUser(AbstractUser):

    FORESTRY = "FR"
    ANONYMOUS = "AN"
    NURSERY = "NR"

    USER_CHOICES = (
        (ANONYMOUS, 'anonymous'),
        (FORESTRY, 'forestry'),
        (NURSERY, 'nursery')
    )

    phone = models.IntegerField(null=True)
    user_type = models.CharField(max_length=10, default=1, choices=USER_CHOICES)

    def __str__(self):

        return self.username
