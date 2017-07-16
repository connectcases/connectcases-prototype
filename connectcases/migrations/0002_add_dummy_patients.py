from django.db import migrations

def forwards_func(apps, schema_editor):
    Patient = apps.get_model("connectcases", "Patient")
    db_alias = schema_editor.connection.alias
    Patient.objects.using(db_alias).bulk_create([
        Patient(name="Tom"),
        Patient(name="David"),
        Patient(name="Harry"),
    ])

def reverse_func(apps, schema_editor):
    pass

class Migration(migrations.Migration):
    dependencies = [
        ('connectcases', '0001_initial'), 
    ]

    operations = [
        migrations.RunPython(forwards_func, reverse_func),
    ]
