from django.db import models
from django.template.defaultfilters import slugify

from cloudinary.models import CloudinaryField

class Project(models.Model):
    title = models.CharField(max_length=200, verbose_name="Titulo")
    descrption = models.TextField(verbose_name="Descripción")
    image = CloudinaryField('image', blank=True)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated =   models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")
    slug = models.SlugField(editable=False, max_length=300)

    class Meta:
        verbose_name = "proyecto"
        verbose_name_plural = "proyectos"
        ordering = ["-created"]

    def __str__(self) -> str:
        return self.title
    
    def save(self, *args, **kwargs):
        slug_unique = '%s' % (self.title)
        self.slug = slugify(slug_unique)
        super(Project, self).save(*args, **kwargs)