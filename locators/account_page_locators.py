from selenium.webdriver.common.by import By


class AccountPageLocators:
    # Кнопка "Личный кабинет" на главной странице
    ACCOUNT_BUTTON = (By.XPATH, "//a[@href='/account']")

    # Поля ввода на странице входа
    EMAIL_INPUT = (By.XPATH, "//input[@name='name']")
    PASSWORD_INPUT = (By.XPATH, "//input[@name='Пароль']")
    LOGIN_BUTTON = (By.XPATH, "//button[contains(text(),'Войти')]")

    # Элементы в личном кабинете
    PROFILE_BUTTON = (By.XPATH, "//a[contains(text(),'Профиль')]")
    ORDER_HISTORY_BUTTON = (By.XPATH, "//a[contains(text(),'История заказов')]")
    LOGOUT_BUTTON = (By.XPATH, "//button[contains(text(),'Выход')]")

    # Завершенные заказы
    ORDER_COMPLETED = (By.XPATH, "//li[contains(@class, 'OrderHistory_card')]")

    # Информация о профиле
    PROFILE_NAME_INPUT = (By.XPATH, "//input[@name='name']")
    PROFILE_EMAIL_INPUT = (By.XPATH, "//input[@name='email']")
    SAVE_BUTTON = (By.XPATH, "//button[contains(text(),'Сохранить')]")