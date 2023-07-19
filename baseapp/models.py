from django.db import models
from django.contrib.auth.models import User


class WordHistory(models.Model):
    word = models.CharField(max_length=128, null=False, blank=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE
                             )
    def __str__(self):
        return self.word
    
class FileModel(models.Model):
    filedata = models.FileField(upload_to='uploads/')                        
    line = models.IntegerField()
    word = models.CharField(max_length=128, null=False, blank=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.word} in {self.line} by {self.user}'
    
    