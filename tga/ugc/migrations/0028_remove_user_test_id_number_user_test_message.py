# Generated by Django 4.1.4 on 2023-05-02 11:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ugc', '0027_remove_test_result_image_test_result_file'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user_test',
            name='id_number',
        ),
        migrations.AddField(
            model_name='user_test',
            name='message',
            field=models.TextField(default=2),
            preserve_default=False,
        ),
    ]
