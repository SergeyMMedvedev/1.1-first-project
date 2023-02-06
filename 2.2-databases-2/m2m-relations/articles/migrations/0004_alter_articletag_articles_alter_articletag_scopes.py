# Generated by Django 4.1.4 on 2022-12-29 13:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0003_remove_articletag_article_remove_articletag_tag_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articletag',
            name='articles',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='article_tags', to='articles.article', verbose_name='Статья'),
        ),
        migrations.AlterField(
            model_name='articletag',
            name='scopes',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='article_tags', to='articles.tag', verbose_name='Раздел'),
        ),
    ]