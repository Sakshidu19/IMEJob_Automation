import time

from pageobjects.apply_job_page import ApplyJobPage
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


    #Verify that the Job description page should be display
    def test_AB_001(self):
        homepage = SearchJobPage(self.driver)
        homepage_text = homepage.get_validate_Firstjob().text
        homepage.get_click_apply().click()
        time.sleep(2)
        jobpage_text = homepage.get_validate_applyjob().text
        assert jobpage_text == homepage_text


    #Verify that the First Name text field should be working
    def test_FN_001(self):
        jobpage = ApplyJobPage(self.driver)
        jobpage.get_first_name().send_keys("Sakshi")


    #Verify that the Last Name text field should be working
    def test_FN_002(self):
        jobpage = ApplyJobPage(self.driver)
        jobpage.get_last_name().send_keys("sakshi")


    #Verify that the Email text field should be working
    def test_EM_001(self):
        jobpage = ApplyJobPage(self.driver)
        jobpage.get_email().send_keys("sakshidu19@gmail.com")


    #Verify that the Phone number index should be selected
    def test_PN_001(self):
        jobpage = ApplyJobPage(self.driver)
        jobpage.get_phone_prefix("+ 91")


    #Verify that the Phone number text field should be working
    def test_PN_002(self):
        jobpage = ApplyJobPage(self.driver)
        jobpage.get_phone_number().send_keys("8178917591")


    #Verify that the Experience text field should be working
    def test_EXP_001(self):
        jobpage = ApplyJobPage(self.driver)
        jobpage.get_experience().send_keys("1")
        text = jobpage.get_validate_experience().get_attribute("value")


    #Verify that the Notice period text field should be working
    def test_NP_001(self):
        jobpage = ApplyJobPage(self.driver)
        jobpage.get_notice_period().send_keys("0")
        text = jobpage.get_validate_notice_period().get_attribute("value")
        assert "0" == text


    #Verify that the Expected CTC text field should be working
    def test_CTC_001(self):
        jobpage = ApplyJobPage(self.driver)
        jobpage.get_expected_CTC().send_keys("600000")
        text = jobpage.get_validate_CTC().get_attribute("value")
        assert "600000" == text


    #Verify that the Location text field should be working
    def test_LTF_001(self):
        jobpage = ApplyJobPage(self.driver)
        jobpage.get_location_apply_page().send_keys("Delhi")
        text = jobpage.get_validate_job_lcation().get_attribute("value")
        assert "Delhi" == text


    #Verify that the Technical skills should be selected
    def test_TS_001(self):
        jobpage = ApplyJobPage(self.driver)
        jobpage.get_skill_apply_job().click()
        jobpage.get_skill_job("Java").click()


    #Verify that the next button should be clicked
    def test_NB_001(self):
        jobpage = ApplyJobPage(self.driver)
        jobpage.get_next_btn().click()
        time.sleep(3)
        text = jobpage.get_validate_next_btn().text
        assert "Questionnaires" == text
