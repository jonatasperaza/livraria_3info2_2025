# Generated by Django 5.1.7 on 2025-05-30 18:02

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_livro'),
    ]

    operations = [
        migrations.AddField(
            model_name='livro',
            name='autores',
            field=models.ManyToManyField(related_name='livros', to='core.autor'),
        ),
        migrations.AddField(
            model_name='livro',
            name='categoria',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.categoria'),
        ),
        migrations.AddField(
            model_name='livro',
            name='editora',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='livros', to='core.editora'),
        ),
    ]
