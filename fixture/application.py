import allure
from selenium.webdriver.support.select import Select
from fixture.cart import CartHelper
from fixture.admin import AdminHelper
from fixture.sorted import SortedHelper
from fixture.session import SessionHelper
from fixture.sticker import StickerHelper
from fixture.product import ProductHelper
from fixture.customer import CustomerHelper
from fixture.window import WindowHelper
from fixture.main import MainHelper
from selenium import webdriver
from fixture.log import LogHelper
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from allure_commons.types import AttachmentType


class Application:


    def __init__(self, browser, base_url):
        if browser == "firefox":
            self.wd = webdriver.Firefox()
        elif browser == "chrome":
            self.wd = webdriver.Chrome()
        elif browser == "ie":
            self.wd = webdriver.Ie()
        else:
            raise ValueError("Unrecognized browser %s" % browser)
        self.wd.implicitly_wait(3)
        self.admin = AdminHelper(self)
        self.sorted = SortedHelper(self)
        self.sticker = StickerHelper(self)
        self.main = MainHelper(self)
        self.product = ProductHelper(self)
        self.session = SessionHelper(self)
        self.customer = CustomerHelper(self)
        self.cart = CartHelper(self)
        self.window = WindowHelper(self)
        self.log = LogHelper(self)
        self.base_url = base_url

    def open_admin_page(self):
        wd = self.wd
        if not wd.current_url.endswith("/admin/"):
            wd.get('http://localhost/litecart/admin/')

    def open_main_page(self):
        wd = self.wd
        if not wd.current_url.endswith("/litecart/en/"):
            wd.get('http://localhost/litecart/en/')

    def is_element_present(self, *args):
        wd = self.wd
        try:
            wd.find_element(*args)
            return True
        except NoSuchElementException:
            return False


    def destroy(self):
        allure.attach(self.wd.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
        self.wd.quit()



    def wait_until_element_present(self, locator):
        wd = self.wd
        wait = WebDriverWait(wd, 10)
        return wait.until(EC.presence_of_element_located((By.NAME, "%s" % locator)))

    def fill_field_value(self, field_name, text):
        wd = self.wd
        wd.find_element_by_name(field_name).click()
        wd.find_element_by_name(field_name).send_keys(text)

    def select_by_text(self, field_name, text):
        wd = self.wd
        select = Select(wd.find_element_by_name(field_name))
        select.select_by_visible_text(text)


    def wait_until_text_to_be_present_in_element(self, locator, text):
        wd = self.wd
        wait = WebDriverWait(wd, 10)
        return wait.until(EC.text_to_be_present_in_element(locator, text))

    def wait_until_staleness_of_element(self, element):
        wd = self.wd
        wait = WebDriverWait(wd, 10)
        return wait.until(EC.staleness_of(element))






