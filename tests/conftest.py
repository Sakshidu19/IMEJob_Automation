import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture(scope="class")
def setup(request):
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.get("https://imejob.com/")
    driver.implicitly_wait(10)
    driver.maximize_window()
    request.cls.driver = driver

    yield
    driver.close()
