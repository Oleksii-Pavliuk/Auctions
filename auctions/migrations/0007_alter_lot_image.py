# Generated by Django 4.1.4 on 2022-12-29 12:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0006_alter_lot_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lot',
            name='image',
            field=models.FileField(upload_to='./auction/static/uploads/'),
        ),
    ]
