import pytest
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait


@pytest.mark.usefixtures("setup")
class BaseClass():

    def wait_for_visibiltiy(self, locator, time=5):
        wait=WebDriverWait(self.driver, time)
        wait.until(expected_conditions.visibility_of_element_located(locator))


    def wait_for_invisibility(self, locator, time=5):
        wait = WebDriverWait(self.driver, time)
        wait.until(expected_conditions.invisibility_of_element_located(locator))


    def get_select_option_by_visible_text(self, locator, value):
        loc_select = Select(locator)
        loc_select.select_by_visible_text(value)

    def get_selected_option_text(self, locator):
        loc_select = Select(locator)
        lo = loc_select.first_selected_option
        return lo.text
