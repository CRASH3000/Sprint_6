import pytest
import allure
import time
from pages.main_page import MainPage
from pages.order_page import OrderPage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from data.urls_site_data import Urls
from locators.order_page_locators import OrderPageLocators
from data.order_form_test_data import test_data


@pytest.mark.usefixtures("driver")
class TestOrder:

    def setup_method(self, method):
        self.main_page = MainPage(self.driver)
        self.order_page = OrderPage(self.driver)
        self.main_page.open()
        self.wait = WebDriverWait(self.driver, 10)

    @allure.step("Клик на кнопку 'Заказать' в шапке сайта")
    def click_order_button_in_header(self):
        self.main_page.click_order_button_in_header()
        self.wait.until(EC.url_to_be(Urls.ORDER_URL))

    @allure.step("Клик на кнопку 'Заказать' на главной странице")
    def click_order_button_in_main_page(self):
        self.main_page.close_cookie_message()
        self.main_page.scroll_to_order_button()
        self.main_page.click_order_button()
        self.wait.until(EC.url_to_be(Urls.ORDER_URL))

    @allure.step("Заполнение имени")
    def fill_first_name(self, data):
        self.order_page.fill_first_name(data["first_name"])
        self.wait.until(
            EC.text_to_be_present_in_element_value(
                (By.XPATH, OrderPageLocators.FIRST_NAME_INPUT), data["first_name"]
            )
        )

    @allure.step("Заполнение фамилии")
    def fill_last_name(self, data):
        self.order_page.fill_last_name(data["last_name"])
        self.wait.until(
            EC.text_to_be_present_in_element_value(
                (By.XPATH, OrderPageLocators.LAST_NAME_INPUT), data["last_name"]
            )
        )

    @allure.step("Заполнение адреса")
    def fill_address(self, data):
        self.order_page.fill_address(data["address"])
        self.wait.until(
            EC.text_to_be_present_in_element_value(
                (By.XPATH, OrderPageLocators.ADDRESS_INPUT), data["address"]
            )
        )

    @allure.step("Выбор первой станции метро")
    def select_metro_station(self):
        self.order_page.click_metro_station_input()
        self.order_page.select_first_metro_station()
        self.wait.until(
            EC.text_to_be_present_in_element_value(
                (By.XPATH, OrderPageLocators.METRO_STATION_INPUT),
                "Бульвар Рокоссовского",
            )
        )

    @allure.step("Заполнение телефона")
    def fill_phone(self, data):
        self.order_page.fill_phone(data["phone"])
        self.wait.until(
            EC.text_to_be_present_in_element_value(
                (By.XPATH, OrderPageLocators.PHONE_INPUT), data["phone"]
            )
        )

    @allure.step("Клик на кнопку 'Далее'")
    def click_next_button(self):
        self.order_page.click_next_button()
        self.wait.until(
            EC.visibility_of_element_located(
                (By.XPATH, OrderPageLocators.RENT_DATE_INPUT)
            )
        )

    @allure.step("Заполнение даты аренды")
    def fill_rent_date(self, data):
        self.order_page.fill_rent_date(data["rent_date"])
        self.wait.until(
            EC.presence_of_element_located(
                (By.XPATH, OrderPageLocators.RENT_DATE_INPUT)
            )
        )

    @allure.step("Выбор срока аренды")
    def select_rent_duration(self):
        self.order_page.click_rent_period_dropdown()
        self.order_page.select_rent_duration()

    @allure.step("Выбор цвета самоката")
    def select_scooter_color(self, color):
        if color == "black":
            self.order_page.select_scooter_color_black()
        elif color == "grey":
            self.order_page.select_scooter_color_grey()

    @allure.step("Клик по кнопке 'Заказать'")
    def click_order_button(self):
        self.order_page.click_order_button()
        self.wait.until(
            EC.visibility_of_element_located((By.XPATH, OrderPageLocators.ORDER_MODAL))
        )

    @allure.step("Проверка открытия окна подтверждения заказа")
    def check_order_modal_opened(self):
        assert (
            self.order_page.is_order_modal_opened()
        ), "Окно подтверждения заказа не открылось"

    @allure.step("Клик по кнопке 'Да' в окне подтверждения")
    def click_order_modal_yes_button(self):
        self.order_page.click_order_modal_yes_button()

    @allure.step("Клик по кнопке 'Нет' в окне подтверждения")
    def click_order_modal_no_button(self):
        self.order_page.click_order_modal_no_button()

    @allure.step("Проверка, что появилось сообщение 'Заказ оформлен'")
    def check_order_confirmation(self):
        self.order_page.check_order_confirmation()

    @allure.step("Клик по кнопке 'Посмотреть статус' и проверка перехода на страницу заказа")
    def click_view_order_status(self):
        self.order_page.click_view_order_status()

    @allure.step("Клик по логотипу 'Самокат'")
    def click_logo_scooter(self):
        self.order_page.click_logo_scooter()
        assert self.driver.current_url == Urls.MAIN_URL, "Главная страница не открылась"

    @allure.step("Клик по логотипу 'Яндекс'")
    def click_logo_yandex(self):
        self.order_page.click_logo_yandex()
        self.wait.until(EC.url_contains("dzen.ru/?yredirect=true"))
        assert "dzen.ru/?yredirect=true" in self.driver.current_url, "Страница Дзена не открылась"

    @pytest.mark.parametrize("confirm_order", ["yes", "no"])
    @pytest.mark.parametrize("data", test_data)
    @pytest.mark.parametrize(
        "click_order_button_method",
        ["click_order_button_in_header", "click_order_button_in_main_page"],
    )
    def test_order_form(self, data, click_order_button_method, confirm_order, request):

        # Словари для сопоставления параметров с текстовыми значениями для названия теста в Allure
        click_order_button_method_mapping = {
            "click_order_button_in_header": 'через кнопку "Заказать" в шапке сайта',
            "click_order_button_in_main_page": 'через кнопку "Заказать" на главной странице',
        }

        confirm_order_mapping = {
            "yes": "с оформлением заказа",
            "no": "с отменой заказа",
        }

        # Получаем текстовые значения параметров
        click_order_button_method_text = click_order_button_method_mapping.get(click_order_button_method,
                                                                               click_order_button_method)
        confirm_order_text = confirm_order_mapping.get(confirm_order, confirm_order)

        # Получаем название браузера из параметра driver
        browser_name = request.node.callspec.params.get("driver", "unknown")

        # Динамически формируем заголовок
        test_title = (
            f"Проверка заполнения формы заказа {click_order_button_method_text} "
            f"{confirm_order_text} в браузере {browser_name}"
        )
        allure.dynamic.title(test_title)

        click_order_button_func = getattr(self, click_order_button_method)
        click_order_button_func()
        self.fill_first_name(data)
        self.fill_last_name(data)
        self.fill_address(data)
        self.fill_phone(data)
        self.select_metro_station()
        self.click_next_button()
        self.fill_rent_date(data)
        self.select_rent_duration()
        self.select_scooter_color(data["scooter_color"])
        self.click_order_button()
        self.check_order_modal_opened()

        if confirm_order == "yes":
            self.click_order_modal_yes_button()
            self.check_order_confirmation()
            self.click_view_order_status()
        else:
            self.click_order_modal_no_button()

        self.click_logo_scooter()
        self.click_logo_yandex()