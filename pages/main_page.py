from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.main_page_locators import MainPageLocators
from data.urls_site_data import Urls


class MainPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open(self):
        self.driver.get(Urls.MAIN_URL)

    def scroll_to_faq_section(self):
        faq_section = self.wait.until(
            EC.visibility_of_element_located((By.XPATH, MainPageLocators.FAQ_SECTION))
        )
        self.driver.execute_script("arguments[0].scrollIntoView();", faq_section)

    def click_question(self, question_xpath):
        question_element = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, question_xpath))
        )
        self.driver.execute_script("arguments[0].scrollIntoView();", question_element)
        question_element.click()

    def get_answer_text(self, answer_xpath):
        answer_element = self.wait.until(
            EC.visibility_of_element_located((By.XPATH, answer_xpath))
        )
        return answer_element.text

    def click_order_button_in_header(self):
        order_button = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, MainPageLocators.ORDER_BUTTON_HEADER))
        )
        order_button.click()
        self.wait.until(EC.url_to_be(Urls.ORDER_URL))

    def click_order_button_in_main_page(self):
        self.close_cookie_message()
        self.scroll_to_order_button()
        order_button = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, MainPageLocators.ORDER_BUTTON))
        )
        order_button.click()
        self.wait.until(EC.url_to_be(Urls.ORDER_URL))

    def scroll_to_order_button(self):
        order_button = self.wait.until(
            EC.visibility_of_element_located((By.XPATH, MainPageLocators.ORDER_BUTTON))
        )
        self.driver.execute_script("arguments[0].scrollIntoView(true); window.scrollBy(0, -100);", order_button)

    def close_cookie_message(self):
        try:
            cookie_button = self.wait.until(
                EC.element_to_be_clickable((By.XPATH, MainPageLocators.COOKIE_BUTTON))
            )
            cookie_button.click()
        except:
            pass  # Если сообщение о cookie не отображается, ничего не делаем