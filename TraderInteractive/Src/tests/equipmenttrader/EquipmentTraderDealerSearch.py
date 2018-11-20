from selenium import webdriver
import unittest
from Src.pageHelper.EquipmentTraderHelper import EquipmentDealerSearch
from Src.reportrunner import HTMLTestRunner
from Src.utils import DriverFramework

class EquipmentTraderDealerSearch(DriverFramework.DriverFramework):
    
     def setUp(self):
        super(EquipmentTraderDealerSearch, self).setup()
        
     #Open Application   
     def test_EquipDealerSearch(self):
        helper = EquipmentDealerSearch.EquipmentDealerSearch(self.driver)

        helper.openUrl()
                    
        #Expand the Dealer arrow icon at home page
        helper.clickOnDealerIcon()
        
        #Click on Search Dealer Button
        helper.clickOnSearchDealer()
              
        #Click on All Class Droplist
        helper.clickOnAllClass()
        
        #Select option under the All Class droplist
        helper.selectClassOption()
                       
        #Click on All Make Droplist
        helper.clickOnAllMake()
        
        #Select option under the All Make droplist
        helper.selectMakeOption()
        
        #Click on Dealer search button
        helper.clickOnDealerSearchButton()
              
        #Click on Dealer search result button
        helper.clickOnDealerResultButton()
        
        #Expand the Dealer Class option
        helper.clickOnDealerClass()
        
        #Select multiple Dealer class type1
        helper.clickOnDealerClass1()
        
        #Select multiple Dealer class type2
        helper.clickOnDealerClass2()
        
        #Select multiple Dealer class type3
        helper.clickOnDealerClass3()
        
        #Click on Update button at Class popup window
        helper.clickOnDealerClassUpdateButton()
        
        #Click BackToHome      
        helper.clickOnBackToHome()
        
     def tearDown(self):
        super(EquipmentTraderDealerSearch, self).tearDown()
       
        
#if __name__ == 'Src.tests.equipmenttrader.EquipmentTraderDealerSearch': 
    #outfile = open("C:/Users/admin/eclipse-workspace/TraderInteractive/Reports/dealersearch.html", "w")
    #runner = HTMLTestRunner.HTMLTestRunner(outfile)
    #ds = EquipmentTraderDealerSearch('test_EquipDealerSearch')
    #runner.run(ds)