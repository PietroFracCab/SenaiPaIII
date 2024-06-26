# Generated by Django 5.0.6 on 2024-06-25 01:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meu_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Edificio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.IntegerField(default=0)),
                ('nome', models.CharField(max_length=100)),
                ('tipo', models.CharField(max_length=100)),
                ('loc', models.CharField(default='Não especificado', max_length=100)),
                ('custo_aquisicao', models.FloatField()),
                ('depreciacao_anual', models.FloatField()),
                ('expectativa_vida_util', models.IntegerField()),
                ('data_aquisicao', models.IntegerField(default=2024)),
            ],
        ),
        migrations.CreateModel(
            name='Equipamento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.IntegerField(default=0)),
                ('nome', models.CharField(max_length=100)),
                ('tipo', models.CharField(max_length=100)),
                ('loc', models.CharField(default='Não especificado', max_length=100)),
                ('custo_aquisicao', models.FloatField()),
                ('depreciacao_anual', models.FloatField()),
                ('expectativa_vida_util', models.IntegerField()),
                ('data_aquisicao', models.IntegerField(default=2024)),
            ],
        ),
        migrations.CreateModel(
            name='Veiculo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.IntegerField(default=0)),
                ('nome', models.CharField(max_length=100)),
                ('tipo', models.CharField(max_length=100)),
                ('loc', models.CharField(default='Não especificado', max_length=100)),
                ('custo_aquisicao', models.FloatField()),
                ('depreciacao_anual', models.FloatField()),
                ('expectativa_vida_util', models.IntegerField()),
                ('data_aquisicao', models.IntegerField(default=2024)),
            ],
        ),
        migrations.RenameField(
            model_name='maquina',
            old_name='custo_inicial',
            new_name='custo_aquisicao',
        ),
        migrations.AddField(
            model_name='maquina',
            name='codigo',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='maquina',
            name='data_aquisicao',
            field=models.IntegerField(default=2024),
        ),
        migrations.AddField(
            model_name='maquina',
            name='loc',
            field=models.CharField(default='Não especificado', max_length=100),
        ),
    ]
