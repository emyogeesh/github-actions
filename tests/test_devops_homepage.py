import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

BASE_URL = "http://localhost:8080"


@pytest.fixture(scope="class")
def driver(request):
    options = Options()
    options.add_argument("--headless=new")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    drv = webdriver.Chrome(options=options)
    drv.maximize_window()

    request.cls.driver = drv
    yield drv

    drv.quit()


@pytest.mark.sanity
@pytest.mark.usefixtures("driver")
class TestDevOpsHomepage:

    def test_homepage_load_and_texts(self):
        self.driver.get(BASE_URL)

        assert self.driver.title == "DevOps Journey"
        assert self.driver.find_element(By.TAG_NAME, "h2").text == "My DevOps Docker Application"
        assert self.driver.find_element(By.CLASS_NAME, "section-title").text == "Core DevOps Concepts"

    def test_explore_button_alert(self):
        self.driver.get(BASE_URL)

        self.driver.find_element(By.TAG_NAME, "button").click()

        alert = WebDriverWait(self.driver, 5).until(EC.alert_is_present())
        assert alert.text == "Continuous Integration and Deployment Active"
        alert.accept()