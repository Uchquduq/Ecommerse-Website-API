# Generated by Django 3.2.12 on 2022-11-09 22:16

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Collection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=255)),
                ('birth_date', models.DateField(blank=True, null=True)),
                ('membership', models.CharField(choices=[('B', 'Bronze'), ('S', 'Silver'), ('G', 'Gold')], default='Bronze', max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('placed_at', models.DateTimeField(auto_now_add=True)),
                ('payment_status', models.CharField(choices=[('P', 'Pending'), ('C', 'Complete'), ('F', 'Failed')], default='P', max_length=1)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='store.customer')),
            ],
            options={
                'permissions': [('cancel_order', 'Can cancel order')],
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('slug', models.SlugField()),
                ('description', models.TextField()),
                ('unit_price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('inventory', models.IntegerField()),
                ('last_update', models.DateTimeField(auto_now=True)),
                ('collection', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='store.collection')),
            ],
        ),
        migrations.CreateModel(
            name='Promotion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=255)),
                ('discount', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('date', models.DateField(auto_now_add=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='store.product')),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='promotions',
            field=models.ManyToManyField(blank=True, to='store.Promotion'),
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveSmallIntegerField(default=1, validators=[django.core.validators.MinValueValidator(1)])),
                ('unit_price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='store.order')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='orderitems', to='store.product')),
            ],
        ),
        migrations.AddField(
            model_name='collection',
            name='featured_product',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='store.product'),
        ),
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('street', models.CharField(max_length=255)),
                ('city', models.CharField(max_length=255)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.customer')),
            ],
        ),
        migrations.CreateModel(
            name='CartItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveSmallIntegerField(validators=[django.core.validators.MinValueValidator(1)])),
                ('cart', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='store.cart')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.product')),
            ],
            options={
                'unique_together': {('cart', 'product')},
            },
        ),
    ]
