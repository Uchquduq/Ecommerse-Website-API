import random
from django.contrib.admin.utils import flatten
from django.core.management.base import BaseCommand, CommandError
from django_seed import Seed
from store.models import Cart, CartItem, Product

NAME = 'carts'

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
            Cart,
            number
        )

        all_products = Product.objects.all()
        created_carts = seeder.execute()
        created_clean = flatten(list(created_carts.values()))

        for pk in created_clean:
            cart = Cart.objects.get(pk=pk)
        for i in range(2, random.randint(0, 7)):
            CartItem.objects.create(
                cart=cart,
                product=random.choice(all_products),
                quantity=random.randrange(1, 30, 2)
            )
        self.stdout.write(self.style.SUCCESS(f"{number} cart items created!"))

        self.stdout.write(self.style.SUCCESS(f"{number} {NAME} created!"))
