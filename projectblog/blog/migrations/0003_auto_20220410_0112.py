# Generated by Django 2.2.3 on 2022-04-10 04:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20220410_0110'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='excerto_post',
            field=models.TextField(),
        ),
    ]
