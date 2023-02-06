from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import pytest
from selenium.webdriver.chrome.options import Options



@pytest.fixture(autouse=True)
def get_driver(request):
    options = Options()
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_argument("--user-agent=Automation QA (Windows NT 6.1; rv:106.0) Gecko/20100101 Firefox/106.0")
    options.page_load_strategy = "normal"
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    request.cls.driver = driver
    yield
    driver.delete_all_cookies()
    driver.quit()

