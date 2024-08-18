from selenium.webdriver.common.by import By


class StellaLocators:
    ENTER_ACCOUNT_BUTTON = (By.XPATH, "//button[text() = 'Войти в аккаунт']")  # кнопка "Войти в аккаунт"
    REGISTER_LINK = (By.XPATH, "//a[text() = 'Зарегистрироваться']")  # ссылка для регистрации

    NAME_REG_INPUT = (By.XPATH, "//input[@name = 'name']") # Имя при регистрации
    EMAIL_REG_INPUT = (By.XPATH, ".//label[text() = 'Email']/parent::*/input") # Email при регистрации
    PASSWORD_REG_INPUT = (By.XPATH, "//input[@name = 'Пароль']") # Пароль при регистрации
    BUTTON_REG = (By.XPATH, "//button[text() = 'Зарегистрироваться']") # кнопка регистрации
    ERROR_MESSAGE = (By.XPATH, "//p[text() = 'Некорректный пароль']") # сообщение о некорректном пароле


    LOGIN_INPUT = (By.XPATH, "//input[@name = 'name']") # Логин при авторизации
    PASSWORD_INPUT = (By.XPATH, "//input[@name = 'Пароль']") # Пароль при авторизации
    LOGIN_SUBMINT_BUTTON = (By.XPATH, "//button[text() = 'Войти']") # Кнопка "Войти"
    LINK_REGISTER = (By.XPATH, "//a[text() = 'Зарегистрироваться']") # Ссылка "Зарегистрироваться"
    LINK_ENTER = (By.XPATH, "//a[text() = 'Войти']") # Ссылка "Войти"
    LINK_RECOVER_PASSWORD = (By.XPATH, "//a[text() = 'Восстановить пароль']") # Ссылка "Восстановить пароль"
    LINK_PERSONAL_ACCOUNT = (By.XPATH, "//p[text() = 'Личный Кабинет']") # Ссылка "Личный кабинет"

    LINK_CONSTRUCTOR = (By.XPATH, "//p[text() = 'Конструктор']") # Ссылка "Конструктор"

    LOGO = (By.XPATH, "//div[@class = 'AppHeader_header__logo__2D0X2']") # Логотип
  #  LOGO = (By.XPATH, ".//div[contains(@class,'AppHeader_header')")  # Логотип

    EXIT_BUTTON = (By.XPATH, "//button[text() = 'Выход']") # Кнопка "Выход"

    SAUCE_ON_MENU = (By.XPATH, "//span[text() ='Соусы']") # Ссылка на соусы в меню
    SAUCE = (By.XPATH, "//p[text() ='Соус Spicy-X']") # первый элемент соуса
    BUN_ON_MENU = (By.XPATH, "//span[text() = 'Булки']") # Ссылка на булки в меню
    BUN = ((By.XPATH, "//p[text() ='Флюоресцентная булка R2-D3']")) # первый элемент булок
    FILLINGS_ON_MENU = (By.XPATH, "//span[text() ='Начинки']") # Начинки в меню
    FILLINGS = ((By.XPATH, "//p[text() ='Мясо бессмертных моллюсков Protostomia']"))