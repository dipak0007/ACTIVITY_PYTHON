from django.db import models

# Create your models here.
from django.db import models
from django.forms import ValidationError

from master.models import baseModel
from master.utils.BOY_UNIQ.unique_filename import genrate_unique_filename
from master.utils.BOY_UNIQ.unique_table_id import generate_table_id
from master.utils.BOY_CALCULATE.calc import calculate_discount

# Create your models here.

class MyCategoriesModel(baseModel):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name

class MyProductsModel(baseModel):
    DIR_NAME = 'product_images/'
    SUFFIX_WORD = 'pi'
    PREFIX_TABLE_ID_WORD = 'LOP'
    product_id = models.CharField(primary_key=True, max_length=255, blank=True)
    image = models.ImageField(upload_to=genrate_unique_filename)
    title = models.CharField(max_length=255)
    content = models.TextField()
    category_id = models.ForeignKey(MyCategoriesModel, on_delete=models.CASCADE)
    mrp_price = models.DecimalField(max_digits=10, decimal_places=2)
    selling_price = models.DecimalField(max_digits=10, decimal_places=2)
    discount = models.DecimalField(max_digits=5, decimal_places=2, blank=True)

    def clean(self):
        if self.mrp_price < self.selling_price:
            raise ValidationError("Selling price cannot be greater than MRP price")

    def save(self, *args, **kwargs):
        if not self.product_id:
            self.full_clean()  # Validate before saving
            self.discount = calculate_discount(self.mrp_price, self.selling_price)
            self.product_id = generate_table_id(self)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.category_id.name} - {self.product_id}"