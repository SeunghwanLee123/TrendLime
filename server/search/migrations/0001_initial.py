# Generated by Django 3.2.9 on 2021-12-05 15:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_id', models.CharField(max_length=100)),
                ('category_name', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'category',
                'verbose_name_plural': 'categories',
                'db_table': 'tb_category',
            },
        ),
        migrations.CreateModel(
            name='Latest_100',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Topic', models.CharField(max_length=100)),
                ('Percentage', models.CharField(max_length=100)),
                ('song_id', models.CharField(max_length=100)),
                ('song_name', models.CharField(max_length=100)),
                ('artist', models.CharField(max_length=100)),
                ('album', models.CharField(max_length=100)),
                ('Like_Count', models.CharField(max_length=100)),
                ('Lyric', models.CharField(max_length=100)),
                ('cover_url', models.CharField(max_length=100)),
                ('tags', models.CharField(max_length=100)),
                ('year', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'latest_100',
                'db_table': 'tb_latest_100',
            },
        ),
        migrations.CreateModel(
            name='Song',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('song_id', models.CharField(max_length=100)),
                ('song_name', models.CharField(max_length=100)),
                ('artist', models.CharField(max_length=100)),
                ('album', models.CharField(max_length=100)),
                ('Like_Count', models.CharField(max_length=50)),
                ('Lyric', models.CharField(max_length=500)),
                ('cover_url', models.CharField(max_length=200)),
                ('tags', models.CharField(max_length=500)),
                ('year', models.CharField(max_length=4)),
            ],
            options={
                'verbose_name': 'song',
                'verbose_name_plural': 'songs',
                'db_table': 'tb_song',
            },
        ),
        migrations.CreateModel(
            name='Song_with_meta_emotion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('emotion', models.CharField(max_length=100)),
                ('percentage', models.CharField(max_length=100)),
                ('song_id', models.CharField(max_length=100)),
                ('song_name', models.CharField(max_length=100)),
                ('artist', models.CharField(max_length=100)),
                ('album', models.CharField(max_length=100)),
                ('Like_Count', models.CharField(max_length=100)),
                ('Lyric', models.CharField(max_length=100)),
                ('cover_url', models.CharField(max_length=100)),
                ('tags', models.CharField(max_length=100)),
                ('year', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'song_with_meta_emotion',
                'db_table': 'tb_song_with_meta_emotion',
            },
        ),
        migrations.CreateModel(
            name='Song_without_year',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Topic', models.CharField(max_length=100)),
                ('Percentage', models.CharField(max_length=100)),
                ('song_id', models.CharField(max_length=100)),
                ('song_name', models.CharField(max_length=100)),
                ('artist', models.CharField(max_length=100)),
                ('album', models.CharField(max_length=100)),
                ('Like_Count', models.CharField(max_length=50)),
                ('Lyric', models.CharField(max_length=500)),
                ('cover_url', models.CharField(max_length=200)),
                ('tags', models.CharField(max_length=500)),
            ],
            options={
                'verbose_name': 'song_withoout_year',
                'verbose_name_plural': 'songs_withoout_year',
                'db_table': 'tb_song_without_year',
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_id', models.CharField(max_length=100)),
                ('category_name', models.CharField(max_length=100)),
                ('tag_id', models.CharField(max_length=100)),
                ('tag_name', models.CharField(max_length=100)),
                ('tag_name_en', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'tag',
                'verbose_name_plural': 'tags',
                'db_table': 'tb_tag',
            },
        ),
        migrations.CreateModel(
            name='Top11',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('word', models.CharField(max_length=100)),
                ('freq', models.CharField(max_length=100)),
                ('year', models.CharField(max_length=4)),
            ],
            options={
                'verbose_name': 'top11',
                'db_table': 'tb_top11',
            },
        ),
        migrations.CreateModel(
            name='Top11_like100',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('word', models.CharField(max_length=100)),
                ('freq', models.CharField(max_length=100)),
                ('year', models.CharField(max_length=4)),
            ],
            options={
                'verbose_name': 'top11_like100',
                'db_table': 'tb_top11_like100',
            },
        ),
    ]
