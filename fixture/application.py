from fixture.admin import AdminHelper
from fixture.session import SessionHelper
from fixture.sticker import StickerHelper
from selenium import webdriver
from fixture.sorted import SortedHelper



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
        self.wd.implicitly_wait(5)
        self.session = SessionHelper(self)
        self.admin = AdminHelper(self)
        self.sticker = StickerHelper(self)
        self.sorted = SortedHelper(self)
        self.base_url = base_url


    def open_home_page(self):
        wd = self.wd
        wd.get(self.base_url)

    def destroy(self):
        self.wd.quit()

    def is_valid(self):
        try:
            self.wd.current_url
            return True
        except:
            return False