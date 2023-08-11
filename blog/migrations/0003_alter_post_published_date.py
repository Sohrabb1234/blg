# Generated by Django 3.2.20 on 2023-08-11 17:12

from django.db import migrations, models
import jdatetime


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_alter_post_created_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='published_date',
            field=models.DateTimeField(blank=True, default=jdatetime.datetime.now, null=True),
        ),
    ]
