__winc_id__ = "d7b474e9b3a54d23bca54879a4f1855b"
__human_name__ = "Betsy Webshop"

import models
import populate_db
import data


def main():

    # FILL the DATABASE

    populate_db.populate_db()

    # SEARCH TERM in Product.name & Product.description, BONUS :)

    def search(term):
        list_search_product = []
        query = (models.Product.select()
                 .where(models.Product.name.contains(term) | models.Product.description.contains(term))
                 )
        for searchTerm in query:
            list_search_product.append(searchTerm.name)
        return print(f'List for search term "{term}": {list_search_product}')

# CALLS SEARCH

    search("160")
    search("500")
    search("necklace")

    # List products OWNED BY USER.

    def list_user_products(user_id):
        owned_products = []
        query = (models.Product
                 .select()
                 .where(models.Product.owned_by_user == user_id)
                 )
        for user_id in query:
            owned_products.append(user_id.name)
        return print(f'Products owned by {user_id.owned_by_user.first_name}:', owned_products)

    list_user_products(2)

    # List products for given TAG.

    def list_products_per_tag(tag_id):
        list_products_tag = []
        query = (models.ProductTag
                 .select()
                 .where(models.ProductTag.tag_id == tag_id)
                 )
        for tag_id in query:
            list_products_tag.append(tag_id.product.name)
        return print(f'List products for tag "{tag_id.tag.name}":', list_products_tag)

    # CALL LIST_PRODUCTS_PER_TAG

    list_products_per_tag(2)

    # ADD PRODUCT to database.

    def add_product_to_catalog(user_id, product):
        add_product = models.Product.create(name=product.name, description=product.description,
                                            price_per_unit=product.price_per_unit,  amount_stock=product.amount_stock, owned_by_user=user_id)
        return add_product

    # CALL ADD_PRODUCT_TO_CATALOG

    add_product_to_catalog(3, data.winc_product)

    # UPDATE STOCK value.

    def update_stock(product_id, new_quantity):
        new_stock = models.Product.update(amount_stock=new_quantity).where(
            models.Product.id == product_id)
        new_stock.execute()
        return new_stock

    # CALL UPDATE_STOCK

    update_stock(2, 15)

    # PURCHASE product, make TRANSACTION and UPDATE the STOCK.

    def purchase_product(product_id, buyer_id, quantity):

        # MAKE TRANSACTION
        make_transaction = models.Transactionbetsy.create(
            updated_at=models.date_now, t_user=buyer_id, t_product=product_id, quantity=quantity)

        # UPDATE STOCK
        quantity_now = models.Product.select(models.Product.amount_stock).where(
            models.Product.id == product_id).scalar()
        new_quantity = quantity_now - quantity

        update_stock(product_id, new_quantity)

        return make_transaction

    # CALL PURCHASE PRODUCT

    purchase_product(1, 3, 8)

    # REMOVE product

    def remove_product(product_id):
        remove_product = models.Product.delete().where(models.Product.id == product_id)
        return remove_product.execute()

    # CALL REMOVE_PRODUCT

    remove_product(6)


if __name__ == "__main__":
    main()
