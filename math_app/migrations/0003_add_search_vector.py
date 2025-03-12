from django.db import migrations
import django.contrib.postgres.search

class Migration(migrations.Migration):
    dependencies = [
        ('math_app', '0002_search_vector'),
    ]

    operations = [
        migrations.AddField(
            model_name='problems',
            name='search_vector',
            field=django.contrib.postgres.search.SearchVectorField(null=True, editable=False),
        ),
    ]