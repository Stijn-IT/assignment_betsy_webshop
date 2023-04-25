import models
import datetime
my_date_now = datetime.datetime.now()
date_now = my_date_now.strftime("%Y-%m-%d, %H:%M:%S")

# USERS

Jan = models.User(first_name='Jan', last_name="Janssen", address_data="Janstraat 3",
                  bank_account_number="INGB0738324")
Klaas = models.User(first_name='Klaas', last_name="Claasen", address_data="Klaasstraat 3",
                    bank_account_number="RABO932042")
Wincstudent = models.User(first_name='Wincstudent', last_name='Wincy', address_data="Wincstraat 3",
                          bank_account_number="234dfadfafa1")

# TAGS

clothes = models.Tag(name='clothes')
jewellery = models.Tag(name='jewellery')
furniture = models.Tag(name='furniture')
food = models.Tag(name='food')
silver = models.Tag(name='silver')
gold = models.Tag(name='gold')
wood = models.Tag(name='wood')
wool = models.Tag(name='wool')

# PRODUCTS

wool_sock = models.Product(
    name="sock", description="Wool sock", price_per_unit=5.50, amount_stock=10, owned_by_user=1)
necklace = models.Product(
    name="necklace silver", description="silver necklace", price_per_unit=45, amount_stock=5, owned_by_user=1)
necklace_gold = models.Product(
    name="necklace gold", description="gold necklace", price_per_unit=95, amount_stock=3, owned_by_user=2)
table = models.Product(
    name="table", description="Oak round table 160 x 160", price_per_unit=120, amount_stock=1, owned_by_user=2)
apple_pie = models.Product(
    name="apple Pie", description="apple pie 500 grams", price_per_unit=3.50, amount_stock=1, owned_by_user=2)

# winc_product will be added in add_product_to_catalog, main.py.
winc_product = models.Product(
    name="winc product", description="best IT academy", price_per_unit=5000, amount_stock=1000, owned_by_user=None)

# TRANSACTION

Jan_table = models.Transactionbetsy(
    name="Jan Table", updated_ad=date_now, t_user=1, t_product=3, quantity=1)
Klaas_apple_pie = models.Transactionbetsy(
    name="Klaas Apple Pie", updated_ad=date_now, t_user=2, t_product=4, quantity=2)

# PRODUCTTAGS

tag_woolsock_1 = models.ProductTag(product=1, tag=1)
tag_woolsock_2 = models.ProductTag(product=1, tag=8)
tag_necklace_silver_1 = models.ProductTag(product=2, tag=2)
tag_necklace_silver_2 = models.ProductTag(product=2, tag=5)
tag_necklace_gold_1 = models.ProductTag(product=3, tag=6)
tag_necklace_gold_2 = models.ProductTag(product=3, tag=2)
tag_table_1 = models.ProductTag(product=4, tag=3)
tag_table_2 = models.ProductTag(product=4, tag=7)
tag_apple_pie = models.ProductTag(product=5, tag=4)

# LISTS to be added.

list_users = [Jan, Klaas, Wincstudent]
list_tags = [clothes, jewellery, furniture, food, silver, gold, wood, wool]
list_products = [wool_sock, necklace, necklace_gold, table, apple_pie]
list_transactions = [Jan_table, Klaas_apple_pie]
list_product_tags = [tag_woolsock_1,
                     tag_woolsock_2, tag_necklace_silver_1, tag_necklace_silver_2, tag_necklace_gold_1, tag_necklace_gold_2, tag_table_1, tag_table_2, tag_apple_pie]
