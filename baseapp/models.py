from django.db import models
from django.contrib.auth.models import User
from django.core.validators import FileExtensionValidator
from django.core.exceptions import ValidationError

def validar_tamano_pdf(value):
    # Tamaño máximo permitido en bytes (por ejemplo, 5 MB)
    max_size = 5 * 1024 * 1024

    if value.size > max_size:
        raise ValidationError("El tamaño del archivo no puede exceder 5 MB.")


class WordHistory(models.Model):
    word = models.CharField(max_length=128, null=False, blank=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE
                             )
    def __str__(self):
        return self.word
    
    def to_dict(self):
        return {
            'word': self.word,
            'user': self.user.username,
            # Agrega otros campos que necesites para la plantilla
        }
    
class FileModel(models.Model):
    filedata = models.FileField(upload_to='uploads/',
                                validators=[
            FileExtensionValidator(allowed_extensions=['pdf']),
            validar_tamano_pdf
        ])                        
    line = models.IntegerField()
    word = models.CharField(max_length=128, null=False, blank=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.word} in {self.line} by {self.user}'
    
