# Generated by Django 4.1.7 on 2023-05-09 06:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('skincare_recommendation_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='function',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='review',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='warning',
            field=models.TextField(blank=True, null=True),
        ),
    ]
