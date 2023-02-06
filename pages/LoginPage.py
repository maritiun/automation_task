from pages.BasePage import BasePage
import allure

class LoginPage(BasePage):

    PAGE_URL = "https://google.com"

    RECEIVE_ALL_BUTTON = ("xpath", "//div[text()='Принять все']")
    SIGNIN_BUTTON = ("xpath", "//a[text()='Войти']")
    CHANGE_ACCOUNT_BUTTON = ("xpath", "//div[text()='Сменить аккаунт']")
    LOGIN_FIELD = ("xpath", "//input[@type='email']")
    NEXT_BUTTON = ("xpath", "//span[text()='Далее']")
    PASSWORD_FIELD = ("xpath", "//input[@type='password']")
    INCORECT_LOGIN_MESSAGE = ("xpath", " //div[contains(text(),'Введите адрес электронной почты или номер телефона')]")

    @allure.step("Нажать на кнопку Войти")
    def click_on_signin_button(self):
        self.click_on(self.SIGNIN_BUTTON)

    @allure.step("Нажать на кнопку Принять всё")
    def click_on_receive_all_button(self):
        self.click_on(self.RECEIVE_ALL_BUTTON)

    @allure.step("Ввести логин")
    def enter_login(self, text):
        self.enter_text_in(self.LOGIN_FIELD, text, True)
        self.make_screenshot("Ввод логина")

    @allure.step("Ввести пароль")
    def enter_password(self, text):
        self.enter_text_in(self.PASSWORD_FIELD, text, True)
        self.make_screenshot("Ввод пароля")

    @allure.step("Нажать на кнопку Далее")
    def click_on_next_button(self):
        self.click_on(self.NEXT_BUTTON)

    @allure.step("Проверяем, что зашли в аккаунт")
    def check_in_profile_with_email(self, text):
        self.check_element(("xpath", f"//a[contains(@aria-label, '{text}']"))
        self.make_screenshot("Зашли в аккаунт")

    @allure.step("Проверяем, что появилось сообщение об ошибке при введении пароля")
    def check_password_message(self, text):
        self.check_element(("xpath", f"//span[contains(text(),'{text}')]"))
        self.make_screenshot("Сообщение об ошибке при введении пароля")

    @allure.step("Проверяем, что появилось сообщение об ошибке при введении логина")
    def check_email_message(self, text):
        self.check_element(("xpath", f"//div[contains(text(),'{text}')]"))
        self.make_screenshot("Сообщение об ошибке при введении логина")

