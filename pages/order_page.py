from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.order_page_locators import OrderPageLocators


class OrderPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def is_order_page_opened(self):
        return self.wait.until(
            EC.presence_of_element_located((By.XPATH, OrderPageLocators.ORDER_FORM))
        )

    def fill_first_name(self, first_name):
        first_name_input = self.driver.find_element(
            By.XPATH, OrderPageLocators.FIRST_NAME_INPUT
        )
        first_name_input.clear()
        first_name_input.send_keys(first_name)

    def fill_last_name(self, last_name):
        last_name_input = self.driver.find_element(
            By.XPATH, OrderPageLocators.LAST_NAME_INPUT
        )
        last_name_input.clear()
        last_name_input.send_keys(last_name)

    def fill_address(self, address):
        address_input = self.driver.find_element(
            By.XPATH, OrderPageLocators.ADDRESS_INPUT
        )
        address_input.clear()
        address_input.send_keys(address)

    def fill_phone(self, phone):
        phone_input = self.driver.find_element(By.XPATH, OrderPageLocators.PHONE_INPUT)
        phone_input.clear()
        phone_input.send_keys(phone)

    def click_metro_station_input(self):
        self.driver.find_element(
            By.XPATH, OrderPageLocators.METRO_STATION_INPUT
        ).click()

    def select_first_metro_station(self):
        first_metro_option = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, OrderPageLocators.FIRST_METRO_OPTION))
        )
        first_metro_option.click()

    def click_next_button(self):
        next_button = self.driver.find_element(By.XPATH, OrderPageLocators.NEXT_BUTTON)
        next_button.click()

    def is_rent_details_form_opened(self):
        return self.driver.find_element(
            By.XPATH, OrderPageLocators.RENT_DATE_INPUT
        ).is_displayed()

    def fill_rent_date(self, date):
        rent_date_input = self.driver.find_element(
            By.XPATH, OrderPageLocators.RENT_DATE_INPUT
        )
        rent_date_input.clear()
        rent_date_input.send_keys(date)

    def click_rent_period_dropdown(self):
        page_body = self.driver.find_element(By.XPATH, OrderPageLocators.PAGE_BODY)
        page_body.click()  # Клик в произвольное место экрана, чтобы убрать календарь
        rent_period_dropdown = self.wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, OrderPageLocators.RENT_PERIOD_DROPDOWN)
            )
        )
        rent_period_dropdown.click()

    def select_rent_duration(self):
        rent_duration_option = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, OrderPageLocators.RENT_PERIOD_OPTION))
        )
        rent_duration_option.click()

    def select_scooter_color(self, color):
        if color == "black":
            scooter_color_black = self.driver.find_element(
                By.XPATH, OrderPageLocators.SCOOTER_COLOR_BLACK
            )
            scooter_color_black.click()
        elif color == "grey":
            scooter_color_grey = self.driver.find_element(
                By.XPATH, OrderPageLocators.SCOOTER_COLOR_GREY
            )
            scooter_color_grey.click()

    def click_order_button(self):
        next_button = self.driver.find_element(By.XPATH, OrderPageLocators.ORDER_BUTTON)
        next_button.click()

    def is_order_modal_opened(self):
        return bool(
            self.wait.until(
                EC.visibility_of_element_located(
                    (By.XPATH, OrderPageLocators.ORDER_MODAL)
                )
            )
        )

    def click_order_modal_yes_button(self):
        yes_button = self.driver.find_element(
            By.XPATH, OrderPageLocators.ORDER_MODAL_YES_BUTTON
        )
        yes_button.click()

    def click_order_modal_no_button(self):
        no_button = self.driver.find_element(
            By.XPATH, OrderPageLocators.ORDER_MODAL_NO_BUTTON
        )
        no_button.click()

    def check_order_confirmation(self):
        confirmation_message = self.wait.until(
            EC.visibility_of_element_located(
                (By.XPATH, "//div[contains(@class, 'Order_ModalHeader__3FDaJ')]")
            )
        )
        assert "Заказ оформлен" in confirmation_message.text, "Сообщение о подтверждении заказа не найдено"

    def click_view_order_status(self):
        view_status_button = self.driver.find_element(
            By.XPATH, "//button[contains(text(), 'Посмотреть статус')]"
        )
        view_status_button.click()
        self.wait.until(EC.url_contains("/track?t="))

    def click_logo_scooter(self):
        logo_scooter = self.driver.find_element(
            By.XPATH, OrderPageLocators.LOGO_SCOOTER
        )
        logo_scooter.click()

    def click_logo_yandex(self):
        logo_yandex = self.driver.find_element(By.XPATH, OrderPageLocators.LOGO_YANDEX)
        logo_yandex.click()
        self.driver.switch_to.window(self.driver.window_handles[-1])
