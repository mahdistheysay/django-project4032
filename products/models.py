import random
from django.db import models
import os
# چهارتا کار انجام میدهد با دی بی
#crud
#create/read or retrive/update/delete

#for giving the pic title cistumize style
def get_file_extension(file):
    base_name = os.path.basename(file)
    name, ext = os.path.splitext(base_name)
    return name, ext

def upload_image(instance, filename):
    rand_name = random.randint(1,9999999)
    name , ext = get_file_extension(filename)
    file_name = f"{instance.id}-{instance.title}-{rand_name}{ext}"
    return f'products/{file_name}'

class ProductQuerySet(models.query.QuerySet):
    def actived(self):
        return self.filter(actived=True)


class ProductManageObjects(models.Manager):
    def get_queryset(self):
        return ProductQuerySet(self.model, self._db)



    def get_product_by_id(self, productid):
        qs = self.get_queryset().filter(id=productid)
        if qs.count() == 1:
            return qs.first()
        return None

    def get_active_products(self):
        return self.get_queryset().filter(actived=True)

    def get_active_show_products(self):
        return self.get_queryset().filter(actived=True , show =True)






# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=15, decimal_places=2)
    image = models.ImageField(upload_to=upload_image , null=True , blank=True)#products folder in media root
    actived = models.BooleanField(default=False)
    show = models.BooleanField(default=False)

    objects = ProductManageObjects()

    def __str__(self):#dunder method
        return self.title


