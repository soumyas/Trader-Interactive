from selenium import webdriver
import unittest
from Src.pageHelper.TruckTraderHelper import MyTraderLogin
from Src.reportrunner.HTMLTestRunner import HTMLTestRunner
from Src.reportrunner import HTMLTestRunner

class MyTraderLoginPage(unittest.TestCase):    
    
    @classmethod
    def setUpClass(cls):
        options = webdriver.ChromeOptions()
        options.add_experimental_option("excludeSwitches", ["ignore-certificate-errors"])
        options.add_argument("--start-maximized")
        cls.driver = webdriver.Chrome(executable_path="C:/Users/admin/eclipse-workspace/TraderInteractive/Webdriverexe/chromedriver.exe",chrome_options=options)
        #driverhelper.driverhelper.initializedriver(cls)
    
    def test_TraderLogin(self):
        helper = MyTraderLogin.MyTraderLogin(self.driver)
        print(__name__)
        #open url
        helper.openUrl()
        
        #Click on LogIn button      
        helper.clickOnLogInButton()
        
        #Enter the login credential
        helper.enterUserDetails()
       
        #Click on SignIn Butto+n at MyT page   
        helper.clickOnSignInButton()
        
        #Click on Hamburger Icon
        helper.clickOnHamburgerIcon()
        
        #Click on Sign Out MyTrader  
        helper.clickOnSignOutMyTrader()
    
    @classmethod
    def tearDown(self):
        self.driver.quit()
        #Src.MyTraderLoginPage
 
if __name__ == 'Src.tests.trucktrader.MyTraderLoginPage': 
    outfile = open("C:/Users/admin/eclipse-workspace/TraderInteractive/Reports/mylogin.html", "w")
    runner = HTMLTestRunner.HTMLTestRunner(outfile)
    mylogin = MyTraderLoginPage('test_TraderLogin')
    runner.run(mylogin)