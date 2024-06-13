import csv
import random
import getpass
from django.core.management import call_command
from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand
from agenda.models import Talk, Track
import os

class Command(BaseCommand):
    help = 'Setup the Django application for demo purposes'

    # Create a constructor and create a user property
    def __init__(self):
        super().__init__()
        self.user = get_user_model()
        self.dir_path = os.path.dirname(os.path.realpath(__file__))


    def handle(self, *args, **options):
        self.run_migrations()
        self.create_superuser()
        self.create_speakers()
        self.populate_database_with_talks()
        self.stdout.write(self.style.SUCCESS('Successfully setup demo!'))

    def run_migrations(self):
        # Call the migrate command but suppress output
        call_command('migrate', verbosity=0)
        # Print status message saying database created
        self.stdout.write(self.style.MIGRATE_HEADING('Migrations run; database initialized!'))

    def create_superuser(self):
        username = input('Enter your username: ')
        first_name = input('Enter your first name: ')
        last_name = input('Enter your last name: ')
        email = input('Enter your email: ')
        password = getpass.getpass('Enter your password: ')
        self.user.objects.create_superuser(username, email, password, first_name=first_name, last_name=last_name)

    def create_speakers(self):
        # Load the user_data.csv file from dir_path
        with open(f'{self.dir_path}/user_data.csv', 'r') as f:
            reader = csv.reader(f)
            for row in reader:
                first_name, last_name = row
                username = first_name.lower()
                email = f'{first_name.lower()}@example.com'
                password = 'P@ssw0rd'
                bio = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nullam euismod, nisl eget aliquam ultricies, nunc nisl aliquet nunc, eget aliquam ni'
                self.user.objects.create_user(username, email, password, first_name=first_name, last_name=last_name, bio=bio)

    def populate_database_with_talks(self):
        users = self.user.objects.all()
        # Load data from starter_data.csv
        # The values are surrounded by quotes
        # Values are title, abstract, and track
        # Create the track as necessary, with a basic description of "<track> description"
        # Create a talk for each row in the CSV file
        # Assign a random speaker to each talk
        # Leave the default status

        with open(f'{self.dir_path}/starter_data.csv', 'r') as f:
            reader = csv.reader(f, quotechar='"', delimiter=',', quoting=csv.QUOTE_ALL, skipinitialspace=True)
            for row in reader:
                title, abstract, track = row
                track, _ = Track.objects.get_or_create(name=track, description=f'{track} description')
                speaker = random.choice(users)
                Talk.objects.create(title=title, abstract=abstract, track=track, speaker=speaker)