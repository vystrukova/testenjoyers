from selenium.webdriver.common.by import By


class BasePageLocators:
    PIKABU_LOGO_HOME = (By.XPATH, "//div[@class='header__item header__logo']")
    SPINNER = (By.CSS_SELECTOR, "spinner-border")


class LoginPageLocators(BasePageLocators):
    PIKABU_LOGIN_PAGE_BUTTON = (By.XPATH, "//span[@class='header-right-menu__login-button']")

    '''Форма открывается по кнопке PIKABU_LOGIN_PAGE_BUTTON'''

    PIKABU_FORM_LOGIN_FIELD = (By.XPATH, "(//div[@class='auth__field auth__field-input']//div[@class='input input_small']//div[@class='input__box']//input[@name='username'])[2]")
    PIKABU_FORM_PASSWORD_FIELD = (By.XPATH, "(//div[@class='auth__field auth__field-input']//div[@class='input input_small']//div[@class='input__box']//input[@name='password'])[2]")
    PIKABU_FORM_LOGIN_BUTTON = (By.XPATH, "(//button[@class='button_success button_width_100']//span[@class='button__title'])[2]")


class MainPageLocators(BasePageLocators):
    PIKABU_LOGOUT_BUTTON = (By.XPATH, "//div[@class='user__info-item user__exit']")