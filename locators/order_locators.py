from selenium.webdriver.common.by import By


class OrderLocators:
    # Основные элементы страницы заказов
    PLACE_AN_ORDER = (By.XPATH, "//button[contains(text(), 'Оформить заказ')]")
    ORDER_FEED_BUTTON = (By.XPATH, "//p[contains(text(),'Лента Заказов')]")
    CONSTRUCTOR_BUTTON = (By.XPATH, "//a[contains(text(), 'Конструктор')]")

    # Элементы личного кабинета
    ACCOUNT_BUTTON = (By.XPATH, "//a[@href='/account']")
    ORDER_HISTORY_BUTTON = (By.XPATH, "//a[contains(text(), 'История заказов')]")
    LOGIN_AFTER_LOGOUT_BURGER = (By.XPATH, "//h1[@class='text text_type_main-large mb-5 mt-10']")

    # Элементы ленты заказов
    LAST_ORDER = (By.XPATH, "//div[contains(@class, 'OrderHistory_card__')][1]")
    TOTAL_ORDERS_COUNTER = (By.XPATH, "//p[contains(text(), 'Выполнено за все время:')]/following-sibling::p")
    TODAY_COMPLETED_COUNTER = (
        By.XPATH,
        "//p[@class='OrderFeed_number__2MbrQ text text_type_digits-large']"
    )


    # Детали заказа
    ORDER_ID = (By.XPATH, "//h2[contains(@class, 'Modal_modal__title') and normalize-space(text())]")
    CLOSE_ORDER_DETAILS_BUTTON = (By.XPATH, "//button[contains(@class, 'Modal_modal__close')]//*[name()='svg']/ancestor::button")
    ORDER_LOADING_MODAL = (By.XPATH, "//div[contains(@class, 'Modal_modal_opened')]")
    IN_PROGRESS_SECTION = (By.XPATH, "//section[contains(@class, 'order-in-progress')]")
    ORDER_IN_PROGRESS = (By.XPATH, "//div[contains(@class, 'order-item') and contains(., '{}')]")
    ORDER_NUMBER = (By.XPATH, "//h2[contains(text(),'идентификатор заказа')]/following-sibling::p")
    BUTTON_X_MODAL = (By.XPATH, "//button [@class = 'Modal_modal__close_modified__3V5XS Modal_modal__close__TnseK']")
    FEED_TITLE = (
        By.XPATH,
        "//h1[contains(@class, 'text_type_main-large')]"
    )
    # Статус заказа
    ORDER_STATUS = (By.XPATH, "//p[contains(@class, 'status_done')]")

    # Состав заказа
    ORDER_INGREDIENTS_LIST = (By.XPATH, "//div[contains(@class, 'OrderIngredients_ingredients__')]")
    ORDER_TOTAL_PRICE = (By.XPATH, "//p[contains(@class, 'OrderIngredients_price__')]")
    ORDERS_IN_PROGRESS = Orders_in_progress = (By.XPATH, "//ul [@class = 'OrderFeed_orderListReady__1YFem OrderFeed_orderList__cBvyi']/li[text() != 'Все текущие заказы готовы!']")


