from selenium import webdriver
import unittest
from Src.pageHelper.EquipmentTraderHelper import EquipmentResult
from Src.reportrunner import HTMLTestRunner
from Src.utils import DriverFramework

class EquipmentSearchPage(DriverFramework.DriverFramework):

    def setUp(self):
        super(EquipmentSearchPage, self).setup()
        
    #Open Application   
    def test_SearchResult(self):
        helper = EquipmentResult.EquipmentResult(self.driver)

        helper.openUrl()
                
        #Click on search button      
        helper.clickOnSearchButton()
        
        #Expand the Keyword section 
        helper.clickOnKeywordSection()
        
        #Enter the keyword into the keyword text field.
        helper.enterDetails()
        
        #Click on Update keyword button at search result page 
        helper.clickOnKeywordUpdateButton()
        
        #Expand the Class at search page      
        helper.clickOnClass()
         
        #Select the Class type      
        helper.clickOnClassType1()     
        
        #Click on Update button at Class popup window
        helper.clickOnUpdateButton()
         
        #Expand the Category at search page      
        helper.clickOnCategory()
         
        #Select the Category type      
        helper.clickOnCategoryType1()     
        
        #Click on Update button at Category popup window
        helper.clickOnUpdateButton()
        
        #Expand the Make at search page      
        helper.clickOnMake()
         
        #Select the Make type      
        helper.clickOnMakeType()
        
        #Click on Update button at Make popup window
        helper.clickOnUpdateButton()
        
        #Expand the Make at search page      
        helper.clickOnPrice()
         
        #Select the Make type      
        helper.clickOnPriceRange()
        
        #Click on Start Over button
        helper.clickOnStartOverButton()

        #Go to home page
        helper.clickOnBackToHome()
    
    def tearDown(self):
        super(EquipmentSearchPage, self).tearDown()
        
        
#if __name__ == 'Src.tests.equipmenttrader.EquipmentSearchPage': 
    #outfile = open("C:/Users/admin/eclipse-workspace/TraderInteractive/Reports/searchpage.html", "w")
    #runner = HTMLTestRunner.HTMLTestRunner(outfile)
    #sp = EquipmentSearchPage('test_SearchResult')
    #runner.run(sp)