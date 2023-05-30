from django.core.management.base import BaseCommand
from django.db import connection


class Command(BaseCommand):
    help = 'Imports an SQL file to create tables in SQLite3.'

    def add_arguments(self, parser):
        parser.add_argument('sql_file', type=str, help='Path to the SQL file to import.')

    def handle(self, *args, **options):
        sql_file = options['sql_file']

        with connection.cursor() as cursor:
            with open(sql_file, 'r') as f:
                sql_statements = f.read()

                try:
                    cursor.executescript(sql_statements)
                except Exception as e:
                    self.stderr.write(f'Error importing SQL file: {str(e)}')
                else:
                    self.stdout.write('SQL file imported successfully.')
