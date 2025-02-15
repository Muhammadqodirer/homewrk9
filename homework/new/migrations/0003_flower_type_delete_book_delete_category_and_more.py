# Generated by Django 4.2.5 on 2024-12-12 12:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('new', '0002_book_photo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Flower',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('publication_date', models.DateField(auto_now_add=True)),
                ('summary', models.TextField(blank=True, null=True)),
                ('photo', models.ImageField(upload_to='photos/')),
            ],
        ),
        migrations.CreateModel(
            name='Type',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Book',
        ),
        migrations.DeleteModel(
            name='Category',
        ),
        migrations.AddField(
            model_name='flower',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='new.type'),
        ),
    ]
