from selenium import webdriver
import unittest
from Src.pageHelper.EquipmentTraderHelper import EquipmentResetRefineSearch
from Src.reportrunner import HTMLTestRunner

   
class EquipmemtTraderResetRefineSearch(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        options = webdriver.ChromeOptions()
        options.add_experimental_option("excludeSwitches", ["ignore-certificate-errors"])
        options.add_argument("--start-maximized")
        cls.driver = webdriver.Chrome(executable_path="C:/Users/admin/eclipse-workspace/TraderInteractive/Webdriverexe/chromedriver.exe",chrome_options=options)

    def setUp(self):
        super(EquipmemtTraderResetRefineSearch,self).setUp()
        
    # Open Application   
    def test_EquipRefineSearch(self):
        helper = EquipmentResetRefineSearch.EquipmentResetRefineSearch(self.driver)

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
        
    @classmethod
    def tearDown(self):
        self.driver.quit()

if __name__ == 'Src.tests.equipmenttrader.EquipmemtTraderResetRefineSearch': 
    outfile = open("C:/Users/admin/eclipse-workspace/TraderInteractive/Reports/refinesearch.html", "w")
    runner = HTMLTestRunner.HTMLTestRunner(outfile)
    rs = EquipmemtTraderResetRefineSearch('test_EquipRefineSearch')
    runner.run(rs)