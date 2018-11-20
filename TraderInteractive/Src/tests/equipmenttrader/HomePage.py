from selenium import webdriver
import unittest
from Src.pageHelper.EquipmentTraderHelper import HomeResponsive_Page
from Src.reportrunner import HTMLTestRunner
from Src.utils import DriverFramework

class HomePage(DriverFramework.DriverFramework):
    
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
        helper.clickOnEquipPrivateParty()
        
        privatevalue1 = helper.getprivatepartydetailsafterclick()
        print(privatevalue1)
         
        
        #helper.comparestring(privatevalue, privatevalue1)
        
        #Click on Start Over button
        #helper.clickOnRefineSearch()
        
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
        helper.clickOnEquipNonPrivateParty()
        
        privatevalue3 = helper.getnonprivatepartydetailsafterclick()
        print(privatevalue3)
        
        #Click BackToHome      
        helper.clickOnBackToHome()
               
    def tearDown(self):
        super(HomePage, self).tearDown()
        
#if __name__ == 'Src.tests.equipmenttrader.HomePage': 
    #outfile = open("C:/Users/admin/eclipse-workspace/TraderInteractive/Reports/homepage.html", "w")
    #runner = HTMLTestRunner.HTMLTestRunner(outfile)
    #hp = HomePage('test_HomePage')
    #runner.run(hp)