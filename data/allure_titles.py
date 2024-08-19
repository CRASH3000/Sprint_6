# Логика для тестов аккордеона
def get_allure_title_for_question(question_number, browser_name):
    return f"[Вопросы о важном] Проверка на соответствие текста в ответе на вопрос {question_number}, браузер: {browser_name}"

def get_allure_description_for_question(question_number):
    return f"Клик по вопросу {question_number} и проверка ответа"


# Логика для тестов оформления заказа
click_order_button_method_mapping = {
    "click_order_button_in_header": 'через кнопку "Заказать" в шапке сайта',
    "click_order_button_in_main_page": 'через кнопку "Заказать" на главной странице',
}

confirm_order_mapping = {
    "yes": "с оформлением заказа",
    "no": "с отменой заказа",
}

def generate_test_title(click_order_button_method, confirm_order, browser_name, index):
    """
    Генерация заголовка теста на основе переданных параметров
    """
    click_order_button_method_text = click_order_button_method_mapping.get(click_order_button_method,
                                                                           click_order_button_method)
    confirm_order_text = confirm_order_mapping.get(confirm_order, confirm_order)

    test_title = (
        f"Проверка оформления заказа {click_order_button_method_text}, "
        f"{confirm_order_text}. Используя тестовые данные: {index} в браузере {browser_name}"
    )

    return test_title

def generate_test_description():
    return ("Этот тест проверяет процесс оформления заказа с различными параметрами, включая "
            "выбор кнопки заказа и подтверждение.")

