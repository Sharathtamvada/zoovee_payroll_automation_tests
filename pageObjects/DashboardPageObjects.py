from selenium.webdriver.common.by import By


class DashboardPage():
    # Locators
    sdbr_timesheets_xpath = "/html/body/app-root/div/div/div/div/app-home/div/div/div/div/ngx-slick-carousel/div/div/div[2]/div/div/h2"
    sdbr_employees_xpath = "/html/body/app-root/div/div/div/div/app-home/div/div/div/div/ngx-slick-carousel/div/div/div[3]/div/div/h2"
    sdbr_programs_xpath = "/html/body/app-root/div/div/div/div/app-home/div/div/div/div/ngx-slick-carousel/div/div/div[3]/div/div/h2"
    
    # constructor
    def __init__(self,driver):
        self.driver=driver

    # action methods
    def selectTimesheets(self):
        self.driver.find_element(By.XPATH,self.sdbr_timesheets_xpath).click()

    def selectEmployees(self):
        self.driver.find_element(By.XPATH,self.sdbr_employees_xpath).click()
    
    def selectPrograms(self):
        self.driver.find_element(By.XPATH,self.sdbr_programs_xpath).click()