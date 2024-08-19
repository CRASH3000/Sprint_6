import pytest
import allure
from data.accordion_data import accordion_data
from pages.main_page import MainPage
from locators.main_page_locators import MainPageLocators
from selenium.webdriver.support.ui import WebDriverWait
from data.allure_titles import get_allure_title_for_question, get_allure_description_for_question


@pytest.mark.usefixtures("driver")
class TestAccordion:

    @allure.step("Открываем главную страницу Аренды самоката")
    def setup_method(self, method):
        self.page = MainPage(self.driver)
        self.page.open()
        self.wait = WebDriverWait(self.driver, 3)

    @allure.step("Прокрутка к секции 'Вопросы о важном'")
    def scroll_to_faq_section(self):
        self.page.scroll_to_faq_section()

    @allure.step("Клик по вопросу")
    @pytest.mark.parametrize(
        "question_xpath, answer_xpath, expected_answer, question_number",
        [
            (MainPageLocators.QUESTION_0, MainPageLocators.ANSWER_0, accordion_data["items"][0]["answer"], 1),
            (MainPageLocators.QUESTION_1, MainPageLocators.ANSWER_1, accordion_data["items"][1]["answer"], 2),
            (MainPageLocators.QUESTION_2, MainPageLocators.ANSWER_2, accordion_data["items"][2]["answer"], 3),
            (MainPageLocators.QUESTION_3, MainPageLocators.ANSWER_3, accordion_data["items"][3]["answer"], 4),
            (MainPageLocators.QUESTION_4, MainPageLocators.ANSWER_4, accordion_data["items"][4]["answer"], 5),
            (MainPageLocators.QUESTION_5, MainPageLocators.ANSWER_5, accordion_data["items"][5]["answer"], 6),
            (MainPageLocators.QUESTION_6, MainPageLocators.ANSWER_6, accordion_data["items"][6]["answer"], 7),
            (MainPageLocators.QUESTION_7, MainPageLocators.ANSWER_7, accordion_data["items"][7]["answer"], 8),
        ]
    )
    def test_question_answer(self, question_xpath, answer_xpath, expected_answer, question_number, request):
        # Установка динамического заголовка и описания для теста
        browser_name = request.node.callspec.params.get("driver", "unknown")
        allure.dynamic.title(get_allure_title_for_question(question_number, browser_name))
        allure.dynamic.description(get_allure_description_for_question(question_number))

        self.scroll_to_faq_section()
        self.page.click_question(question_xpath)
        answer_text = self.page.get_answer_text(answer_xpath)
        assert (
                answer_text == expected_answer
        ), f"Expected '{expected_answer}', but got '{answer_text}'"

