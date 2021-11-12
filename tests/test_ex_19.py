
def test_page_object_working_with_cart(app):
    app.cart.add_to_cart_random_product()    # добавляем первый случайный продукт в корзину
    app.cart.add_to_cart_random_product()    # второй случайный продукт
    app.cart.add_to_cart_random_product()    # третий случай продукт
    app.cart.del_items_from_cart()           # удаляем все продукты из корзины