from selenium import webdriver
import unittest
from Src.pageHelper.TruckTraderHelper import MyTraderLogin
from Src.reportrunner.HTMLTestRunner import HTMLTestRunner
from Src.reportrunner import HTMLTestRunner
from Src.utils import DriverFramework

class MyTraderLoginPage(DriverFramework.DriverFramework):    
    
    def setUp(self):
        super(MyTraderLoginPage, self).setup()
    
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
    
    def tearDown(self):
        #self.driver.quit()
        super(MyTraderLoginPage, self).tearDown()
 
#if __name__ == 'Src.tests.trucktrader.MyTraderLoginPage': 
    #outfile = open("C:/Users/admin/eclipse-workspace/TraderInteractive/Reports/mylogin.html", "w")
    #runner = HTMLTestRunner.HTMLTestRunner(outfile)
    #mylogin = MyTraderLoginPage('test_TraderLogin')
    #runner.run(mylogin)