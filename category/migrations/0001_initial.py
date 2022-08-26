# Generated by Django 3.2 on 2022-08-26 09:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('slug', models.SlugField(max_length=30, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=30, unique=True)),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='category', to='category.category')),
            ],
        ),
    ]
