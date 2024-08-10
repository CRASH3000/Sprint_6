class OrderPageLocators:

    # Локаторы для первой формы
    ORDER_FORM = '//div[@class="Order_Content__bmtHS"]'
    FIRST_NAME_INPUT = '//input[@placeholder="* Имя"]'
    LAST_NAME_INPUT = '//input[@placeholder="* Фамилия"]'
    ADDRESS_INPUT = '//input[@placeholder="* Адрес: куда привезти заказ"]'
    METRO_STATION_INPUT = '//input[@placeholder="* Станция метро"]'
    FIRST_METRO_OPTION = '//div[@class="select-search__select"]//ul/li[1]'
    PHONE_INPUT = '//input[@placeholder="* Телефон: на него позвонит курьер"]'
    NEXT_BUTTON = '//button[text()="Далее"]'

    # Локаторы для второй формы
    ORDER_CONTENT_HEADER = '//div[@class="Order_Header__BZXOb"]'
    RENT_DATE_INPUT = '//input[@placeholder="* Когда привезти самокат"]'
    RENT_PERIOD_DROPDOWN = '//div[contains(@class, "Dropdown-placeholder") and text()="* Срок аренды"]'
    RENT_PERIOD_OPTION = '//div[@class="Dropdown-option" and text()="сутки"]'
    SCOOTER_COLOR_BLACK = '//label[@for="black"]'
    SCOOTER_COLOR_GREY = '//label[@for="grey"]'
    COMMENT_INPUT = '//input[@placeholder="Комментарий для курьера"]'
    ORDER_BUTTON = '//div[@class="Order_Buttons__1xGrp"]/button[text()="Заказать"]'
    ORDER_CONFIRM_BUTTON = '//button[text()="Да"]'
    ORDER_OVERLAY = '//div[@class="Order_Overlay__3KW-T"]'
    ORDER_MODAL = '//div[@class="Order_Modal__YZ-d3"]'
    ORDER_MODAL_YES_BUTTON = "//button[contains(text(), 'Да')]"
    ORDER_MODAL_NO_BUTTON = '//button[text()="Нет"]'

    # Локатор для логотипа
    LOGO_SCOOTER = '//a[@class="Header_LogoScooter__3lsAR"]'
    LOGO_YANDEX = '//a[@class="Header_LogoYandex__3TSOI"]'

    # Локатор для клика в произвольное место
    PAGE_BODY = '//body'
