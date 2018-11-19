from selenium import webdriver
import unittest
from Src.pageHelper.TruckTraderHelper import TruckResult
import os
from Src.reportrunner import HTMLTestRunner

class TruckSearchPage(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        options = webdriver.ChromeOptions()
        options.add_experimental_option("excludeSwitches", ["ignore-certificate-errors"])
        options.add_argument("--start-maximized")
        path1 = os.path.abspath("chromedriver.exe")
        driver_path = path1.replace(os.sep, '//')
        print(driver_path)
        cls.driver = webdriver.Chrome(executable_path="C:/Users/admin/eclipse-workspace/TraderInteractive/Webdriverexe/chromedriver.exe",chrome_options=options)
       
    #Open Application   
    def test_SearchResult(self):
        helper = TruckResult.TruckResult(self.driver)

        helper.openUrl()
                
        #Click on search button      
        helper.clickOnSearchButton()
        
        #Expand the Keyword section 
        helper.clickOnKeywordSection()
        
        #Click on Update keyword button at search result page 
        helper.clickOnKeywordUpdateButton()
        
        #Expand the Class at search page      
        helper.clickOnClass()
         
        #Select the Class type      
        helper.clickOnClassType1()     
        
        #Click on Update button at Class popup window
        helper.clickOnUpdateButtonClass()
         
        #Expand the Category at search page      
        helper.clickOnCategory()
         
        #Select the Category type      
        helper.clickOnCategoryType1()     
        
        #Click on Update button at Category popup window
        helper.clickOnUpdateButtonClass()
        
        #Expand the Make at search page      
        helper.clickOnMake()
         
        #Select the Make type      
        helper.clickOnMakeType()
        
        #Click on Update button at Make popup window
        helper.clickOnUpdateButtonClass()
        
        #Expand the Make at search page      
        helper.clickOnModel()
         
        #Select the Make type      
        helper.clickOnModelType()
        
        #Click on Update button at Model popup window
        helper.clickOnUpdateButtonClass()
               
        #Click on Start Over button
        helper.clickOnStartOverButton()

        #Go to home page
        helper.clickOnBackToHome()
    
    @classmethod
    def tearDown(self):
        self.driver.quit()
        
if __name__ == 'Src.tests.trucktrader.TruckSearchPage': 
    outfile = open("C:/Users/admin/eclipse-workspace/TraderInteractive/Reports/searchpage.html", "w")
    runner = HTMLTestRunner.HTMLTestRunner(outfile)
    sp = TruckSearchPage('test_SearchResult')
    runner.run(sp)