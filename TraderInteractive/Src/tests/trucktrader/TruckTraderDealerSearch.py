from selenium import webdriver
import unittest
from Src.pageHelper.TruckTraderHelper import TruckDealerSearch
from Src.reportrunner import HTMLTestRunner
from Src.utils import DriverFramework

class TruckTraderDealerSearch(DriverFramework.DriverFramework):
    
    def setUp(self):
        super(TruckTraderDealerSearch, self).setup()
        
    # Open Application   
    def test_DealerSearch(self):
        helper = TruckDealerSearch.TruckDealerSearch(self.driver)

        helper.openUrl()
        
        #Expand the Dealer arrow icon at home page
        helper.clickOnDealerIcon()
        
        #Click on Search Dealer Button
        helper.clickOnSearchDealer()
              
        #Click on All Class Droplist
        helper.clickOnAllClass()
        
        #Select option under the All Class droplist
        helper.selectClassOption()
        
        #Click on All Category Droplist
        helper.clickOnAllCategory()
        
        #Select option under the All Category droplist
        helper.selectCategoryOption()
        
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
        
              
    @classmethod
    def tearDown(self):
        super(TruckTraderDealerSearch, self).tearDown()
        
#if __name__ == 'Src.tests.trucktrader.TruckTraderDealerSearch': 
    ##outfile = open("C:/Users/admin/eclipse-workspace/TraderInteractive/Reports/dealersearch.html", "w")
    #runner = HTMLTestRunner.HTMLTestRunner(outfile)
    #DealerSearch = TruckTraderDealerSearch('test_DealerSearch')
    #runner.run(DealerSearch)