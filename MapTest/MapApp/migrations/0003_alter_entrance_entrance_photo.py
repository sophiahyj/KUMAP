# Generated by Django 4.0.6 on 2022-08-04 11:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MapApp', '0002_entrance_entrance_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entrance',
            name='entrance_photo',
            field=models.ImageField(blank=True, null=True, upload_to='user_<django.db.models.fields.related.ForeignKey>/<function filename at 0x10481c430>'),
        ),
    ]