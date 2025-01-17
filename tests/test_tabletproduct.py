import logging
import time


import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

from pageObjects.basePage import BasePage
from pageObjects.homePage import HomePage
from utilities.logger import LogGen


@pytest.mark.usefixtures("setup_and_teardown")
# @pytest.mark.skip(reason="Need to run the register test case separately")
# @pytest.mark.run(order=1)
class TestSelectProduct:
    logger = LogGen.log_gen()

    def test_select_tablet_product(self):
        logging.info("Program execution started")

        # Below is the method has been implemented before create the page Object:
        # self.driver.find_element(By.LINK_TEXT, "Tablets").click()
        # self.driver.find_element(By.XPATH, "//div[@class='button-group']//button[1]").click()
        # time.sleep(5)
        # self.driver.find_element(By.ID, "cart-total").click()
        # self.driver.find_element(By.XPATH, "//strong[text()='View Cart']").click()

        # Below is the method has been implemented after the Page Objects:
        select_tablet_product = HomePage(self.driver)
        select_tablet_product.do_click_tablet()
        select_tablet_product.do_click_product_cart_btn()
        select_tablet_product.do_click_top_totalcart_btn()
        select_tablet_product.do_click_view_cart_btn()
        logging.info("Program execution ended")




