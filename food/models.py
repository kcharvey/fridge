from django.db import models
from django.utils.text import slugify


class BaseModel(models.Model):

    name = models.CharField(max_length=30)
    slug = models.SlugField(blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(unicode(self.name))
        super(BaseModel, self).save(*args, **kwargs)

    class Meta:
        abstract = True


class Food(BaseModel):

    quantity = models.IntegerField()
    unit = models.CharField(max_length=30)


class Recipe(BaseModel):

    ingredients = models.ManyToManyField(Food)

