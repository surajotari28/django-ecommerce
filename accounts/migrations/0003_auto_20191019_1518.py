# Generated by Django 2.2 on 2019-10-19 15:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20191019_1516'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='pseudo',
            field=models.CharField(blank=True, max_length=30, verbose_name='pseudo'),
        ),
    ]
