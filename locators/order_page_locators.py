class OrderPageLocators:

    # Локаторы для первой формы
    ORDER_FORM = '//div[contains(@class, "Order_Content")]'
    FIRST_NAME_INPUT = '//input[@placeholder="* Имя"]'
    LAST_NAME_INPUT = '//input[@placeholder="* Фамилия"]'
    ADDRESS_INPUT = '//input[@placeholder="* Адрес: куда привезти заказ"]'
    METRO_STATION_INPUT = '//input[@placeholder="* Станция метро"]'
    FIRST_METRO_OPTION = '//div[@class="select-search__select"]//ul/li[1]'
    PHONE_INPUT = '//input[@placeholder="* Телефон: на него позвонит курьер"]'
    NEXT_BUTTON = '//button[text()="Далее"]'

    # Локаторы для второй формы
    ORDER_CONTENT_HEADER = '//div[contains(@class, "Order_Header")]'
    RENT_DATE_INPUT = '//input[@placeholder="* Когда привезти самокат"]'
    RENT_PERIOD_DROPDOWN = '//div[contains(@class, "Dropdown-placeholder") and text()="* Срок аренды"]'
    RENT_PERIOD_OPTION = '//div[contains(@class, "Dropdown-option") and text()="сутки"]'
    SCOOTER_COLOR_BLACK = '//label[@for="black"]'
    SCOOTER_COLOR_GREY = '//label[@for="grey"]'
    COMMENT_INPUT = '//input[@placeholder="Комментарий для курьера"]'
    ORDER_BUTTON = '//div[contains(@class, "Order_Buttons")]/button[text()="Заказать"]'
    ORDER_CONFIRM_BUTTON = '//button[text()="Да"]'
    ORDER_OVERLAY = '//div[contains(@class, "Order_Overlay")]'
    ORDER_MODAL = '//div[contains(@class, "Order_Modal")]'
    ORDER_MODAL_YES_BUTTON = "//button[contains(text(), 'Да')]"
    ORDER_MODAL_NO_BUTTON = '//button[text()="Нет"]'

    # Локатор для логотипа
    LOGO_SCOOTER = '//a[contains(@class, "Header_LogoScooter")]'
    LOGO_YANDEX = '//a[contains(@class, "Header_LogoYandex")]'

    # Локатор для клика в произвольное место
    PAGE_BODY = '//body'
