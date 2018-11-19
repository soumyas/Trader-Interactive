from selenium import webdriver
import unittest
from Src.pageHelper.EquipmentTraderHelper import HomeResponsive_Page
from Src.reportrunner import HTMLTestRunner

class HomePage(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        options = webdriver.ChromeOptions()
        options.add_experimental_option("excludeSwitches", ["ignore-certificate-errors"])
        options.add_argument("--start-maximized")
        cls.driver = webdriver.Chrome(executable_path="C:/Users/admin/eclipse-workspace/TraderInteractive/Webdriverexe/chromedriver.exe",chrome_options=options)

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
               
    @classmethod
    def tearDown(self):
        self.driver.quit()
        
if __name__ == 'Src.tests.equipmenttrader.HomePage': 
    outfile = open("C:/Users/admin/eclipse-workspace/TraderInteractive/Reports/homepage.html", "w")
    runner = HTMLTestRunner.HTMLTestRunner(outfile)
    hp = HomePage('test_HomePage')
    runner.run(hp)