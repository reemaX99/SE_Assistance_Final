# Generated by Django 4.1.1 on 2023-02-13 18:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('learn', '0004_remove_learn_video_learn_videofile'),
    ]

    operations = [
        migrations.AddField(
            model_name='learn',
            name='author',
            field=models.ForeignKey(default=1, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='learn',
            name='videofile',
            field=models.FileField(null=True, upload_to='videos/'),
        ),
    ]
