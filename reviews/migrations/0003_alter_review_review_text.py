# Generated by Django 5.1.2 on 2024-10-13 02:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0002_auto_20241013_0432'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='review_text',
            field=models.TextField(),
        ),
    ]
