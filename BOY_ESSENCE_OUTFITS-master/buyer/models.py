from django.db import models
from django.conf import settings
from django.contrib.auth.models import User



from authentication.models import MyCustomerModel
from seller.models import MyProductsModel
from master.models import baseModel

# Create your models here.
class MyCartModel(baseModel):
    customer_id = models.ForeignKey(MyCustomerModel, on_delete=models.CASCADE)
    product_id = models.ForeignKey(MyProductsModel, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)



class OrderModel(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    razorpay_order_id = models.CharField(max_length=100)
    razorpay_payment_id = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20, default='Pending')  
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.razorpay_order_id
    

class OrderItemModel(models.Model):
    order = models.ForeignKey(OrderModel, related_name='items', on_delete=models.CASCADE)
    product_id = models.ForeignKey(MyProductsModel, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    image_url = models.URLField(max_length=200)

    def __str__(self):
        return f'{self.product_id.title} ({self.quantity})'    
    
class ContactUSModel(baseModel):

    STATUS_CHOICES = (
        ('resolved', 'Resolved'),
        ('unresolved', 'Unresolved'),
        ('on_working', 'On Working')
    )


    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    message = models.TextField()
    status = models.CharField(choices=STATUS_CHOICES, default='unresolved', max_length=255)


