from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class MainPage:
    def __init__(self, driver: WebDriver) -> None:
        self.driver = driver

    # Навигация по основным разделам
    def open(self) -> None:
        self.driver.get('https://tehnomaks.ru/')

    def open_promotion(self):
        link = self.driver.find_element(By.CSS_SELECTOR, '.header-bottom__url')
        # Нажатие на элемент с помощью JavaScript
        self.driver.execute_script("arguments[0].click();", link)
        return self.driver.current_url.endswith('post/category/stock')

    def open_equipment_catalog(self):
        link = self.driver.find_element(By.CSS_SELECTOR,
                                        '.catalog-list__url.catalog-list__caret')
        self.driver.execute_script("arguments[0].click();", link)
        return self.driver.current_url.endswith(
            'catalog/section/kompyutery-noutbuki-komplektuyshie_po')

    def open_news_page(self):
        link = self.driver.find_element(By.CSS_SELECTOR, '.header-bottom__url')
        self.driver.execute_script("arguments[0].click();", link)
        link = self.driver.find_element(By.CSS_SELECTOR, '.sidebar-links__item')
        self.driver.execute_script("arguments[0].click();", link)
        return self.driver.current_url.endswith('post/category/news')

    def open_computer_catalog(self):
        link = self.driver.find_element(By.CSS_SELECTOR,
                                        '.catalog-list__url.catalog-list__caret')
        self.driver.execute_script("arguments[0].click();", link)
        link = self.driver.find_element(By.LINK_TEXT, 'Компьютеры, ноутбуки')
        self.driver.execute_script("arguments[0].click();", link)
        link = self.driver.find_element(By.LINK_TEXT, 'Брендовые ПК')
        self.driver.execute_script("arguments[0].click();", link)
        return self.driver.current_url.endswith('/catalog/section/brand-pc')

    def open_vacancies_page(self):
        link = self.driver.find_element(By.LINK_TEXT, 'Вакансии')
        self.driver.execute_script("arguments[0].click();", link)
        return self.driver.current_url.endswith('/vacancy')

    def open_trade_in_page(self):
        link = self.driver.find_element(By.LINK_TEXT, 'Трейд-ин')
        self.driver.execute_script("arguments[0].click();", link)
        return self.driver.current_url.endswith('/trade_in')

    def search_products(self, product_name: str):
        input_form = self.driver.find_element(By.ID, 'search-input')
        input_form.send_keys(product_name)
        input_form.send_keys(Keys.ENTER)
        products_list = self.driver.find_elements(By.CSS_SELECTOR,
                                                  '.softiq-products-block.softiq-products-block_default.softiq-products-block_default-nohint')
        return products_list

    def open_non_existing_url(self):
        self.driver.get('https://tehnomaks.ru/some_link')
        error_text = self.driver.find_element(By.CSS_SELECTOR,
                                              '.page-header').text
        if error_text == '404 - страница не найдена':
            return 404

    def add_product_to_cart(self):
        self.driver.get(
            'https://tehnomaks.ru/catalog/detail/fccd7ed841f89cf5fd5bb57194025c70?articul=426620#')
        # Находим кнопку для добавления в корзину
        button = self.driver.find_element(By.CSS_SELECTOR,
                                          '.button-buy.add_to_cart')
        self.driver.execute_script("arguments[0].click();", button)
        cart = self.driver.find_element(By.CSS_SELECTOR,
                                        '.header-cart-block__minicart')
        self.driver.execute_script("arguments[0].click();", cart)
        product = self.driver.find_element(By.CSS_SELECTOR,
                                           '.cart-item__title').text
        if not 'iPhone 15 Pro Max' in product:
            return False
        return True

    def delete_product_from_cart(self):
        self.driver.get(
            'https://tehnomaks.ru/catalog/detail/fccd7ed841f89cf5fd5bb57194025c70?articul=426620#')
        # Находим кнопку для добавления в корзину
        button = self.driver.find_element(By.CSS_SELECTOR,
                                          '.button-buy.add_to_cart')
        self.driver.execute_script("arguments[0].click();", button)
        cart = self.driver.find_element(By.CSS_SELECTOR,
                                        '.header-cart-block__minicart')
        self.driver.execute_script("arguments[0].click();", cart)
        product = self.driver.find_element(By.CSS_SELECTOR,
                                           '.cart-item__title').text
        if not 'iPhone 15 Pro Max' in product:
            return False
        delete_button = self.driver.find_element(By.CSS_SELECTOR,
                                                 '.cart-item__increment.cart-item__increment--minus')
        self.driver.execute_script("arguments[0].click();", delete_button)
        return True


driver = webdriver.Chrome()
main_page = MainPage(driver)
print(main_page.add_product_to_cart())
