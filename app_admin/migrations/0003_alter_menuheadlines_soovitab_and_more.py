# Generated by Django 4.2.7 on 2023-11-02 09:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_admin', '0002_menuheadlines'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menuheadlines',
            name='soovitab',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='menuheadlines',
            name='teema',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='menuheadlines',
            name='valmistas',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
