# Generated by Django 5.0 on 2023-12-26 04:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('back_app', '0019_alter_order_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='image',
            field=models.CharField(blank=True, max_length=1150, null=True),
        ),
    ]
