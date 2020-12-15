from django.db import migrations, models


def add_initial_data(apps, schema_editor):
    Region = apps.get_model('Demo', 'Region')
    City = apps.get_model('Demo', 'City')
    Voie = apps.get_model('Demo', 'Voie')

    Orientale = Region.objects.create(name='Orientale')
    Oujda = City.objects.create(name='Oujda', region=Orientale)
    Berkane = City.objects.create(name='Berkane', region=Orientale)
    Ahfir = City.objects.create(name='Ahfir', region=Orientale)
    City.objects.create(name='Nador', region=Orientale)
    City.objects.create(name='Figuig', region=Orientale)

    FM = Region.objects.create(name='Fès-Meknès')
    City.objects.create(name='Fès', region=FM)
    City.objects.create(name='Meknes', region=FM)

    Tang = Region.objects.create(name='Tanger-Tétouan-Al Hoceïma')
    City.objects.create(name='Tanger', region=Tang)
    City.objects.create(name='Tétouan', region=Tang)
    City.objects.create(name='Al Hoceima', region=Tang)


class Migration(migrations.Migration):

    dependencies = [
        ('Demo', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(add_initial_data),
    ]
