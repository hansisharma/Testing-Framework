from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


def start_browser():

    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install())
    )

    driver.maximize_window()

    return driver


def close_browser(driver):

    driver.quit()