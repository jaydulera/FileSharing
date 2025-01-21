from django.db import models

# Create your models here.
from django.contrib.auth.models import User
from django.db import models

class File(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='files')
    file = models.FileField(upload_to='uploads/')
    shared_with = models.ManyToManyField(User, related_name='shared_files', blank=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.file.name