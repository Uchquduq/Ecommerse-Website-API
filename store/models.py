from django.db import models

# Promotion  - Product M2M
class Promotion(models.Model):
    description = models.CharField(max_length=255)
    discount = models.FloatField()
    # product_set

    # def __str__(self):
    #     return self.description

class Collection(models.Model):
    title = models.CharField(max_length=255)
    featured_product = models.ForeignKey(
        'Product', on_delete=models.SET_NULL, null=True, blank=True, related_name="+") # when 2 models are connected in a circle relationship, if it says related name, you should add + to related name

    def __str__(self):
        return self.title


class Product(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField()
    description = models.TextField()
    unit_price = models.DecimalField(max_digits=6, decimal_places=2)
    inventory = models.IntegerField()
    last_update = models.DateTimeField(auto_now=True)
    collection = models.ForeignKey(Collection, on_delete=models.PROTECT)
    promotions = models.ManyToManyField(Promotion, blank=True) # related_name="products"

    def __str__(self):
        return self.title   

class Customer(models.Model):
    MEMBERSHIP_BRONZE = "Bronze"
    MEMBERSHIP_SILVER = "Silver"
    MEMBERSHIP_GOLD = "Gold"
    
    MEMBERSHIP_CHOICES = (
        ('B', MEMBERSHIP_BRONZE),
        ('S', MEMBERSHIP_SILVER),
        ('G', MEMBERSHIP_GOLD),
    )

    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=255)
    birth_date = models.DateField(null=True)
    membership = models.CharField(max_length=1, choices=MEMBERSHIP_CHOICES, default=MEMBERSHIP_BRONZE)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Order(models.Model):
    PAYMENT_STATUS_PENDING = 'P'
    PAYMENT_STATUS_COMPLETE = 'C'
    PAYMENT_STATUS_FAILED = 'F'

    PAYMENT_STATUS_CHOICES = (
        (PAYMENT_STATUS_PENDING, 'Pending'),
        (PAYMENT_STATUS_COMPLETE, 'Complete'),
        (PAYMENT_STATUS_FAILED, 'Failed')
    )
    placed_at = models.DateTimeField(auto_now_add=True)
    payment_status = models.CharField(max_length=1, default=PAYMENT_STATUS_PENDING, choices=PAYMENT_STATUS_CHOICES)
    customer = models.ForeignKey(Customer, on_delete=models.PROTECT)

    # def __str__(self):
    #     return self.customer.first_name

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.PROTECT)
    product = models.ForeignKey(Product, on_delete=models.PROTECT, related_name="orderitems")
    quantity = models.PositiveSmallIntegerField()
    unit_price = models.DecimalField(max_digits=6, decimal_places=2)

    # def __str__(self):
    #     return f"{self.order} ordered {self.product}"

class Cart(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveSmallIntegerField()

    # def __str__(self):
    #     return f"{self.cart} {self.product}"

class Address(models.Model):
    street = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    customer = models.ForeignKey(
        Customer, on_delete=models.CASCADE)

    # def __str__(self):
    #     return f"{self.customer} address: {self.street}, {self.city}"