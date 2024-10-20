# Generated by Django 5.1.2 on 2024-10-20 19:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0003_alter_review_review_text'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='rating',
            field=models.IntegerField(default=3),
        ),
        migrations.AlterField(
            model_name='movie',
            name='description',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='movie',
            name='rating',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='movie',
            name='title',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='review',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
