from Src.utils import ReaderFile
import time

class MyEquipmentLogin():
    
     def __init__(self,driver):
      self.driver = driver

      
     def openUrl(self):
      reader = ReaderFile.ReadXML()
      self.driver.get(reader.readInI('test', "URL1"))
    
      
    #Click on Log In icon
     def clickOnLogInButton(self):
        reader = ReaderFile.ReadXML()
        locator = reader.readXml('LogIn')
        time.sleep(3)
        self.driver.find_element_by_xpath(locator).click()
        
     def enterUserDetails(self):
      reader = ReaderFile.ReadXML()
      locator = reader.readXml('user')
      time.sleep(3)
      self.driver.find_element_by_xpath(locator).send_keys(reader.readInI('test', "username"))
     
      locator = reader.readXml('pass') 
      self.driver.find_element_by_xpath(locator).send_keys(reader.readInI('test', "password"))
      
    #Click on SignIn Button at MyT page
     def clickOnSignInButton(self):
        reader = ReaderFile.ReadXML()
        locator = reader.readXml('SignInButton')
        time.sleep(3)
        self.driver.find_element_by_xpath(locator).click()
        
        #Click on Hamburger Icon       
     def clickOnHamburgerIcon(self):
        reader = ReaderFile.ReadXML()
        locator = reader.readXml('Hamburger')
        time.sleep(3)
        self.driver.find_element_by_xpath(locator).click()
        
        #Click on Sign Out MyTrader       
     def clickOnSignOutMyTrader(self):
        reader = ReaderFile.ReadXML()
        locator = reader.readXml('SignOutMyTrader')
        time.sleep(3)
        self.driver.find_element_by_xpath(locator).click()