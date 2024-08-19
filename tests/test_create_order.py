import pytest
import allure
from pages.main_page import MainPage
from pages.order_page import OrderPage
from selenium.webdriver.support.ui import WebDriverWait
from data.order_form_test_data import test_data
from data.allure_titles import generate_test_title


@pytest.mark.usefixtures("driver")
class TestOrder:

    def setup_method(self, method):
        self.main_page = MainPage(self.driver)
        self.order_page = OrderPage(self.driver)
        self.main_page.open()
        self.wait = WebDriverWait(self.driver, 10)

    @pytest.mark.parametrize("confirm_order", ["yes", "no"])
    @pytest.mark.parametrize("index, data", list(enumerate(test_data)))  # Передаем индекс и данные
    @pytest.mark.parametrize(
        "click_order_button_method",
        ["click_order_button_in_header", "click_order_button_in_main_page"],
    )
    def test_create_order(self, index, data, click_order_button_method, confirm_order, request):
        browser_name = request.node.callspec.params.get("driver", "unknown")
        test_title = generate_test_title(click_order_button_method, confirm_order, browser_name, index)
        allure.dynamic.title(test_title)

        # Точка входа
        with allure.step("1. Открыть главную страницу и перейти к форме заказа"):
            self.main_page.open()

        # Последовательный набор шагов
        with allure.step(f"2. Нажать на кнопку 'Заказать' ({click_order_button_method})"):
            if click_order_button_method == "click_order_button_in_header":
                self.main_page.click_order_button_in_header()
            else:
                self.main_page.click_order_button_in_main_page()

        with allure.step("3. Заполнить форму заказа и нажать 'Далее'"):
            self.order_page.fill_first_name(data["first_name"])
            self.order_page.fill_last_name(data["last_name"])
            self.order_page.fill_address(data["address"])
            self.order_page.fill_phone(data["phone"])
            self.order_page.click_metro_station_input()
            self.order_page.select_first_metro_station()
            self.order_page.click_next_button()

        with allure.step("4. Заполнить вторую форму заказа данными"):
            self.order_page.fill_rent_date(data["rent_date"])
            self.order_page.click_rent_period_dropdown()
            self.order_page.select_rent_duration()
            self.order_page.select_scooter_color(data["scooter_color"])
            self.order_page.click_order_button()

        # Уникальные шаги
        with allure.step(f"5. {('Подтвердить' if confirm_order == 'yes' else 'Отменить')} заказ"):
            assert self.order_page.is_order_modal_opened(), "Окно подтверждения заказа не открылось"
            if confirm_order == "yes":
                self.order_page.click_order_modal_yes_button()
                self.order_page.check_order_confirmation()
                self.order_page.click_view_order_status()
            else:
                self.order_page.click_order_modal_no_button()

        with allure.step("5. Вернуться на главную страницу кликнув на текст логотипа 'Самокат'"):
            self.order_page.click_logo_scooter()
        with allure.step("6. Открыть страницу Дзена кликну на текст логотипа 'Яндекс'"):
            self.order_page.click_logo_yandex()
