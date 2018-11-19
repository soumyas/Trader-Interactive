import unittest
from Src.reportrunner import HTMLTestRunner
import os
from Src.tests.equipmenttrader.HomePage import HomePage
from Src.tests.equipmenttrader.EquipmentTraderDealerSearch import EquipmentTraderDealerSearch
from Src.tests.equipmenttrader.EquipTraderKeywordSearch import EquipTraderKeywordSearch
from Src.tests.equipmenttrader.EquipmentSearchPage import EquipmentSearchPage
from Src.tests.equipmenttrader.EquipmemtTraderResetRefineSearch import EquipmemtTraderResetRefineSearch
from Src.tests.equipmenttrader.MyEquipmentLoginPage import MyEquipmentLoginPage


result_dir = os.getcwd()

HomePage = unittest.TestLoader().loadTestsFromTestCase(HomePage)
EquipmentTraderDealerSearch = unittest.TestLoader().loadTestsFromTestCase(EquipmentTraderDealerSearch)
EquipTraderKeywordSearch = unittest.TestLoader().loadTestsFromTestCase(EquipTraderKeywordSearch)
EquipmentSearchPage = unittest.TestLoader().loadTestsFromTestCase(EquipmentSearchPage)
EquipmemtTraderResetRefineSearch = unittest.TestLoader().loadTestsFromTestCase(EquipmemtTraderResetRefineSearch)
MyEquipmentLoginPage = unittest.TestLoader().loadTestsFromTestCase(MyEquipmentLoginPage)

regression_tests = unittest.TestSuite([HomePage, EquipmentTraderDealerSearch,EquipTraderKeywordSearch,EquipmentSearchPage,EquipmemtTraderResetRefineSearch,MyEquipmentLoginPage])
#regression_tests = unittest.TestSuite([HomePage])

# open the report file
outfile = open("..\\Reports\\EquipTraderRegressionTestReport.html", "w")
# configure HTMLTestRunner options
runner = HTMLTestRunner.HTMLTestRunner(outfile,
                        title='Trader Interactive Automated Tests',
                        description='Regression Tests')
# run the suite using HTMLTestRunner
runner.run(regression_tests)