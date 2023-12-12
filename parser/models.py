from django.db import models


class Ranobe(models.Model):
    title = models.CharField(max_length=500)
    url = models.URLField()

    def __str__(self):
        return self.title


class RanobeFile(models.Model):
    file = models.FileField(upload_to='files/')
    ranobe = models.ForeignKey(Ranobe, on_delete=models.CASCADE)

    def __str__(self):
        return self.file.name
