# Generated by Django 3.0.6 on 2020-06-17 13:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('heroes', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='heroes',
            name='agi_gain',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='heroes',
            name='attack_range',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='heroes',
            name='attack_rate',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='heroes',
            name='base_agi',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='heroes',
            name='base_armor',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='heroes',
            name='base_attack_max',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='heroes',
            name='base_attack_min',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='heroes',
            name='base_health',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='heroes',
            name='base_health_regen',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='heroes',
            name='base_int',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='heroes',
            name='base_mana',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='heroes',
            name='base_mana_regen',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='heroes',
            name='base_mr',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='heroes',
            name='base_str',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='heroes',
            name='cm_enabled',
            field=models.BooleanField(null=True),
        ),
        migrations.AddField(
            model_name='heroes',
            name='icon',
            field=models.CharField(default='null', max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='heroes',
            name='img',
            field=models.CharField(default='null', max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='heroes',
            name='int_gain',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='heroes',
            name='legs',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='heroes',
            name='localized_name',
            field=models.CharField(default='null', max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='heroes',
            name='move_speed',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='heroes',
            name='projectile_speed',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='heroes',
            name='str_gain',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='heroes',
            name='turn_rate',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='heroes',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
