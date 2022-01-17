from django.db import models
from django.utils.text import slugify

class Indoker(models.Model):
    id = models.AutoField(primary_key=True)
    fornavn = models.CharField(max_length=32, blank=False)
    etternavn = models.CharField(max_length=32, blank=False)
    slug = models.SlugField(blank=False)
    profile_pic = models.ImageField(default='default.png')
    facebooklink = models.CharField(max_length=130, blank=False)

    def __str__(self):
        return self.slug
    
    def fullname(self):
        return f"{self.fornavn} {self.etternavn}"

    def save(self, *args, **kwargs):
        self.slug = '-'.join((slugify(self.fornavn), slugify(self.etternavn)))
        super(Indoker, self).save(*args, **kwargs)