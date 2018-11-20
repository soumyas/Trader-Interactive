from selenium import webdriver
import unittest
from Src.pageHelper.TruckTraderHelper import Truckkeywordsearch
from Src.reportrunner import HTMLTestRunner
from Src.utils import DriverFramework

class TruckTraderKeywordSearch(DriverFramework.DriverFramework):

    def setUp(self):
        super(TruckTraderKeywordSearch, self).setup()
        
    # Open Application   
    def test_KeywordSearch(self):
        helper = Truckkeywordsearch.Truckkeywordsearch(self.driver)

        helper.openUrl()
        
        #Click on search button      
        helper.clickOnSearchButton()
        
        #Go to home page
        helper.clickOnBackToHome()        
    
    @classmethod
    def tearDown(self):
        super(TruckTraderKeywordSearch, self).tearDown()
        
#if __name__ == 'Src.tests.trucktrader.TruckTraderKeywordSearch': 
    #outfile = open("C:/Users/admin/eclipse-workspace/TraderInteractive/Reports/KeywordSearch.html", "w")
    #runner = HTMLTestRunner.HTMLTestRunner(outfile)
    #KeywordSearch = TruckTraderKeywordSearch('test_KeywordSearch')
    #runner.run(KeywordSearch)