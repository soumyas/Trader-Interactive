from selenium import webdriver
import unittest
from Src.pageHelper.EquipmentTraderHelper import MyEquipmentLogin
from Src.reportrunner import HTMLTestRunner

class MyEquipmentLoginPage(unittest.TestCase):    
    
    @classmethod
    def setUpClass(cls):
        options = webdriver.ChromeOptions()
        options.add_experimental_option("excludeSwitches", ["ignore-certificate-errors"])
        options.add_argument("--start-maximized")
        cls.driver = webdriver.Chrome(executable_path="C:/Users/admin/eclipse-workspace/TraderInteractive/Webdriverexe/chromedriver.exe",chrome_options=options)
    
    def test_EquipmentLogin(self):
        helper = MyEquipmentLogin.MyEquipmentLogin(self.driver)
              
        #open url
        helper.openUrl()
        
        #Click on LogIn button      
        helper.clickOnLogInButton()
        
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
        
        
if __name__ == 'Src.tests.equipmenttrader.MyEquipmentLoginPage': 
    outfile = open("C:/Users/admin/eclipse-workspace/TraderInteractive/Reports/loginpage.html", "w")
    runner = HTMLTestRunner.HTMLTestRunner(outfile)
    lp = MyEquipmentLoginPage('test_EquipmentLogin')
    runner.run(lp)