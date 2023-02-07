import random
from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand, CommandError
from django_seed import Seed
from store.models import Address, Customer, Review, Product

NAME = 'reviews'

User = get_user_model()

class Command(BaseCommand):
    help = 'This command creates {NAME}'

    def add_arguments(self, parser):
        parser.add_argument(
            "--number", default=2, type=int, help="How many {NAME} you want to create"
        )

    def handle(self, *args, **options):
        number = options.get("number")
        seeder = Seed.seeder()
        all_users = User.objects.all()
        all_products = Product.objects.all()
        seeder.add_entity(
            Review,
            number,
            {
                'author': lambda x: random.choice(all_users),
                'product': lambda x: random.choice(all_products),
                'description': lambda x: seeder.faker.sentence(random.randrange(2, 10))
            },
        )
        
        seeder.execute()
        self.stdout.write(self.style.SUCCESS(f"{number} {NAME} created!"))

