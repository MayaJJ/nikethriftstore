# Generated by Django 3.1.3 on 2024-01-01 12:11

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('price', models.FloatField(validators=[django.core.validators.MinValueValidator(0.0)])),
                ('img', models.ImageField(upload_to='image/')),
                ('description', models.TextField(blank=True)),
                ('seller', models.CharField(max_length=200)),
                ('category', models.CharField(max_length=200)),
                ('date_posted', models.DateTimeField(auto_now_add=True)),
                ('is_sold', models.BooleanField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['date_posted'],
            },
        ),
    ]
