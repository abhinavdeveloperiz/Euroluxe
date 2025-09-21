from django.db import models

class Home(models.Model):
    banner_video = models.FileField(upload_to="banner_video/")

    product1_image = models.ImageField(upload_to='product/')
    product1_video = models.FileField(upload_to='product/')
    product2_image = models.ImageField(upload_to='product/')
    product2_video = models.FileField(upload_to='product/')
    product3_image = models.ImageField(upload_to='product/')
    product3_video = models.FileField(upload_to='product/')

    def __str__(self):
        return "Home Page Content"


class Testimonial(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name


class Product_details(models.Model):


    # Product detail images (3 images per product)
    image1 = models.ImageField(upload_to='products/')
    image2 = models.ImageField(upload_to='products/', blank=True, null=True)
    image3 = models.ImageField(upload_to='products/', blank=True, null=True)

    def __str__(self):
        return self.name
