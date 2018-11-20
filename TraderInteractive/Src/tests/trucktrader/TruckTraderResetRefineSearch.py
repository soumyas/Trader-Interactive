from selenium import webdriver
import unittest
from Src.pageHelper.TruckTraderHelper import TruckResetRefineSearch
from Src.reportrunner import HTMLTestRunner
from Src.utils import DriverFramework

class TruckTraderResetRefineSearch(DriverFramework.DriverFramework):

    def setUp(self):
        super(TruckTraderResetRefineSearch, self).setup()
        
    # Open Application   
    def test_RefineSearch(self):
        helper = TruckResetRefineSearch.TruckResetRefineSearch(self.driver)

        helper.openUrl()
        
        #Click on search button      
        helper.clickOnSearchButton()
        
        #Click on Class at search page      
        helper.clickOnClass()
         
        #Select the Class type      
        helper.clickOnClassType()     
        
        #Click on Update button at Class popup window
        helper.clickOnUpdateButtonClass()
         
        #Click on Category at search page      
        helper.clickOnCategory()
         
        #Select the Category type      
        helper.clickOnCategoryType()     
        
        #Click on Update button at Class popup window
        helper.clickOnUpdateButtonClass()
        
        #Click on Start Over button
        helper.clickOnStartOverButton()
        
        #Go to home page
        helper.clickOnBackToHome()
        
    #@classmethod
    def tearDown(self):
        super(TruckTraderResetRefineSearch, self).tearDown()
        
#if __name__ == 'Src.tests.trucktrader.TruckTraderResetRefineSearch': 
    #outfile = open("C:/Users/admin/eclipse-workspace/TraderInteractive/Reports/RefineSearch.html", "w")
    #runner = HTMLTestRunner.HTMLTestRunner(outfile)
    #RefineSearch = TruckTraderResetRefineSearch('test_RefineSearch')
    #runner.run(RefineSearch)