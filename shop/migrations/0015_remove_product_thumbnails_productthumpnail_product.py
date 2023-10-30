# Generated by Django 4.2.5 on 2023-10-02 09:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0014_remove_product_thump_nail_product_thumbnails'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='thumbnails',
        ),
        migrations.AddField(
            model_name='productthumpnail',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_thump_nails', to='shop.product'),
            preserve_default=False,
        ),
    ]