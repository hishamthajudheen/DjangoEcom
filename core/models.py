from django.db import models
import datetime

#Product Categories
class Category(models.Model):
    name = models.CharField(max_length=60)    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = 'Categories'

#Customers
class Customer(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    phone = models.CharField(max_length=10)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=100)
    def __str__(self):
        return f'{self.first_name} {self.last_name}'

#All Products
class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(default=0, decimal_places=2, max_digits=10)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
    description = models.CharField(max_length=600, default='', null=True)
    image = models.ImageField(upload_to='uploads/product/')
    
    #Sale Stuff
    on_sale = models.BooleanField(default=False)
    sale_price = models.DecimalField(default=0, decimal_places=2, max_digits=10)
            
    def __str__(self):
        return self.name
#Order Details    
class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    address = models.CharField(max_length=300, default='', blank=False)
    phone = models.CharField(max_length=15, default='', blank=False)
    date = models.DateField(default=datetime.datetime.today)
    status = models.BooleanField(default=False)
    def __str__(self):
        return self.product