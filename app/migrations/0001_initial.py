# Generated by Django 3.2.3 on 2021-05-30 16:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('city', models.CharField(max_length=50)),
                ('zipcode', models.IntegerField()),
                ('state', models.CharField(choices=[('AP', 'Andhra Pradesh'), ('AR', 'Arunachal Pradesh'), ('AS', 'Assam'), ('BH', 'Bihar'), ('CH', 'Chhattisgarh'), ('GO', 'Goa'), ('GU', 'Gujrat'), ('HA', 'Haryana'), ('HI', 'Himachal Pradesh'), ('JK', 'Jharkhand'), ('KA', 'Karnataka'), ('KE', 'Kerala'), ('MP', 'Madhya Pradesh'), ('MA', 'Maharashtra'), ('MA', 'Manipur'), ('ME', 'Meghalaya'), ('MI', 'Mizoram'), ('NA', 'Nagaland'), ('OD', 'Odisha'), ('PU', 'Punjab'), ('RA', 'Rajasthan'), ('SI', 'Sikkim'), ('TN', 'Tamil Nadu'), ('TE', 'Telangana'), ('TR', 'Tripura'), ('UP', 'Uttar Pradesh'), ('UK', 'Uttarakhand'), ('WB', 'West Bengal'), ('AN', 'Andaman and Nicobar Island'), ('CH', 'Chandigarh'), ('DN', 'Dadra and Nagar Haveli and Daman and Diu'), ('DL', 'Delhi'), ('LA', 'Ladakh'), ('LK', 'Lakshadweep'), ('JA', 'Jammu and Kashmir'), ('PU', 'Puducherry')], max_length=50)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('category', models.CharField(choices=[('AC', 'Academy'), ('COMP', 'Competition')], max_length=50)),
                ('selling_price', models.FloatField()),
                ('discounted_price', models.FloatField()),
                ('description', models.TextField()),
                ('product_image', models.ImageField(upload_to='product_image')),
            ],
        ),
        migrations.CreateModel(
            name='OrderPlaced',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField(default=1)),
                ('order_date', models.DateTimeField(auto_now_add=True)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.customer')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.product')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField(default=1)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.product')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
