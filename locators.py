from selenium.webdriver.common.by import By

class Locators:
    SAUCE_PICTURE = (By.XPATH, '//img[@alt="Соус традиционный галактический"]') #картинка из раздела Соусы, из второго ряда
    FILLING_PICTURE = (By.XPATH, '//img[@alt="Филе Люминесцентного тетраодонтимформа"]') #картинка из раздела Начинки, из второго ряда
    BULKA_PICTURE = (By.XPATH, '//img[@alt="Краторная булка N-200i"]')  #картинка из раздела Булки
    REG_NAME_FIELD = (By.XPATH, "//label[contains(text(),'Имя')]/following-sibling::input")
    REG_EMAIL_FIELD = (By.XPATH, "//label[contains(text(),'Email')]/following-sibling::input")
    REG_PASSWORD_FIELD = (By.XPATH, "//label[contains(text(),'Пароль')]/following-sibling::input")
    REG_SIGNIN_BUTTON = (By.XPATH, "//button[contains(text(),'Зарегистрироваться')]") #Кнопка "Зарегистрироваться"
    REG_FINAL_TITLE = (By.XPATH, "//h2[contains(text(),'Вход')]")
    REG_INCORRECT_PASSWORD_MESS = (By.XPATH, "//p[contains(text(),'Некорректный пароль')]")
    AUTH_ENTERACC_BUTTON = (By.XPATH, "//button[contains(text(),'Войти в аккаунт')]") #кнопка "Войти в аккаунт" справа под булочками
    AUTH_CABINET_BUTTON = (By.XPATH, "//p[contains(text(), 'Личный Кабинет')]") #кнопка "Личный кабинет" на верхней панели
    AUTH_LOGIN_BUTTON_IN_PASSWORD = (By.XPATH, "//a[contains(text(),'Войти')]") #кнопка "Войти" на странце восстановления пароля
    AUTH_LOGIN_BUTTON_IN_REGISTR = (By.XPATH, "//a[contains(text(),'Войти')]") #кнопка "войти" на странице регистрации внизу
    AUTH_LOGINBUTTON = (By.XPATH, "//button[contains(text(),'Войти')]")
    AUTH_BUTTON_CHANGED = (By.XPATH, "//button[contains(text(),'Оформить заказ')]") #кнопка "Оформить заказ" в которую превратилась кнопка "войти в аккаунт" после удачной авторизации
    CABINET_TEXT = (By.XPATH, "//p[contains(text(),'В этом разделе вы можете изменить свои персональны')]")
    BUTTON_KONSTRUKTOR = (By.XPATH, "//p[contains(text(),'Конструктор')]") #кнопка для перехода в конструктор из лК
    MAINPAGE_KONSTRUKTOR = (By.XPATH, "//h1[contains(text(),'Соберите бургер')]") #заголовок который появляется при загрузкеконструктора на главной странице
    BUTTON_LOGO = (By.XPATH, "//div[contains(@class, 'AppHeader_header__logo__2D0X2')]")  #значок Логотипа для нажатия
    BUTTON_LOGOUT = (By.XPATH, "//button[contains(text(),'Выход')]")  #кнопка Выход из Личного Кабинета
    KONSTRUKTOR_SAUCE = (By.XPATH, "//span[contains(text(),'Соусы')]") #кнопка "СОУСЫ", для перехода к разделу соусов из другого активного раздела
    KONSTRUKTOR_FILLINGS = (By.XPATH, "//span[contains(text(),'Начинки')]") #кнопка "НАЧИНКИ", для перехода к разделу начинок из другого активного раздела
    KONSTRUKTOR_BULKI = (By.XPATH, "//span[contains(text(),'Булки')]") #кнопка "БУЛКИ", для перехода к разделу булок из другого активного раздела

