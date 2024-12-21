from django.db import models

# Create your models here.
class Media(models.Model):
    MEDIA_TYPE_CHOICES =[
        ('image', 'Image'),
        ('video', 'Video'),
    ]

    title = models.CharField(max_length=50)
    description = models.CharField(max_length=100)
    file_content = models.BinaryField()
    media_type = models.CharField(max_length=10, choices=MEDIA_TYPE_CHOICES)
    is_tarioty_original = models.BooleanField()
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} ({self.media_type})" 

