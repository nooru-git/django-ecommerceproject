# Generated by Django 4.0.2 on 2022-05-16 08:47

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50, unique=True, validators=[django.core.validators.MinLengthValidator(2, 'brand name must to be grater than 2 charectors ')], verbose_name='name')),
                ('slug', models.SlugField(unique=True, validators=[django.core.validators.MinLengthValidator(2, 'brand slug must graterthan 2 charestors')], verbose_name='slug')),
                ('description', models.CharField(blank=True, max_length=250, null=True, verbose_name='description')),
                ('website', models.URLField(blank=True, max_length=70, null=True, verbose_name='website')),
                ('created_on', models.DateTimeField(auto_now_add=True, verbose_name='created on')),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100, unique=True, validators=[django.core.validators.MinLengthValidator(2, 'Category Name must to be grater than 2 charecters')], verbose_name='Category Name')),
                ('slug', models.SlugField(unique=True, validators=[django.core.validators.MinLengthValidator(2, 'Category Name must to be grater than 2 charecters')], verbose_name='Category Slugs')),
                ('description', models.TextField(blank=True, max_length=100, null=True, verbose_name='Category Description')),
                ('created_on', models.DateField(auto_now_add=True, verbose_name='Category Created On')),
                ('upadated_on', models.DateField(auto_now=True, verbose_name='Updated On')),
            ],
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50, unique=True)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('message', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=70, unique=True, validators=[django.core.validators.MinLengthValidator(4, ' name must grater than 4 charectors ')], verbose_name='Name')),
                ('slug', models.SlugField(max_length=70, unique=True, validators=[django.core.validators.MinLengthValidator(4, ' slug must grater than 4 charectors ')], verbose_name='slug')),
                ('shot_description', models.CharField(blank=True, max_length=200, null=True, verbose_name='short description')),
                ('long_description', models.TextField(blank=True, null=True, validators=[django.core.validators.MaxLengthValidator(3000, ' the value is too long')], verbose_name='deatiled description')),
                ('price', models.FloatField(validators=[django.core.validators.MinValueValidator(600, ' price must gratehan 600 value.'), django.core.validators.MaxValueValidator(50000, 'price is too huge value')], verbose_name='price')),
                ('stock', models.IntegerField(validators=[django.core.validators.MinValueValidator(1, 'required at least 1 stock.'), django.core.validators.MaxValueValidator(100, 'stocke value is too big')], verbose_name='stock')),
                ('created_on', models.DateTimeField(auto_now_add=True, verbose_name='created on')),
                ('upadated_on', models.DateTimeField(auto_now=True, verbose_name='updated on')),
                ('image', models.ImageField(upload_to='products/images/')),
                ('status', models.CharField(choices=[('Active', 'Active'), ('Inactive', 'Inactive'), ('Out of stock', 'Out of stock')], max_length=25)),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='adminstrator.brand', verbose_name='brand')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='adminstrator.category', verbose_name='category')),
            ],
        ),
    ]
