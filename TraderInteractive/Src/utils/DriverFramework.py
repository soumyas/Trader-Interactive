from selenium import webdriver
import unittest
import os
from Src.utils import ReaderFile
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import time
from Src.utils import ReaderFile
from selenium.webdriver.common.by import By
import configparser

class DriverFramework(unittest.TestCase):
    
    capabilities = None
    
    def setup(self):
        
        reader = ReaderFile.ReadXML()
        runMode=reader.readInI('test', "RunMode")
        browser=reader.readInI('test', "Browser")
        parent_driver_dir = os.getcwd()
        #parent_driver_dir = os.path.dirname(driver_dir)
        print(parent_driver_dir)
        print (browser)
        if(runMode=='Windows'):            
            if (browser=='IE'):
                self.driver = webdriver.Ie("..\\Webdriverexe\\IEDriverServer.exe")
                self.driver.maximize_window()
            if (browser=='Chrome'):
                #self.driver = webdriver.Chrome("..\\Webdriverexe\\chromedriver.exe")
                options = webdriver.ChromeOptions()
                options.add_experimental_option("excludeSwitches", ["ignore-certificate-errors"])
                options.add_argument("--start-maximized")
                if "trucktrader" not in parent_driver_dir:
                    parent_driver_dir = parent_driver_dir.replace(r'Src\tests\equipmenttrader', 'Webdriverexe\chromedriver.exe')
                else:
                    parent_driver_dir = parent_driver_dir.replace(r'suite', 'Webdriverexe\chromedriver.exe')
                #parent_driver_dir = parent_driver_dir.replace(r'Src\tests\equipmenttrader', 'Webdriverexe\chromedriver.exe')
                #print(parent_driver_dir)
                parent_driver_dir = parent_driver_dir.replace(os.sep, '/')
                #print(parent_driver_dir)
                self.driver = webdriver.Chrome(executable_path=parent_driver_dir, chrome_options=options)
                #self.driver = webdriver.Chrome(executable_path="..\\Webdriverexe\\chromedriver.exe",chrome_options=options)

                             
            if (browser=='Firefox'):  
                self.driver = webdriver.Firefox()
                self.driver.maximize_window()

        if(runMode=='Linux'):            
            if (browser=='IE'):
                self.driver = webdriver.Ie("..\\Webdriverexe\\IEDriverServer.exe")
                self.driver.maximize_window()
                
            if (browser=='Chrome'):
                options = webdriver.ChromeOptions()
                options.add_experimental_option("excludeSwitches", ["ignore-certificate-errors"])
                options.add_argument("--start-maximized")
                self.driver = webdriver.Chrome(executable_path="..\\Webdriverexe\\chromedriver.exe",chrome_options=options)
                
            if (browser=='Firefox'):  
                self.driver = webdriver.Firefox()
                self.driver.maximize_window()
                
        if(runMode=='MAC'):            
            if (browser=='IE'):
                self.driver = webdriver.Ie("..\\Webdriverexe\\IEDriverServer.exe")
                
            if (browser=='Chrome'):
                options = webdriver.ChromeOptions()
                options.add_experimental_option("excludeSwitches", ["ignore-certificate-errors"])
                options.add_argument("--start-maximized")
                self.driver = webdriver.Chrome(executable_path="..\\Webdriverexe\\chromedriver.exe",chrome_options=options)
                
            if (browser=='Firefox'):  
                self.driver = webdriver.Firefox()
                self.driver.maximize_window()
        

              
    def tearDown(self):
        self.driver.quit()
        #DriverFramework.DriverFramework.tearDown(self)
