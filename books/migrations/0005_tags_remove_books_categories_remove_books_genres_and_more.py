# Generated by Django 5.0.3 on 2024-03-17 18:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0004_genre_books_genres'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tags',
            fields=[
                ('tag_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='books',
            name='categories',
        ),
        migrations.RemoveField(
            model_name='books',
            name='genres',
        ),
        migrations.AddField(
            model_name='books',
            name='tags',
            field=models.ManyToManyField(blank=True, related_name='book_tags', to='books.tags'),
        ),
        migrations.DeleteModel(
            name='Category',
        ),
        migrations.DeleteModel(
            name='Genre',
        ),
    ]
