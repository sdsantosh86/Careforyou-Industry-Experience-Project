# Generated by Django 3.1 on 2020-09-05 11:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('careforyou', '0005_childcare_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='quality',
            name='area7',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='childcare',
            name='email',
            field=models.CharField(max_length=50, null=True),
        ),
    ]