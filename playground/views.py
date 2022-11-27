from django.shortcuts import render
from django.core.mail import mail_admins, send_mail, BadHeaderError, EmailMessage
from templated_mail.mail import BaseEmailMessage
from django.db import transaction
from django.db.models import Value, F, Func, ExpressionWrapper, DecimalField
from django.db.models.functions import Concat
from django.db.models.aggregates import Count, Max, Min, Avg, Sum
from django.contrib.contenttypes.models import ContentType
from tags.models import TaggedItem
from store.models import Order, Product, OrderItem, Customer, Collection


def say_hello(request):
    # queryset = Product.objects.all()

    # Products: inventory = unit_price
    # queryset = Product.objects.filter(
    #     inventory=F('unit_price')
    # )
    # sorting
    # queryset = Product.objects.order_by("unit_price")
    # limiting results
    # queryset = Product.objects.all()[:5]
    #
    # queryset = OrderItem.objects.values('product_id')
    # queryset = Product.objects.filter(id__in=OrderItem.objects.values('product_id').distinct()).order_by('title')

    # deffering fields
    # values va only o'rtasida farq only faqat object ni fieldlarini oladi values esa butun dict qilib oladi
    # queryset = Product.objects.only('id', 'title', 'unit_price')
    # queryset = Product.objects.defer('description')
    # select related
    # queryset = Product.objects.select_related('collection').all()

    # queryset = Product.objects.prefetch_related(
    #     'promotions').select_related('collection').all()
    # Select last 5 orders and their customer with their items(incl product)
    # orders = Order.objects.select_related('customer').order_by('-placed_at')[:5]
    # orders = Order.objects.select_related(
    #     'customer').prefetch_related('orderitem_set').order_by('-placed_at')[:5]
    # result = Product.objects.aggregate(Count('id')) # id_count: result
    # result = Product.objects.filter(collection__id=1).aggregate(
    #     count=Count('id'), min_price=Min('unit_price'))
    # queryset = Customer.objects.annotate(new_id=F('id'))
    # queryset = Customer.objects.annotate(
    #     # CONCAT
    #     full_name = Func(F('first_name'), Value(' '),
    #         F('last_name'), function='CONCAT')
    # )
    # queryset = Customer.objects.annotate(
    #     full_name=Concat('first_name', Value(' '), 'last_name')
    # )
    # queryset = Customer.objects.annotate(
    #     orders_count=Count('order')
    # )
    # queryset = Collection.objects.annotate(
    #     products_count=Count('product')
    # )
    # This query calculates the product price including tax

    # discounted_price = ExpressionWrapper(
    #     F('unit_price') * 0.8, output_field=DecimalField()
    # )
    # queryset = Product.objects.annotate(
    #     discounted_price=discounted_price
    # )

    # content_type = ContentType.objects.get_for_model(Product)

    # queryset = TaggedItem.objects \
    #     .select_related('tag') \
    #     .filter(
    #         content_type=content_type,
    #         object_id=1
    #     )

    #               Tramsactions
    # with transaction.atomic():

    #     order = Order()
    #     order.customer_id = 2
    #     order.save()

    #     item = OrderItem()
    #     item.order = order
    #     item.product_id = 2
    #     item.quantity = 2
    #     item.unit_price = 10
    #     item.save()
    try:
        # mail_admins('subject', 'message', html_message='message')
        message = EmailMessage(
                'subject', 
                'message', 
                settings.DEFAULT_FROM_EMAIL, 
                ['abduhakimovfazliddin2002@gmail.com'])
        # message.attach_file('playground/static/images/dog.jpg')
        message.send()


        # message = BaseEmailMessage(
        #     template_name="emails/hello.html", context={"name": "a"}
        # )
        # message.send(["abduhakimovfazliddin2002@gmail.com"])

    except BadHeaderError:
        pass

    context = {
        # "orders" : list(orders),
        # 'product': product,
        # 'result': result,
        # 'result': list(queryset)
        # 'tags': queryset,
    }
    return render(request, "emails/hello.html", context)


from django.conf import settings


def send_mail_message(request):
    message = request.POST.get('message')
    
    if request.method == "POST":
        send_mail('Contact Form', 
            message, 
            settings.EMAIL_HOST_USER, 
            ['abduhakimovfazliddin2002@gmail.com'],
            fail_silently=False)
    return render(request, "emails/send_email.html")

