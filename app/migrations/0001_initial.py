# Generated by Django 2.2.25 on 2022-12-12 17:23

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
            name='Auction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_price', models.IntegerField()),
                ('time_starting', models.DateTimeField()),
                ('time_ending', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('image', models.ImageField(upload_to='')),
                ('description', models.CharField(max_length=500)),
                ('quantity', models.IntegerField()),
                ('category', models.CharField(choices=[('ELC', 'Electronics'), ('UNI', 'Unique Items'), ('RES', 'Real Estate'), ('VEH', 'Vehicles'), ('OTH', 'Others')], max_length=2)),
                ('date_posted', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Bid',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bid_time', models.DateTimeField()),
                ('auction_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Auction')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='auction',
            name='product_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Product'),
        ),
    ]
