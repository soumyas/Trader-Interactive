from selenium import webdriver
import unittest
from Src.pageHelper.EquipmentTraderHelper import Equipmentkeywordsearch
from Src.reportrunner import HTMLTestRunner
from Src.utils import DriverFramework

class EquipTraderKeywordSearch(DriverFramework.DriverFramework):
       
    def setUp(self):
        super(EquipTraderKeywordSearch, self).setup()
        
    # Open Application   
    def test_KeywordSearch(self):
        helper = Equipmentkeywordsearch.Equipmentkeywordsearch(self.driver)

        helper.openUrl()
        
        #Click on search button      
        helper.clickOnSearchButton()
        
        #Go to home page
        helper.clickOnBackToHome()        

    
    def tearDown(self):
        super(EquipTraderKeywordSearch, self).tearDown()
        
#if __name__ == 'Src.tests.equipmenttrader.EquipTraderKeywordSearch': 
    #outfile = open("C:/Users/admin/eclipse-workspace/TraderInteractive/Reports/keywordsearch.html", "w")
    #runner = HTMLTestRunner.HTMLTestRunner(outfile)
    #ks = EquipTraderKeywordSearch('test_KeywordSearch')
    #runner.run(ks)