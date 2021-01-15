from django.db import models
from stdimage.models import StdImageField
from django.db.models import signals
from django.template.defaultfilters import slugify


class Base(models.Model):
    created_at = models.DateField("created at", auto_now_add=True)
    modified = models.DateField("Data update", auto_now_add=True)
    active = models.BooleanField("active", default=True)

    class Meta:
        abstract= True


class Product(Base):
    name = models.CharField('Name', max_length=100)
    price = models.DecimalField('price', max_digits=8, decimal_places=2)
    stock = models.IntegerField('stock')
    img = StdImageField("Img", upload_to='products', variations={'thumb': (124,124)})
    slug = models.SlugField('Slug', max_length=100, blank=True, editable=False)

    def __str__(self):
        return self.name


def product_pre_save(signal, instance, sender, **kwargs):
    instance.slug = slugify(instance.name)


signals.pre_save.connect(product_pre_save, sender=Product)