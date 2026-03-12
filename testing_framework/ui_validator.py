from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def get_ui_combined_demand(driver):

    wait = WebDriverWait(driver, 15)

    # Locate the KPI value next to "Total Combined Demand"
    element = wait.until(
        EC.presence_of_element_located(
            (
                By.XPATH,
                "//span[text()='Total Combined Demand']/following::span[contains(@class,'kpi-value')][1]"
            )
        )
    )

    value_text = element.text

    # Convert "1,292,729" -> 1292729
    value = int(value_text.replace(",", "").strip())

    return value