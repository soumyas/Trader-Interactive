from Src.utils import ReaderFile
import time

class TruckResetRefineSearch():
    
     def __init__(self,driver):
      self.driver=driver
      
     def openUrl(self):
      reader = ReaderFile.ReadXML()
      self.driver.get(reader.readInI('test', "URL"))
      
        
      
      locator= "zip_code";      
      self.driver.find_element_by_id(locator).send_keys(reader.readInI('test', "zip_code"))
      
        #Click Searchbutton at home page
     def clickOnSearchButton(self):
        reader = ReaderFile.ReadXML()
        locator = reader.readXml('SearchButton')
        time.sleep(3)
        self.driver.find_element_by_xpath(locator).click()
        
        #Click Class option at search page
     def clickOnClass(self):
        reader = ReaderFile.ReadXML()
        locator = reader.readXml('Class')
        time.sleep(3)
        self.driver.find_element_by_xpath(locator).click()
        
        #Select the class type
     def clickOnClassType(self):
        reader = ReaderFile.ReadXML()
        locator = reader.readXml('ClassType')
        time.sleep(3)
        self.driver.find_element_by_xpath(locator).click()
        
        #Click on Update button at Class popup window
     def clickOnUpdateButtonClass(self):
        reader = ReaderFile.ReadXML()
        locator = reader.readXml('UpdateButton')
        time.sleep(3)
        self.driver.find_element_by_xpath(locator).click()
        
        #Click Category option at search page
     def clickOnCategory(self):
        reader = ReaderFile.ReadXML()
        locator = reader.readXml('Category')
        time.sleep(3)
        self.driver.find_element_by_xpath(locator).click()
        
        #Select the Category type
     def clickOnCategoryType(self):
        reader = ReaderFile.ReadXML()
        locator = reader.readXml('CategoryType')
        time.sleep(3)
        self.driver.find_element_by_xpath(locator).click()
        
        #Select the Category type
     def clickOnStartOverButton(self):
        reader = ReaderFile.ReadXML()
        locator = reader.readXml('StartOver')
        time.sleep(3)
        self.driver.find_element_by_xpath(locator).click()
        
        #Click Back to home page
     def clickOnBackToHome(self):
        reader = ReaderFile.ReadXML()
        locator = reader.readXml('BackToHome')
        time.sleep(2)
        self.driver.find_element_by_xpath(locator).click()