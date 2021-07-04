# Generated by Django 3.2.4 on 2021-07-04 22:38

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):
    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='authuser',
            name='role',
            field=models.PositiveSmallIntegerField(blank=True,
                                                   choices=[(4, 'Admin'), (3, 'Editor'), (1, 'Reader'), (2, 'Author')],
                                                   default=1, null=True, verbose_name='Role'),
        ),
        migrations.AlterField(
            model_name='authuser',
            name='uid',
            field=models.UUIDField(default=uuid.UUID('ccb93597-6433-4118-96d0-4e980e00b0cd'), editable=False,
                                   unique=True, verbose_name='Public identifier'),
        ),
    ]
