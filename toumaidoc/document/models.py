from io import BytesIO
from PIL import Image

from django.core.files import File
from django.db import models

class Type(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField()

    class Meta:
        ordering =('name',)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f'/{self.slug}/'

class Document(models.Model):
    type = models.ForeignKey(Type, related_name='documents', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    slug = models.SlugField()
    description = models.TextField(blank=True, null=True)
    file = models.FileField(upload_to='uploads/', blank=True, null=True)
    thumbnail = models.FileField(upload_to='uploads/', blank=True, null=True)
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering =('-date_added',)

    def __str__(self):
        return self.name
    
    def get_absolute_name(self):
        return f'/{self.type.name}/{self.slug}/'
    
    def get_absolute_url(self):
        return f'/{self.type.slug}/{self.slug}/'

    def get_file(self):
        if self.file:
            return 'http://192.0.0.1:8000' + self.file.url
        return ''

    def get_thumbnail(self):
        if self.thumbnail:
            return 'http://192.0.0.1:8000' + self.thumbnail.url
        else:
            if self.file:
                self.thumbnail = self.make_thumbnail(self.file)
                self.save()
                return 'http://192.0.0.1:8000' + self.thumbnail.url
            else:
                return ''

    def make_thumbnail(self, file, size=(300,200)):
        fle = File.open(file)
        fle.thumbnail(size)
        thumb_io = BytesIO()
        fle.save(thumb_io, 'PDF', quality=85)

        thumbnail = File(thumb_io, name=file.name)

        return thumbnail