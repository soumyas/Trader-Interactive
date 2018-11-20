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
        
        if(runMode=='Windows'):            
            if (browser=='IE'):
                self.driver = webdriver.Ie("..\\Webdriverexe\\IEDriverServer.exe")
                self.driver.maximize_window()
            if (browser=='Chrome'):
                options = webdriver.ChromeOptions()
                options.add_experimental_option("excludeSwitches", ["ignore-certificate-errors"])
                options.add_argument("--start-maximized")
                self.driver = webdriver.Chrome(executable_path=r"..\\..\\..\\Webdriverexe\chromedriver.exe", chrome_options=options)
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
