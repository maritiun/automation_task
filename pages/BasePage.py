from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure
from allure_commons.types import AttachmentType

class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10, poll_frequency=1)

    def enter_text_in(self, locator, text, check_value=False):
        self.wait.until(EC.element_to_be_clickable(locator))
        self.driver.find_element(*locator).send_keys(text)
        if check_value is True:
            assert self.driver.find_element(*locator).get_attribute("value") == text, "Ошибка"

    def click_on(self, locator):
        self.wait.until(EC.element_to_be_clickable(locator))
        self.driver.find_element(*locator).click()

    def check_element(self, locator):
        self.wait.until(EC.visibility_of_element_located(locator))

    def make_screenshot(self, text):
        allure.attach(
            body=self.driver.get_screenshot_as_png(),
            name=f"{text}",
            attachment_type=AttachmentType.PNG
        )
