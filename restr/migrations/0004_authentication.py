# Generated by Django 5.0.3 on 2024-03-14 16:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restr', '0003_delete_authentication'),
    ]

    operations = [
        migrations.CreateModel(
            name='Authentication',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=200)),
                ('password', models.CharField(max_length=50)),
            ],
        ),
    ]
