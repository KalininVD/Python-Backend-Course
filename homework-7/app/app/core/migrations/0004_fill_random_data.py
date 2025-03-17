from django.db import migrations


def load_random_data(apps, schema_editor):
    with open("app/core/models/random_data.sql", "r", encoding="utf-8") as f:
        schema_editor.connection.cursor().execute(f.read())


class Migration(migrations.Migration):
    dependencies = [
        ("core", "0003_fill_mock_data"),
    ]

    operations = [
        migrations.RunPython(load_random_data),
    ]