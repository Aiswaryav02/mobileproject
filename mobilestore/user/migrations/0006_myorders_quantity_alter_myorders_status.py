# Generated by Django 4.1.5 on 2023-02-06 15:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0005_feedbackmodel'),
    ]

    operations = [
        migrations.AddField(
            model_name='myorders',
            name='quantity',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='myorders',
            name='status',
            field=models.CharField(max_length=100),
        ),
    ]