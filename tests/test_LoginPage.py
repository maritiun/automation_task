from pages.LoginPage import LoginPage
import allure


@allure.parent_suite("Набор тестов для примера")
class TestLoginPage:

    def setup(self):
        self.login_page = LoginPage(self.driver)
        self.driver.get(self.login_page.PAGE_URL)

    @allure.title("Проверка формы без заполнения email")
    @allure.severity("Critical")
    def test_check_form_without_email(self):
        self.login_page.click_on_receive_all_button()
        self.login_page.click_on_signin_button()
        self.login_page.click_on_next_button()
        self.login_page.check_email_message("Введите адрес электронной почты или номер телефона")

    @allure.title("Проверка формы без заполнения пароля")
    @allure.severity("Critical")
    def test_check_form_without_password(self):
        self.login_page.click_on_receive_all_button()
        self.login_page.click_on_signin_button()
        self.login_page.enter_login("mari.tiuniaeva@gmail.com")
        self.login_page.click_on_next_button()
        self.login_page.click_on_next_button()
        self.login_page.check_password_message("Введите пароль")

    @allure.title("Отправка формы с валидными данными - email и пароль")
    @allure.severity("Critical")
    def test_valid_login_with_email(self):
        self.login_page.click_on_receive_all_button()
        self.login_page.click_on_signin_button()
        self.login_page.enter_login("mari.tiuniaeva@gmail.com")
        self.login_page.click_on_next_button()
        self.login_page.enter_password("valid_password")
        self.login_page.click_on_next_button()
        self.login_page.check_in_profile_with_email("mari.tiuniaeva@gmail.com")

    @allure.title("Отправка формы с валидными данными - номер телефона и пароль")
    @allure.severity("Critical")
    def test_valid_login_with_phone_number(self):
        self.login_page.click_on_receive_all_button()
        self.login_page.click_on_signin_button()
        self.login_page.enter_login("89202982286")
        self.login_page.click_on_next_button()
        self.login_page.enter_password("valid_password")
        self.login_page.click_on_next_button()
        self.login_page.check_in_profile_with_email("mari.tiuniaeva@gmail.com")

    @allure.title("Тест на невалидный email")
    @allure.severity("Critical")
    def test_invalid_email(self):
        self.login_page.click_on_receive_all_button()
        self.login_page.click_on_signin_button()
        self.login_page.enter_login("invalid_email@gmail.com")
        self.login_page.click_on_next_button()
        self.login_page.check_email_message("Не удалось найти аккаунт")

    @allure.title("Тест на невалидный пароль")
    @allure.severity("Critical")
    def test_invalid_password(self):
        self.login_page.click_on_receive_all_button()
        self.login_page.click_on_signin_button()
        self.login_page.enter_login("mari.tiuniaeva@gmail.com")
        self.login_page.click_on_next_button()
        self.login_page.enter_password("invalid_password")
        self.login_page.click_on_next_button()
        self.login_page.check_password_message("Неверный пароль. Повторите попытку")
