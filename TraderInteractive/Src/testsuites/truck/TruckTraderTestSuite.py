import unittest
from Src.reportrunner import HTMLTestRunner
import os

from Src.tests.trucktrader.MyTraderLoginPage import MyTraderLoginPage
from Src.tests.trucktrader.HomePage import HomePage
from Src.tests.trucktrader.TruckSearchPage import TruckSearchPage
from Src.tests.trucktrader.TruckTraderDealerSearch import TruckTraderDealerSearch
from Src.tests.trucktrader.TruckTraderKeywordSearch import TruckTraderKeywordSearch
from Src.tests.trucktrader.TruckTraderResetRefineSearch import TruckTraderResetRefineSearch


result_dir = os.getcwd()

MyTraderLoginPage = unittest.TestLoader().loadTestsFromTestCase(MyTraderLoginPage)
HomePage = unittest.TestLoader().loadTestsFromTestCase(HomePage)
TruckSearchPage = unittest.TestLoader().loadTestsFromTestCase(TruckSearchPage)
TruckTraderDealerSearch = unittest.TestLoader().loadTestsFromTestCase(TruckTraderDealerSearch)
TruckTraderKeywordSearch = unittest.TestLoader().loadTestsFromTestCase(TruckTraderKeywordSearch)
TruckTraderResetRefineSearch = unittest.TestLoader().loadTestsFromTestCase(TruckTraderResetRefineSearch)

#regression_tests = unittest.TestSuite([MyTraderLoginPage,HomePage,TruckSearchPage,TruckTraderDealerSearch,TruckTraderKeywordSearch, TruckTraderResetRefineSearch, TruckSearchResult])
regression_tests = unittest.TestSuite([MyTraderLoginPage, HomePage,TruckSearchPage,TruckTraderDealerSearch,TruckTraderKeywordSearch,TruckTraderResetRefineSearch])
#regression_tests = unittest.TestSuite([HomePage])

# open the report file
outfile = open(r"..\\..\\..\\Reports\TruckTraderRegressionTestReport.html", "w")
# configure HTMLTestRunner options
runner = HTMLTestRunner.HTMLTestRunner(outfile,
                        title='Trader Interactive Automated Tests',
                        description='Regression Tests')
# run the suite using HTMLTestRunner
runner.run(regression_tests)