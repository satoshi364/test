from selenium import webdriver
import time
from locators import TestLocators

class TestWeb:
    def test_positive_case(self):
        browser = webdriver.Chrome()
        browser.get("https://rusia-fashion.ru")

        open_dresses = browser.find_element_by_xpath(TestLocators.loc_open_dresses)
        time.sleep(2)
        or_text_open_dresses = open_dresses.text
        print(f'текущий результат - {or_text_open_dresses}')
        example_open_dresses = 'ПЛАЩИ И ВЕТРОВКИ'
        assert or_text_open_dresses == example_open_dresses
        open_dresses.click()

        open_dress = browser.find_element_by_xpath(TestLocators.loc_open_dress)
        open_dress.click()

        pop_up = browser.find_element_by_xpath(TestLocators.loc_open_dress)
        pop_up.click()

        add_to_cart = browser.find_element_by_xpath(TestLocators.loc_add_to_cart)
        time.sleep(2)
        add_to_cart.click()

        time.sleep(1)
        go_to_cart = browser.find_element_by_xpath(TestLocators.loc_go_to_cart)
        time.sleep(2)
        go_to_cart.click()

        making_order = browser.find_element_by_xpath(TestLocators.loc_making_order)
        time.sleep(2)
        making_order.click()

        my_name = browser.find_element_by_xpath(TestLocators.loc_my_name)
        my_name.send_keys('Линкольн Авраам Кольтович')

        my_mobile = browser.find_element_by_xpath(TestLocators.loc_my_mobile)
        my_mobile.send_keys('+7924123456')

        my_town = browser.find_element_by_xpath(TestLocators.loc_my_town)
        my_town.send_keys('Пенза')

        comment = browser.find_element_by_xpath(TestLocators.loc_comment)
        comment.send_keys('Проверочка')

        order_confirmation = browser.find_element_by_xpath(TestLocators.loc_order_confirmation)
        order_confirmation.click()

    def test_positive_case_2(self):
        print('privet')