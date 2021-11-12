
def test_items_in_cart(app):
    product_list = app.cart.get_product_list()
    for ind in range(3):
        app.cart.add_item_to_cart(product_list, 1)
    app.cart.del_items_from_cart()