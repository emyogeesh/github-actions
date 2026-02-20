import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

BASE_URL = "http://localhost:8080"

@pytest.mark.sanity
class TestDevOpsHomepage:

    def get_driver(self):
        options = Options()
        options.add_argument("--headless=new")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        driver = webdriver.Chrome(options=options)
        driver.maximize_window()
        return driver

    def test_homepage_load_and_texts(self):
        driver = self.get_driver()
        driver.get(BASE_URL)

        assert driver.title == "DevOps Journey"
        assert driver.find_element(By.TAG_NAME, "h2").text == "My DevOps Docker Application"
        assert "Hello from DevOps Journey" in driver.find_element(By.TAG_NAME, "h1").text
        assert driver.find_element(By.CLASS_NAME, "section-title").text == "Core DevOps Concepts"

        driver.quit()

    def test_explore_button_alert(self):
        driver = self.get_driver()
        driver.get(BASE_URL)

        driver.find_element(By.TAG_NAME, "button").click()

        alert = WebDriverWait(driver, 5).until(EC.alert_is_present())
        assert alert.text == "Continuous Integration and Deployment Active"
        alert.accept()

        driver.quit()