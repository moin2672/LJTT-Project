# Generated by Django 4.1 on 2022-08-07 05:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lessonName', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='LJTTCard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imageData', models.TextField()),
                ('jp_word', models.TextField()),
                ('en_word', models.TextField()),
                ('en_pronounciation', models.TextField()),
                ('ta_word', models.TextField()),
                ('ta_pronounciation', models.TextField()),
                ('hint', models.TextField(blank=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('lesson', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ljttcards.lesson')),
                ('user', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='LJTTCard', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]