import pytest
from selenium import webdriver
from pageObjects.LoginPageObjects import LoginPage
from pageObjects.HomePageObjects import HomePage
from pageObjects.UploadPageObjects import UploadPage
import os
from utilities.readProperties import ReadConfig

class TestUpload:
    @pytest.mark.sanity
    def test_upload_file(self):
        baseURL = ReadConfig.getApplicationURL()
        user = ReadConfig.getUseremail()
        password = ReadConfig.getPassword()

        # Initialize the Chrome driver
        self.driver = webdriver.Chrome()
        self.driver.get(baseURL)
        self.driver.maximize_window()

        # Initialize the LoginPage object
        self.driver.implicitly_wait(10)
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(user)
        self.lp.setPassword(password)
        self.lp.clickLogin()
        self.hp = HomePage(self.driver)
        self.hp.clickTimesheets()
        self.up = UploadPage(self.driver)
        self.up.clickUploadFile()
        self.up.clickChooseFile()
        self.driver.close()