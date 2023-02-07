import random
from django.core.management.base import BaseCommand, CommandError
from django_seed import Seed
from store.models import Promotion

NAME = 'promotions'

class Command(BaseCommand):
    help = 'This command creates {NAME}'

    def add_arguments(self, parser):
        parser.add_argument(
            "--number", default=2, type=int, help="How many {NAME} you want to create"
        )

    def handle(self, *args, **options):
        number = options.get("number")
        seeder = Seed.seeder()
        seeder.add_entity(
            Promotion,
            number,
            {
                'description': lambda x: seeder.faker.catch_phrase(),
                'discount': lambda x: random.randrange(1, 5)
            },
        )

        seeder.execute()
        self.stdout.write(self.style.SUCCESS(f"{number} {NAME} created!"))