# Generated by Django 4.2.7 on 2024-01-30 18:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('strona_glowna', '0007_alter_daneskladuchemicznego_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='gatunek',
            name='kategoria',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='gatunki', to='strona_glowna.kategorie'),
        ),
        migrations.AlterField(
            model_name='gatunek',
            name='Id_komentarza',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='strona_glowna.komentarze'),
        ),
    ]
