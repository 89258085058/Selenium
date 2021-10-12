import pytest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture
def driver(request):
    wd = webdriver.Firefox()
    request.addfinalizer(wd.quit)
    return wd


def test_example(driver):
    driver.get("https://software-testing.ru/")
    driver.find_element_by_name("q").send_keys("webdriver" + Keys.ENTER)
    WebDriverWait(driver, 10).until(EC.title_is("Software-Testing.Ru"))