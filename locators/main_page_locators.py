from selenium.webdriver.common.by import By


class MainPageLocators:
    # Основные элементы страницы
    CONSTRUCTOR_BUTTON = (By.XPATH, "//p[contains(text(),'Конструктор')]")
    ORDER_FEED_BUTTON = (By.XPATH, "//p[contains(text(),'Лента Заказов')]")

    ORDER_FEED_SECTION = (By.XPATH, "//h1[contains(text(), 'Лента заказов')]")
    ACCOUNT_BUTTON = (By.XPATH, "//a[@href='/account']")
    CONSTRUCTOR_TITLE = (By.XPATH, "//h1[text()='Соберите бургер']")
    # Ингредиенты
    INGREDIENT_ITEM = (By.XPATH, "//div[@class='BurgerIngredient_ingredient__1TVf6']")
    INGREDIENT_DETAILS_MODAL = (By.XPATH, "//div[@class='Modal_modal__1TykB']")
    INGREDIENT_COUNTER  = (By.XPATH, "//a[contains(@href, '61c0c5a71d1f82001bdaaa6c')]//p[contains(@class, 'counter_counter__')]")
    COUNTER = (By.XPATH, ".//ancestor::div[contains(@class, 'ingredient')]//div[contains(@class, 'counter')]")
    INGREDIENT_SECTION = (By.XPATH, "//section[contains(@class, 'ingredients')]")
    # Модальные окна
    MODAL_CLOSE_BUTTON = (By.XPATH, "//button[@class='Modal_modal__close__2F_7J']")
    CLOSE_INGREDIENT_DETAILS_BUTTON = (By.XPATH,
                                       "//section[@class='Modal_modal_opened__3ISw4 Modal_modal__P3_V5']//button[@type='button']//*[name()='svg']//*[name()='path' and contains(@fill-rule,'evenodd')]")

    COUNTER_LOCATOR = (By.XPATH, "//div[contains(@class, 'counter')]")
    ADD_BUTTON_LOCATOR = (By.XPATH, "//button[contains(@class, 'add-ingredient')]")

    #Ингредиент  краторная булка

    INGREDIENT_KRATORNAYA = (By.XPATH, "//img[@alt='Краторная булка N-200i']")

    ID_ORDER= (By.XPATH, "// h2 [@class = 'Modal_modal__title_shadow__3ikwq Modal_modal__title__2L34m text text_type_digits-large mb-8' and text() != '9999']")
    # Лента заказов
    COMPLETED_ORDERS = (By.XPATH, "//p[contains(text(),'Готовы:')]")
    COMPLETED_ORDERS_COUNTER = (By.XPATH, "//p[normalize-space()='153072']")
    ADDED_INGREDIENT = (By.XPATH, "//div[contains(@class, 'constructor-element')]")
    # Оформление заказа
    ORDER_BUTTON = (By.XPATH, "//button[contains(text(),'Оформить заказ')]")
    ORDER_NUMBER = (By.XPATH, "//p[@class='text text_type_digits-large mb-8']")
    COUNTER = (By.XPATH, "//div[contains(@class, 'counter')]")

    # Конструктор
    BUNS_SECTION = (By.XPATH, "//span[contains(text(),'Булки')]")
    SAUCES_SECTION = (By.XPATH, "//span[contains(text(),'Соусы')]")
    TOPPINGS_SECTION = (By.XPATH, "//span[contains(text(),'Начинки')]")
    BURGER_CONSTRUCTOR_SECTION = (By.XPATH, "//section[@class='BurgerIngredients_ingredients__1N8v2']")
    CONSTRUCTOR_AREA = (By.XPATH, "//div[contains(@class, 'BurgerConstructor_basket')]")
    PLACE_ORDER_BUTTON = (By.XPATH, "//button[contains(text(), 'Оформить заказ')]")
    BUN_COUNTER = (By.XPATH, "//div[contains(@class, 'IngredientItem_bun')]//p[contains(@class, 'counter')]")
    BUN_ITEM = (By.XPATH, "//div[contains(@class, 'IngredientItem_bun')][1]")

    @staticmethod
    def get_ingredient_locator(ingredient_name):
        """Возвращает локатор ингредиента по имени"""
        return (
        By.XPATH, f"//*[contains(text(), '{ingredient_name}')]/ancestor::div[contains(@class, 'Ingredient_card')]")
