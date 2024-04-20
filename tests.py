from main import MainPage
from selenium import webdriver
driver = webdriver.Chrome()

def test_open_promotion():
    page = MainPage(driver)
    page.open()
    assert page.open_promotion()

def test_open_equipment_catalog():
    page = MainPage(driver)
    page.open()
    assert page.open_equipment_catalog()

def test_open_news_page():
    page = MainPage(driver)
    page.open()
    assert page.open_news_page()

def test_open_computer_catalog():
    page = MainPage(driver)
    page.open()
    assert page.open_computer_catalog()

def test_open_vacancies_page():
    page = MainPage(driver)
    page.open()
    assert page.open_vacancies_page()

def test_open_trade_in_page():
    page = MainPage(driver)
    page.open()
    assert page.open_trade_in_page()

def test_search_products():
    page = MainPage(driver)
    page.open()
    assert page.search_products('iphone 15 pro max')

def test_open_non_existing_url():
    page = MainPage(driver)
    assert page.open_non_existing_url() == 404

def test_add_product_to_cart():
    page = MainPage(driver)
    assert page.add_product_to_cart()

def test_delete_product_from_cart():
    page = MainPage(driver)
    assert page.delete_product_from_cart()