from selenium import webdriver
import unittest
from Src.pageHelper.TruckTraderHelper import HomeResponsive_Page
from Src.reportrunner import HTMLTestRunner
from Src.utils import DriverFramework

class HomePage(DriverFramework.DriverFramework):
      
    #@classmethod
    def setUp(self):
        super(HomePage, self).setup()
        
    # Open Application   
    def test_HomePage(self):      
        helper = HomeResponsive_Page.HomeResponsive_Page(self.driver)
        
        helper.openUrl()
        
        #Click on search button      
        helper.clickOnSearchButton()
        
        #Expand the seller type      
        helper.clickOnSellerType()
        
        #Click on Private Seller
        helper.clickOnPrivateSeller()
        
        privatevalue = helper.getprivatepartydetails()
        print(privatevalue)
        
        #Click on Private Party
        helper.clickOnPrivateParty()
        
        privatevalue1 = helper.getprivatepartydetailsafterclick()
        print(privatevalue1)
         
        #helper.comparestring(privatevalue, privatevalue1)
               
        #Click BackToHome      
        helper.clickOnBackToHome()
        
        #Click on search button      
        helper.clickOnSearchButton()
        
        #Expand the seller type      
        helper.clickOnSellerType()
        
        #Expand the Non Private seller      
        helper.clickOnNonPrivateSeller()
        
        privatevalue2 = helper.getnonprivatepartydetails()
        print(privatevalue2)
        
        #Click on Non Private Party
        helper.clickOnNonPrivateParty()
        
        privatevalue3 = helper.getnonprivatepartydetailsafterclick()
        print(privatevalue3)
        
        #Click BackToHome      
        helper.clickOnBackToHome()
        
        #print(privatevalue, privatevalue1, privatevalue2, privatevalue3 )
        
    #@classmethod
    def tearDown(self):
        super(HomePage, self).tearDown()
        
#if __name__ == 'Src.tests.trucktrader.HomePage': 
    #print(2)
    #HomePage = unittest.TestLoader().loadTestsFromTestCase(HomePage)
    #homepage_regression = unittest.TestSuite([HomePage])
    #outfile = open(r"..\\..\\..\\Reports\homepage1.html", "w")
    #runner = HTMLTestRunner.HTMLTestRunner(outfile)
    #runner.run(homepage_regression)
    