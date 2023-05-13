from distutils.command.upload import upload
from django.db import models
from django.core.validators  import MinLengthValidator, MaxLengthValidator, MaxValueValidator, MinValueValidator


# Create your models here.
class Category(models.Model):
    id = models.AutoField(primary_key=True)

    name = models.CharField(
        max_length=100,
        unique=True,
        verbose_name= "Category Name",
        validators=[
            MinLengthValidator(2, "Category Name must to be grater than 2 charecters"),
        ],
    )

    slug = models.SlugField(
        max_length=50,
        unique=True,
        verbose_name= "Category Slugs",
        validators=[
            MinLengthValidator (2, "Category Name must to be grater than 2 charecters")
        ],
    )

    description = models.TextField(
        max_length=100,
        blank=True,
        null=True,
        verbose_name= 'Category Description',    
    )

    created_on = models.DateField(
        auto_now_add= True,
        verbose_name= 'Category Created On'    
    )

    upadated_on = models.DateField(
        auto_now=True,
        verbose_name= 'Updated On'    
    )

    def __str__(self):
        return self.name




class  Contact(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=50,unique=True)
    email = models.EmailField(unique=True)
    message = models.TextField()


class Brand(models.Model):
    id = models.AutoField(primary_key= True)

    name = models.CharField(
        max_length=50, 
        unique= True,
        verbose_name= 'name',
        validators= [
                MinLengthValidator(2, "brand name must to be grater than 2 charectors ")
          ],
    )

    slug = models.SlugField(
        max_length=50,
        unique= True,
        verbose_name= 'slug',
        validators=[
                MinLengthValidator(2, "brand slug must graterthan 2 charestors")
        ],
    )

    description = models.CharField(
        max_length= 250,
        null= True,
        blank= True,
        verbose_name= 'description'
    )

    website = models.URLField(
        max_length= 70,
        blank=True,
        null= True,
        verbose_name='website'
    )

    created_on = models.DateTimeField(
        auto_now_add=True,
        verbose_name= 'created on'
        
    ) 

    def __str__(self):
        return self.name


class Products(models.Model):

    status = (
        ('Active', 'Active'),
        ('Inactive', 'Inactive'),
        ('Out of stock', 'Out of stock')
    )

    id = models.BigAutoField(primary_key= True)
    name = models.CharField(
        max_length = 70,
        unique=True,
        verbose_name = 'Name',
        validators= [
            MinLengthValidator(4 ,' name must grater than 4 charectors '),
        ]
    )
    slug = models.SlugField(
        max_length = 70,
        unique=True,
        verbose_name = 'slug',
        validators= [
            MinLengthValidator(4 ,' slug must grater than 4 charectors '),

        ]
    )
    shot_description= models.CharField(
        max_length = 200,
        verbose_name = 'short description',
        blank=True,
        null= True,
    )
    long_description=models.TextField(
        verbose_name ='deatiled description',
        null = True,
        blank=True,
        validators= [
            MaxLengthValidator(3000, ' the value is too long')
        ]
    )

    price = models.FloatField(
        verbose_name = 'price',
        validators= [
            MinValueValidator(600 , ' price must gratehan 600 value.'),
            MaxValueValidator( 1000000, 'price is too huge value') 
        ]
    )

    stock = models.IntegerField(
        verbose_name = 'stock',
        validators = [
            MinValueValidator(1, 'required at least 1 stock.'),
            MaxValueValidator(100, 'stocke value is too big')
        ]
    )

    category = models.ForeignKey(
        Category,
        on_delete= models.PROTECT,
        verbose_name= 'category'
    )

    brand = models.ForeignKey(
        Brand,
        on_delete = models.PROTECT,
        verbose_name= 'brand'
    )
    created_on = models.DateTimeField(
        auto_now_add=True,
        verbose_name= 'created on'
    )

    upadated_on = models.DateTimeField(
        verbose_name = 'updated on',
        auto_now = True
    )

    image = models.ImageField(
        upload_to ='products/images/',
    )
    status = models.CharField(
        max_length =25,
        choices= status,
    )
    def __str__(self):
        return self.name
