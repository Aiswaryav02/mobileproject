# Generated by Django 4.1.5 on 2023-02-06 15:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('store', '0002_products_prodimg'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='store',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='storeuser', to=settings.AUTH_USER_MODEL),
        ),
    ]
