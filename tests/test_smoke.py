import time

from pageobjects.search_job_page import SearchJobPage
from utilities.base_class import BaseClass


class TestSmoke(BaseClass):


    #Verify that the Home page should display
    def test_TC_HP_001(self):
        homepage = SearchJobPage(self.driver)
        text = homepage.get_validate_homepage().text
        assert "Find Immediate Job Openings" == text


    #Verify that selected skill should be clicked
    def test_SC_001(self):
        homepage = SearchJobPage(self.driver)
        homepage.get_skill_enable().click()
        homepage.get_skill("Java").click()
        text = homepage.get_validate_skill().text
        assert "Java" == text


    #Verify that the selected location should be clicked
    def test_LOC_001(self):
        homepage = SearchJobPage(self.driver)
        homepage.get_location("Delhi")
        text = homepage.get_validate_location()
        assert "Delhi" == text


    # Verify that the selected salary should be clicked
    def test_ASR_001(self):
        homepage = SearchJobPage(self.driver)
        homepage.get_salary("600000-1000000")
        text = homepage.get_validate_salary()
        assert "600000-1000000" == text


    #verify that the search button is clicked
    def test_SB_001c(self):
        homepage = SearchJobPage(self.driver)
        homepage.get_search_button().click()
        text = homepage.get_validate_search_btn().text
        assert "Newest Job Openings" == text