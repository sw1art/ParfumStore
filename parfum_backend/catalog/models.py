from django.db import models


class Category(models.Model):
    pass 
class Brand(models.Model):
    pass
class Volume(models.Model):
    volume = models.IntegerField(unique=True)
    
class Product(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=7, decimal_places=0)
    volume = models.ForeignKey(to=Volume)
    image = models.ImageField(upload_to='', default='')
    descriptions = models.CharField(max_length=1000)
    slug = models.SlugField(null=False, unique=True)
    brand = models.ForeignKey(to=Brand, on_delete=models.CASCADE, related_name='')

    def get_absolute_url(self):
        return reverse('sneaker_detail', kwargs={'slug': self.slug, 'uuid': self.volume})
    
    def __str__(self):
        return self.name   