from selenium import webdriver
import unittest
from Src.pageHelper.EquipmentTraderHelper import MyEquipmentLogin
from Src.reportrunner import HTMLTestRunner
from Src.utils import DriverFramework

class MyEquipmentLoginPage(DriverFramework.DriverFramework):    
    
    def setUp(self):
        super(MyEquipmentLoginPage, self).setup()
    
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
    
    def tearDown(self):
        super(MyEquipmentLoginPage, self).tearDown()
        
        
#if __name__ == 'Src.tests.equipmenttrader.MyEquipmentLoginPage': 
    #outfile = open("C:/Users/admin/eclipse-workspace/TraderInteractive/Reports/loginpage.html", "w")
    #runner = HTMLTestRunner.HTMLTestRunner(outfile)
    #lp = MyEquipmentLoginPage('test_EquipmentLogin')
    #runner.run(lp)