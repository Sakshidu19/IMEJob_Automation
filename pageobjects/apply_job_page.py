from selenium.webdriver.common.by import By

from utilities.base_class import BaseClass


class ApplyJobPage(BaseClass):

    def __init__(self, driver):
        self.driver = driver

    first_name_locator = (By.XPATH, "//input[@id='firstName']")
    last_name_locator = (By.XPATH, "//input[@id='lastName']")
    email_locator = (By.XPATH, "//input[@id='companyEmail']")
    phone_number_prefix_locator = (By.XPATH, "//select[@id='companyMobilePrefix']")
    phone_number_locator = (By.XPATH, "//input[@id='companyMobile']")
    experience_locator = (By.XPATH, "//input[@id='totalExperience']")
    #validate_experience = (By.XPATH, "//input[@id='totalExperience']")
    notice_period_locator = (By.XPATH, "//input[@id='noticePeriod']")
    validate_notice_period = (By.XPATH, "//input[@id='noticePeriod']")
    expected_CTC_locator = (By.XPATH, "//input[@id='expectedCTC']")
    validate_CTC = (By.XPATH, "//input[@id='expectedCTC']")
    location_locator = (By.XPATH, "//input[@id='tagLocation']")
    validate_job_location = (By.XPATH, "//input[@id='tagLocation']")
    technical_skill_locator = (By.XPATH, "//div[@class=' css-tlfecz-indicatorContainer']")
    technical_list_locator = (By.XPATH, "//div[@class=' css-26l3qy-menu']")
    next_btn_locator = (By.CSS_SELECTOR, 'button[type="submit"].ime-btn.ime-btn-primary-soft')
    validate_next_btn = (By.XPATH, "(//div[@class='card-body']/h3)[2]")


    def get_first_name(self):
        self.driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
        self.wait_for_visibiltiy(self.first_name_locator)
        return self.driver.find_element(*self.first_name_locator)


    def get_last_name(self):
        self.wait_for_visibiltiy(self.last_name_locator)
        return self.driver.find_element(*self.last_name_locator)


    def get_email(self):
        self.wait_for_visibiltiy(self.email_locator)
        return self.driver.find_element(*self.email_locator)


    def get_phone_prefix(self, prefix):
        self.wait_for_visibiltiy(self.phone_number_prefix_locator)
        phone = self.driver.find_element(*self.phone_number_prefix_locator)
        self.get_select_option_by_visible_text(phone, prefix)


    def get_phone_number(self):
        self.wait_for_visibiltiy(self.phone_number_locator)
        return self.driver.find_element(*self.phone_number_locator)


    def get_experience(self):
        self.wait_for_visibiltiy(self.experience_locator)
        return self.driver.find_element(*self.experience_locator)


    def get_validate_experience(self):
        self.wait_for_visibiltiy(self.experience_locator)
        return self.driver.find_element(*self.experience_locator)


    def get_notice_period(self):
        self.wait_for_visibiltiy(self.notice_period_locator)
        return self.driver.find_element(*self.notice_period_locator)


    def get_validate_notice_period(self):
        self.wait_for_visibiltiy(self.validate_notice_period)
        return self.driver.find_element(*self.validate_notice_period)


    def get_expected_CTC(self):
        self.wait_for_visibiltiy(self.expected_CTC_locator)
        return self.driver.find_element(*self.expected_CTC_locator)


    def get_validate_CTC(self):
        self.wait_for_visibiltiy(self.validate_CTC)
        return self.driver.find_element(*self.validate_CTC)


    def get_location_apply_page(self):
        self.wait_for_visibiltiy(self.location_locator)
        return self.driver.find_element(*self.location_locator)


    def get_validate_job_lcation(self):
        self.wait_for_visibiltiy(self.validate_job_location)
        return self.driver.find_element(*self.validate_job_location)


    def get_skill_apply_job(self):
        self.wait_for_visibiltiy(self.technical_skill_locator)
        return self.driver.find_element(*self.technical_skill_locator)


    def get_skill_job(self, skillsname):
        #self.wait_for_visibiltiy(self.technical_list_locator)
        job_technical = self.driver.find_element(*self.technical_list_locator)
        print(job_technical.get_attribute('innerHTML'))
        skill_Xpath = f"//div[.='{skillsname}']"
        selected_skill = job_technical.find_element(By.XPATH, skill_Xpath)
        return selected_skill


    def get_next_btn(self):
        #self.driver.execute_script("arguments[0].scrollIntoView();", self.next_btn_locator)
        self.wait_for_visibiltiy(self.next_btn_locator)
        return self.driver.find_element(*self.next_btn_locator)


    def get_validate_next_btn(self):
        self.wait_for_visibiltiy(self.validate_next_btn)
        return self.driver.find_element(*self.validate_next_btn)


