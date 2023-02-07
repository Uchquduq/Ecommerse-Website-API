import random
from django.core.management.base import BaseCommand, CommandError
from django_seed import Seed
from store.models import Address, Customer

NAME = 'addresses'

class Command(BaseCommand):
    help = 'This command creates {NAME}'

    def add_arguments(self, parser):
        parser.add_argument(
            "--number", default=2, type=int, help="How many {NAME} you want to create"
        )

    def handle(self, *args, **options):
        number = options.get("number")
        seeder = Seed.seeder()
        all_customers = Customer.objects.all()
        seeder.add_entity(
            Address,
            number,
            {
                'street': lambda x: seeder.faker.street_address(),
                'city': lambda x: seeder.faker.city(),
                'customer': lambda x: random.choice(all_customers)
            },
        )
        
        seeder.execute()
        self.stdout.write(self.style.SUCCESS(f"{number} {NAME} created!"))

