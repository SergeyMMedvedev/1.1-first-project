# Generated by Django 4.1.4 on 2022-12-29 13:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0002_articletag_tag_articletag_tag'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='articletag',
            name='article',
        ),
        migrations.RemoveField(
            model_name='articletag',
            name='tag',
        ),
        migrations.AddField(
            model_name='articletag',
            name='articles',
            field=models.ForeignKey(blank=True, default='', on_delete=django.db.models.deletion.CASCADE, related_name='article_tags', to='articles.article', verbose_name='Статья'),
        ),
        migrations.AddField(
            model_name='articletag',
            name='scopes',
            field=models.ForeignKey(blank=True, default='', on_delete=django.db.models.deletion.CASCADE, related_name='article_tags', to='articles.tag', verbose_name='Раздел'),
        ),
        migrations.AlterField(
            model_name='articletag',
            name='is_main',
            field=models.BooleanField(verbose_name='Основной'),
        ),
        migrations.AlterField(
            model_name='tag',
            name='name',
            field=models.CharField(max_length=40, verbose_name='Раздел'),
        ),
    ]
