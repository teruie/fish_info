# Generated by Django 3.2.4 on 2021-07-28 12:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20)),
            ],
            options={
                'verbose_name': 'カテゴリー',
                'verbose_name_plural': 'カテゴリー',
            },
        ),
        migrations.CreateModel(
            name='Place',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20)),
            ],
            options={
                'verbose_name': '場所',
                'verbose_name_plural': '場所',
            },
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(default='ネーム', max_length=10, verbose_name='ユーザーネーム')),
                ('icon', models.ImageField(default='画像が設定されていません', upload_to='icon/', verbose_name='アイコン')),
                ('header', models.ImageField(default='画像が設定されていません', upload_to='header/', verbose_name='ヘッダー')),
                ('text', models.TextField(default='自己紹介文を入力してください', max_length=50, verbose_name='自己紹介')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_profile', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'プロフィール',
                'verbose_name_plural': 'プロフィール',
            },
        ),
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.UUIDField(db_index=True, default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=30, verbose_name='タイトル')),
                ('fish_img', models.ImageField(upload_to='images/', verbose_name='写真')),
                ('fishing_comment', models.TextField(max_length=100, verbose_name='釣果コメント')),
                ('length', models.IntegerField(blank=True, default=0, null=True, verbose_name='長さ')),
                ('weight', models.IntegerField(blank=True, default=0, null=True, verbose_name='重さ')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='作成日')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='更新日')),
                ('fish_category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='fish.category', verbose_name='魚種')),
                ('place', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='fish.place', verbose_name='場所')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': '投稿',
                'verbose_name_plural': '投稿',
            },
        ),
    ]
