from django.db import models
from django.contrib.auth.models import User
# Create your models here.
statename=(('AP','Andhra Pradesh'),('AR','Arunachal Pradesh'),('AS','Assam'),('BH','Bihar'),('CH','Chhattisgarh'),
('GO','Goa'),('GU','Gujrat'),('HA','Haryana'),('HI','Himachal Pradesh'),('JK','Jharkhand'),('KA','Karnataka'),
('KE','Kerala'),('MP','Madhya Pradesh'),('MA','Maharashtra'),
('MA','Manipur'),('ME','Meghalaya'),('MI','Mizoram'),('NA','Nagaland'),
('OD','Odisha'),('PU','Punjab'),('RA','Rajasthan'),('SI','Sikkim'),('TN','Tamil Nadu'),
('TE','Telangana'),('TR','Tripura'),('UP','Uttar Pradesh'),('UK','Uttarakhand'),
('WB','West Bengal'),('AN','Andaman and Nicobar Island'),('CH','Chandigarh'),
('DN','Dadra and Nagar Haveli and Daman and Diu'),('DL','Delhi'),
('LA','Ladakh'),('LK','Lakshadweep'),('JA','Jammu and Kashmir'),('PU','Puducherry'))

category_choices= (('AC','Academy'),('COMP','Competition'))
class Customer(models.Model):
   user= models.ForeignKey(User,on_delete=models.CASCADE)
   name=models.CharField(max_length=200)
   city=models.CharField(max_length=50)
   zipcode=models.IntegerField()
   state=models.CharField(choices=statename,max_length=50)
   def __str(self):
       return self.name


class Product(models.Model):
    title=models.CharField(max_length=100)
    category=models.CharField(choices=category_choices,max_length=50)
    selling_price=models.FloatField()
    discounted_price=models.FloatField()
    description=models.TextField()
    product_image=models.ImageField(upload_to='product_image')
    def __str(self):
       return self.title

class Cart(models.Model):
    user= models.ForeignKey(User,on_delete=models.CASCADE)
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity=models.PositiveIntegerField(default=1)
    def __str(self):
       return self.id

class OrderPlaced(models.Model):
    user= models.ForeignKey(User,on_delete=models.CASCADE)
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity=models.PositiveIntegerField(default=1)
    customer=models.ForeignKey(Customer,on_delete=models.CASCADE)
    order_date=models.DateTimeField(auto_now_add=True)
    def __str(self):
       return self.id