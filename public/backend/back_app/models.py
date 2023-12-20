from django.db import models

# Create your models here.

class login(models.Model):
    email=models.CharField(max_length=50)
    password=models.CharField(max_length=50)
    role=models.CharField(max_length=50)


class UserRegister(models.Model):
    name=models.CharField(max_length=50)
    contact=models.CharField(max_length=50)
    log_id=models.ForeignKey(login,on_delete=models.CASCADE)
    address=models.CharField(max_length=50)

class Products(models.Model):
    name=models.CharField(max_length=50)
    Trousers='Trousers'
    jeans='jeans'
    shirt='shirt'
    t_shirt='t-shirt'
    Shorts='Shorts'
    innerware='innerware'
    Shoes='Shoes'
    Accessories='Accessories'
    jackets_coats='Jackets & Coats'
    Hoodies_Sweatshirts='Hoodies & Sweatshirts'
    Skirts='Skirts'
    tops='tops'

    
    STATUS_CHOICES = [
    (Trousers,'Trousers'),
    (jeans,'jeans'),
    (shirt,'shirt'),
    (t_shirt,'t-shirt'),
    (Shorts,'Shorts'),
    (innerware,'innerware'),
    (Shoes,'Shoes'),
    (Accessories,'Accessories'),
    (jackets_coats,'Jackets & Coats'),
    (Hoodies_Sweatshirts,'Hoodies & Sweatshirts'),
    (Skirts,'Skirts'),
    (tops,'tops'),
       
    ]
    
    category = models.CharField(
        max_length=2000,
        choices=STATUS_CHOICES,
     
    )


    MEN='men'
    WOMEN='women'
    KIDS='kids'
    HOME='home'

    
    STATUS_CHOICES = [
        (MEN, 'men'),
        (WOMEN, 'women'),
        (KIDS, 'kids'),
        (HOME, 'home'),
    ]
    
    gender = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
     
    )

    # gender=models.CharField(max_length=50)
    actualprice=models.CharField(max_length=50)
    discountprice=models.CharField(max_length=50)
    description=models.CharField(max_length=50)
    Imagesone = models.ImageField(upload_to='images/',null=True,blank=True)
    Imagestwo = models.ImageField(upload_to='images/',null=True,blank=True)
    Imagesthree = models.ImageField(upload_to='images/',null=True,blank=True)
    Imagesonefour = models.ImageField(upload_to='images/',null=True,blank=True)
    def __str__(self):
        return self.name
    

class productsize(models.Model):
    size=models.CharField(max_length=200)
    count=models.PositiveIntegerField(default=0,null=True)
    pro_name=models.ForeignKey(Products,on_delete=models.CASCADE)
    def __str__(self):
       return self.size


# class ProductSizeCount(models.Model):
#     product = models.ForeignKey(Products, on_delete=models.CASCADE)
#     size = models.ForeignKey(productsize, on_delete=models.CASCADE)
#     count = models.PositiveIntegerField(default=0)

class cart(models.Model):
    product_name=models.CharField(max_length=250)
    size=models.CharField(max_length=50,null=True,blank=True)
    log_id=models.CharField(max_length=50)
    def __str__(self):
        return self.product_name
    
class favourite(models.Model):
    product_name=models.CharField(max_length=250)
    log_id=models.CharField(max_length=50)
    def __str__(self):
        return self.product_name
    
