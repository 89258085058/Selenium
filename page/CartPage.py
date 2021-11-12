from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class CartPageHelper:

    def __init__(self, app):
        self.app = app
        self.wait = WebDriverWait(self.app.wd, 10)

    def go_to_cart_page(self):
        wd = self.app.wd
        if not (wd.current_url == "http://localhost/litecart/en/checkout"):
            wd.find_element_by_link_text("Checkout »").click()

    def del_items_from_cart(self):
        wd = self.app.wd
        self.go_to_cart_page()
        item_list = wd.find_elements_by_css_selector("[name='cart_form']")
        for item in range(len(item_list)):
            table = wd.find_element_by_css_selector(".dataTable")
            wd.find_element_by_css_selector("[name='cart_form']").find_element_by_name("remove_cart_item").click()
            wait = WebDriverWait(wd, 5)
            wait.until(ec.staleness_of(table))
        assert wd.find_element_by_css_selector("#checkout-cart-wrapper em").text == "There are no items in your cart."
