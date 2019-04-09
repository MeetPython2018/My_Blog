# Generated by Django 2.1.4 on 2018-12-19 08:11

import ckeditor.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=16, verbose_name='分类')),
            ],
            options={
                'verbose_name': '分类',
                'verbose_name_plural': '分类管理',
            },
        ),
        migrations.CreateModel(
            name='Keyword',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='分类的关键字')),
                ('c', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blogs.Category')),
            ],
        ),
        migrations.CreateModel(
            name='PTArticle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=32, verbose_name='文章标题')),
                ('con', ckeditor.fields.RichTextField()),
                ('c_time', models.DateTimeField(auto_now_add=True, verbose_name='发布日期')),
                ('u_time', models.DateTimeField(auto_now=True, verbose_name='更新日期')),
                ('a', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='作者')),
                ('c', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blogs.Category', verbose_name='分类')),
                ('k', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blogs.Keyword', verbose_name='关键字')),
            ],
            options={
                'verbose_name': '文章标题',
                'verbose_name_plural': '文章管理',
            },
        ),
    ]
