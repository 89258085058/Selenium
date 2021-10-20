import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture
def driver(request):
    wd = webdriver.Firefox()
    request.addfinalizer(wd.quit)
    return wd


def test_login(driver):
    #OPEN MAIN PAGE
    driver.get("http://localhost/litecart/admin/")
    #input login
    driver.find_element_by_name('username').clear()
    driver.find_element_by_name('username').send_keys('admin')
    #input password
    driver.find_element_by_name('password').clear()
    driver.find_element_by_name('password').send_keys('admin')
    # submit button
    driver.find_element_by_name("login").click()
    # check page
    WebDriverWait(driver, 10).until(EC.url_contains("http://localhost/litecart/admin/"))

