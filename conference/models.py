from django.db import models

# Create your models here.
class Speaker(models.Model):
    first_name = models.CharField(
        max_length=20,
        blank=False,
        null=False,
    )
    last_name = models.CharField(
        max_length=20,
        blank=False,
        null=False,
    )
    bio = models.TextField(
        max_length=2000,
        blank=False,
        null=False,
    )
    email = models.EmailField(blank=False, null=False)

    twitter = models.CharField(
        null=True,
        default=None,
        max_length=32,
        blank=True,
    )

    instagram = models.CharField(
        null=True,
        default=None,
        max_length=32,
        blank=True,
    )
    facebook = models.CharField(
        null=True,
        default=None,
        max_length=32,
        blank=True,
    )

    def __str__(self) -> str:
        return f'{self.first_name} {self.last_name}'

class Presentation(models.Model):
    title = models.CharField(
        max_length=200,
        blank=False,
        null=False,
    )
    abstract = models.TextField(
        max_length=2000,
        blank=False,
        null=False,
    )
    speaker = models.ForeignKey(Speaker, on_delete=models.PROTECT)

    approved = models.BooleanField(
        default=False
    )

    def __str__(self) -> str:
        return self.title