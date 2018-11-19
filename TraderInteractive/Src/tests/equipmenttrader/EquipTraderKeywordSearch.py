from selenium import webdriver
import unittest
from Src.pageHelper.EquipmentTraderHelper import Equipmentkeywordsearch
from Src.reportrunner import HTMLTestRunner

class EquipTraderKeywordSearch(unittest.TestCase):
       
    @classmethod
    def setUpClass(cls):
        options = webdriver.ChromeOptions()
        options.add_experimental_option("excludeSwitches", ["ignore-certificate-errors"])
        options.add_argument("--start-maximized")
        cls.driver = webdriver.Chrome(executable_path="C:/Users/admin/eclipse-workspace/TraderInteractive/Webdriverexe/chromedriver.exe",chrome_options=options)
        
    # Open Application   
    def test_KeywordSearch(self):
        helper = Equipmentkeywordsearch.Equipmentkeywordsearch(self.driver)

        helper.openUrl()
        
        #Click on search button      
        helper.clickOnSearchButton()
        
        #Go to home page
        helper.clickOnBackToHome()        

    
    @classmethod
    def tearDown(self):
        self.driver.quit()
        
if __name__ == 'Src.tests.equipmenttrader.EquipTraderKeywordSearch': 
    outfile = open("C:/Users/admin/eclipse-workspace/TraderInteractive/Reports/keywordsearch.html", "w")
    runner = HTMLTestRunner.HTMLTestRunner(outfile)
    ks = EquipTraderKeywordSearch('test_KeywordSearch')
    runner.run(ks)