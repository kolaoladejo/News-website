# Generated by Django 4.0.5 on 2022-12-20 11:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('newsapp', '0003_alter_category_options_alter_news_options_comment'),
    ]

    operations = [
        migrations.RenameField(
            model_name='news',
            old_name='images',
            new_name='image',
        ),
    ]