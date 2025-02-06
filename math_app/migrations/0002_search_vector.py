from django.db import migrations, connection

def create_search_vector_trigger(apps, schema_editor):
    with connection.cursor() as cursor:
        cursor.execute("""
            CREATE TRIGGER problems_search_update
            BEFORE INSERT OR UPDATE ON problems
            FOR EACH ROW EXECUTE FUNCTION
            tsvector_update_trigger(search_vector, 'pg_catalog.english', title, statement, answer);
        """)

def remove_search_vector_trigger(apps, schema_editor):
    with connection.cursor() as cursor:
        cursor.execute("DROP TRIGGER IF EXISTS problems_search_update ON problems;")

class Migration(migrations.Migration):

    dependencies = [
         ('math_app', '0001_alter_problems_options'),
    ]

    operations = [
        migrations.RunPython(create_search_vector_trigger, remove_search_vector_trigger),
    ]
