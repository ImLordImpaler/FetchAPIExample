# Generated by Django 3.0.5 on 2020-07-02 16:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task', models.CharField(max_length=100, null=True)),
                ('completed', models.BooleanField(default=False)),
            ],
        ),
    ]
