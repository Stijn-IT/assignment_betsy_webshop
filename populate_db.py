import models
import data
import datetime
my_date_now = datetime.datetime.now()
date_now = my_date_now.strftime("%Y-%m-%d, %H:%M:%S")


# POPULATE DB function.

def populate_db():

    models.db.create_tables(
        [models.User, models.Tag, models.Product, models.ProductTag, models.Transactionbetsy])

    for user in data.list_users:
        user.get_or_create(first_name=user.first_name, last_name=user.last_name,
                           address_data=user.address_data, bank_account_number=user.bank_account_number)

    for tag in data.list_tags:
        tag.get_or_create(name=tag.name)

    for product in data.list_products:
        product.get_or_create(name=product.name, description=product.description, price_per_unit=product.price_per_unit,
                              amount_stock=product.amount_stock, owned_by_user=product.owned_by_user_id)

    for producttag in data.list_product_tags:
        producttag.get_or_create(
            product=producttag.product_id, tag=producttag.tag_id)

    '''Onderstaand werkt get_or_create niet. Dit omdat updated_at een datum en tijd via datetime is.
Dit is dus steeds anders per seconde. Daarom heb ik nu try & except gebruikt en bij try updated_at weggehaald'''

    for transaction in data.list_transactions:
        try:
            transaction.get(t_user=transaction.t_user,
                            t_product=transaction.t_product, quantity=transaction.quantity)
        except transaction.DoesNotExist:
            transaction.create(updated_at=transaction.updated_at, t_user=transaction.t_user,
                               t_product=transaction.t_product, quantity=transaction.quantity)
