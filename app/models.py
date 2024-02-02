from django.db import models

# Create your models here.


class Document(models.Model):
    name = models.CharField(max_length=50, verbose_name="Document Name")
    document = models.FileField(verbose_name="Documents", upload_to="media/documents/")

    def __str__(self):
        return str(self.id)
