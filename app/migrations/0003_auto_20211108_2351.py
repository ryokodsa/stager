# Generated by Django 2.2.24 on 2021-11-08 14:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_calendar_link'),
    ]

    operations = [
        migrations.AlterField(
            model_name='calendar',
            name='link',
            field=models.CharField(max_length=1000, verbose_name='リンク'),
        ),
        migrations.CreateModel(
            name='Choice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('choice_text', models.CharField(max_length=200)),
                ('votes', models.IntegerField(default=0)),
                ('calendar', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Calendar')),
            ],
        ),
    ]