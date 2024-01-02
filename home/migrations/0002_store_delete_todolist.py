# Generated by Django 5.0 on 2024-01-02 09:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Store',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book_id', models.CharField(max_length=200)),
                ('author', models.CharField(max_length=200)),
                ('book_name', models.CharField(max_length=200)),
                ('price', models.IntegerField()),
            ],
        ),
        migrations.DeleteModel(
            name='ToDoList',
        ),
    ]