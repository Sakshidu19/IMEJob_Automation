from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from utilities.base_class import BaseClass


class SearchJobPage(BaseClass):

    def __init__(self, driver):
        self.driver = driver

    validate_homepage = (By.XPATH, "//div[@class= 'search-con']/h2")
    search_skill_locator = (By.CLASS_NAME, 'css-ackcql')
    skill_list_locator = (By.ID, 'react-select-2-listbox')
    validate_skill_locator = (By.XPATH, '(//div[@class="css-1rhbuit-multiValue"]/div)[1]')
    search_location_locator= (By.XPATH, '(//select)[1]')
    salary_range_locator = (By.XPATH, '(//select)[2]')
    search_btn_locator = (By.XPATH, "//div[@class='search-area']/button")
    validate_search_btn = (By.XPATH, "//div[@class='left-panel ']/h2")





    def get_validate_homepage(self):
        self.wait_for_visibiltiy(self.validate_homepage)
        return self.driver.find_element(*self.validate_homepage)


    def get_skill_enable(self):
        self.wait_for_visibiltiy(self.search_skill_locator)
        return self.driver.find_element(*self.search_skill_locator)


    def get_skill(self, skillname):
        self.wait_for_visibiltiy(self.skill_list_locator)
        skills = self.driver.find_element(*self.skill_list_locator)
        skillxpath = f"//div[.='{skillname}']"
        select_skill = skills.find_element(By.XPATH, skillxpath)
        return select_skill


    def get_validate_skill(self,):
        self.wait_for_visibiltiy(self.validate_skill_locator)
        return self.driver.find_element(*self.validate_skill_locator)


    def get_location(self, location):
        self.wait_for_visibiltiy(self.search_location_locator)
        loc_options = self.driver.find_element(*self.search_location_locator)
        self.get_select_option_by_visible_text(loc_options,location)


    def get_validate_location(self):
        validate_loc = self.driver.find_element(*self.search_location_locator)
        return self.get_selected_option_text(validate_loc)


    def get_salary(self, salaryrange):
        self.wait_for_visibiltiy(self.salary_range_locator)
        sal_options = self.driver.find_element(*self.salary_range_locator)
        self.get_select_option_by_visible_text(sal_options, salaryrange)


    def get_validate_salary(self):
        validate_sal = self.driver.find_element(*self.salary_range_locator)
        return self.get_selected_option_text(validate_sal)

    def get_search_button(self):
        self.wait_for_visibiltiy(self.search_btn_locator)
        return self.driver.find_element(*self.search_btn_locator)


    def get_validate_search_btn(self):
        self.wait_for_visibiltiy(self.validate_search_btn)
        return self.driver.find_element(*self.validate_search_btn)