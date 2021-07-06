# Generated by Django 3.2.5 on 2021-07-06 09:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cl_hw', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='author',
            options={'ordering': ['id'], 'verbose_name': 'Author'},
        ),
        migrations.AlterModelOptions(
            name='quotes',
            options={'ordering': ['id'], 'verbose_name': 'Quotes'},
        ),
        migrations.AlterField(
            model_name='quotes',
            name='author',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='cl_hw.author'),
        ),
    ]
