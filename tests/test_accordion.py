import pytest
import allure
from data.accordion_data import accordion_data
from pages.main_page import MainPage
from locators.main_page_locators import MainPageLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time


@pytest.mark.usefixtures("driver")

class TestAccordion:
    @allure.step("Открываем главную страницу Аренды самоката'")
    def setup_method(self, method):
        self.page = MainPage(self.driver)
        self.page.open()
        self.wait = WebDriverWait(self.driver, 3)

    @allure.step("Прокрутка к секции 'Вопросы о важном'")
    def scroll_to_faq_section(self):
        self.page.scroll_to_faq_section()

    @allure.title(
        "[Вопросы о важном] Проверка на соответствие текста в ответе на 1 вопрос"
    )
    @allure.description(
        "Клик по вопросу и проверка ответа"
    )
    def test_first_question(self):
        self.scroll_to_faq_section()
        self.page.click_question(MainPageLocators.QUESTION_0)
        answer_text = self.page.get_answer_text(MainPageLocators.ANSWER_0)
        assert (
            answer_text == accordion_data["items"][0]["answer"]
        ), f"Expected '{accordion_data['items'][0]['answer']}', but got '{answer_text}'"
        time.sleep(3)

    @allure.title(
        "[Вопросы о важном] Проверка на соответствие текста в ответе на 2 вопрос"
    )
    @allure.description(
        "Клик по вопросу и проверка ответа"
    )
    def test_second_question(self):
        self.scroll_to_faq_section()
        self.page.click_question(MainPageLocators.QUESTION_1)
        answer_text = self.page.get_answer_text(MainPageLocators.ANSWER_1)
        assert (
            answer_text == accordion_data["items"][1]["answer"]
        ), f"Expected '{accordion_data['items'][1]['answer']}', but got '{answer_text}'"
        time.sleep(3)

    @allure.title(
        "[Вопросы о важном] Проверка на соответствие текста в ответе на 3 вопрос"
    )
    @allure.description(
        "Клик по вопросу и проверка ответа"
    )
    def test_third_question(self):
        self.scroll_to_faq_section()
        self.page.click_question(MainPageLocators.QUESTION_2)
        answer_text = self.page.get_answer_text(MainPageLocators.ANSWER_2)
        assert (
            answer_text == accordion_data["items"][2]["answer"]
        ), f"Expected '{accordion_data['items'][2]['answer']}', but got '{answer_text}'"
        time.sleep(3)

    @allure.title(
        "[Вопросы о важном] Проверка на соответствие текста в ответе на 4 вопрос"
    )
    @allure.description(
        "Клик по вопросу и проверка ответа"
    )
    def test_fourth_question(self):
        self.scroll_to_faq_section()
        self.page.click_question(MainPageLocators.QUESTION_3)
        answer_text = self.page.get_answer_text(MainPageLocators.ANSWER_3)
        assert (
            answer_text == accordion_data["items"][3]["answer"]
        ), f"Expected '{accordion_data['items'][3]['answer']}', but got '{answer_text}'"
        time.sleep(3)

    @allure.title(
        "[Вопросы о важном] Проверка на соответствие текста в ответе на 5 вопрос"
    )
    @allure.description(
        "Клик по вопросу и проверка ответа"
    )
    def test_fifth_question(self):
        self.scroll_to_faq_section()
        self.page.click_question(MainPageLocators.QUESTION_4)
        answer_text = self.page.get_answer_text(MainPageLocators.ANSWER_4)
        assert (
            answer_text == accordion_data["items"][4]["answer"]
        ), f"Expected '{accordion_data['items'][4]['answer']}', but got '{answer_text}'"
        time.sleep(3)

    @allure.title(
        "[Вопросы о важном] Проверка на соответствие текста в ответе на 6 вопрос"
    )
    @allure.description(
        "Клик по вопросу и проверка ответа"
    )
    def test_sixth_question(self):
        self.scroll_to_faq_section()
        self.page.click_question(MainPageLocators.QUESTION_5)
        answer_text = self.page.get_answer_text(MainPageLocators.ANSWER_5)
        assert (
            answer_text == accordion_data["items"][5]["answer"]
        ), f"Expected '{accordion_data['items'][5]['answer']}', but got '{answer_text}'"
        time.sleep(3)

    @allure.title(
        "[Вопросы о важном] Проверка на соответствие текста в ответе на 7 вопрос"
    )
    @allure.description(
        "Клик по вопросу и проверка ответа"
    )
    def test_seventh_question(self):
        self.scroll_to_faq_section()
        self.page.click_question(MainPageLocators.QUESTION_6)
        answer_text = self.page.get_answer_text(MainPageLocators.ANSWER_6)
        assert (
            answer_text == accordion_data["items"][6]["answer"]
        ), f"Expected '{accordion_data['items'][6]['answer']}', but got '{answer_text}'"
        time.sleep(3)

    @allure.title(
        "[Вопросы о важном] Проверка на соответствие текста в ответе на 8 вопрос"
    )
    @allure.description(
        "Клик по вопросу и проверка ответа"
    )
    def test_eighth_question(self):
        self.scroll_to_faq_section()
        self.page.click_question(MainPageLocators.QUESTION_7)
        answer_text = self.page.get_answer_text(MainPageLocators.ANSWER_7)
        assert (
            answer_text == accordion_data["items"][7]["answer"]
        ), f"Expected '{accordion_data['items'][7]['answer']}', but got '{answer_text}'"
        time.sleep(3)



