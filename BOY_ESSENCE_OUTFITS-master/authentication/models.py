from django.db import models

from master.models import baseModel

# Create your models here.
class MyCustomerModel(baseModel):
        customer_id = models.CharField(primary_key=True,max_length=255, blank=True)
        firstname = models.CharField(max_length=255, blank=True)
        lastname = models.CharField(max_length=255, blank=True)
        email = models.EmailField(max_length=255, blank=False, null=False)
        mobile = models.CharField(max_length=255, blank=True)
        password = models.CharField(max_length=255)
        is_activate = models.BooleanField(default=False)
        is_added_address = models.BooleanField(default=False)
        otp = models.CharField(max_length=10, default="111111")

        def __str__(self):
              return f"{self.customer_id} - {self.firstname} {self.lastname}"
        
        def save(self, *args, **kwargs):
               if not self.customer_id:
                     self.customer_id = self.generate_customer_id()
               return super(MyCustomerModel, self).save(*args, **kwargs)
        
        def generate_customer_id(self):
              Mylast_customer = MyCustomerModel.objects.order_by('-customer_id').first()
              if Mylast_customer:
                    last_id = int(Mylast_customer.customer_id[3:])
                    new_id = last_id + 1
              else:
                   new_id = 1
              return 'BEO{:04d}'.format(new_id)
        

class MyAddressModel(baseModel):
      customer_id = models.ForeignKey(MyCustomerModel, on_delete=models.CASCADE)
      curent_address = models.CharField(max_length=255)
      city = models.CharField(max_length=255)
      pincode = models.CharField(max_length=255)
      state = models.CharField(max_length=255)











