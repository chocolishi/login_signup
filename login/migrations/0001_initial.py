# Generated by Django 2.1.4 on 2018-12-16 05:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Uesr',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('sex', models.CharField(choices=[('male', '男'), ('female', '女'), ('unknown-sex', '性别未选择')], default='性别未选择', max_length=50)),
                ('c_time', models.DateTimeField(auto_now_add=True)),
                ('age', models.IntegerField()),
                ('evaluation', models.TextField(max_length=500)),
                ('identification_photo', models.ImageField(height_field='url_height', upload_to='image_uploads/%Y/%m/%d/', width_field='url_width')),
                ('resume', models.FileField(upload_to='file_uploads/%Y/%m/%d')),
            ],
            options={
                'verbose_name': '用户',
                'verbose_name_plural': '用户',
                'ordering': ['-c_time'],
            },
        ),
    ]
