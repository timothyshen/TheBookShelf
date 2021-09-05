# Generated by Django 3.2.7 on 2021-09-05 17:19

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0021_auto_20210824_2143'),
    ]

    operations = [
        migrations.AlterField(
            model_name='authuser',
            name='role',
            field=models.PositiveSmallIntegerField(blank=True, choices=[(2, 'Author'), (4, 'Admin'), (3, 'Editor'), (1, 'Reader')], default=1, null=True, verbose_name='Role'),
        ),
        migrations.AlterField(
            model_name='authuser',
            name='uid',
            field=models.UUIDField(default=uuid.UUID('a5d7115b-f6c8-45b1-a883-c96c600d121b'), editable=False, unique=True, verbose_name='Public identifier'),
        ),
    ]
