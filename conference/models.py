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

    def __str__(self) -> str:
        return self.title