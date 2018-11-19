from selenium import webdriver
from Src.utils import ReaderFile
import time
import unittest

class TruckResult(unittest.TestCase):
    
     def __init__(self,driver):
      self.driver=driver

      
     def openUrl(self):
      reader = ReaderFile.ReadXML()
      self.driver.get(reader.readInI('test', "URL"))
      
    #Click Searchbutton at home page
     def clickOnSearchButton(self):
        reader = ReaderFile.ReadXML()
        locator = reader.readXml('SearchButton')
        time.sleep(3)
        self.driver.find_element_by_xpath(locator).click()
        
    #Expand the Keyword section 
     def clickOnKeywordSection(self):
        reader = ReaderFile.ReadXML()
        locator = reader.readXml('KeywordResult')
        time.sleep(3)
        self.driver.find_element_by_xpath(locator).click()
      
              
     def enterDetails(self):
        reader = ReaderFile.ReadXML()
        locator = reader.readXml('KeywordInput')
        time.sleep(3)
        self.driver.find_element_by_xpath(locator).send_keys(reader.readInI('test', "keyword"))
        
        locator = "inputWrapr keyword";  
        self.driver.find_element_by_id(locator).send_keys(reader.readInI('test', "inputWrapr keyword"))
        
        #Click on Update keyword button at search result page 
     def clickOnKeywordUpdateButton(self):
        reader = ReaderFile.ReadXML()
        locator = reader.readXml('KeywordUpdateButton')
        time.sleep(3)
        self.driver.find_element_by_xpath(locator).click()
        
        #Click Class option at search page
     def clickOnClass(self):
        reader = ReaderFile.ReadXML()
        locator = reader.readXml('Class')
        time.sleep(3)
        self.driver.find_element_by_xpath(locator).click()
        
        #Select the class type
     def clickOnClassType1(self):
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
     def clickOnCategoryType1(self):
        reader = ReaderFile.ReadXML()
        locator = reader.readXml('CategoryType')
        time.sleep(3)
        self.driver.find_element_by_xpath(locator).click()
    
        #Click Make option at search page
     def clickOnMake(self):
        reader = ReaderFile.ReadXML()
        locator = reader.readXml('Make')
        time.sleep(3)
        self.driver.find_element_by_xpath(locator).click()
        
        #Select the Make type
     def clickOnMakeType(self):
        reader = ReaderFile.ReadXML()
        locator = reader.readXml('MakeType')
        time.sleep(3)
        self.driver.find_element_by_xpath(locator).click()
        
        #Click Make option at search page
     def clickOnModel(self):
        reader = ReaderFile.ReadXML()
        locator = reader.readXml('Model')
        time.sleep(3)
        self.driver.find_element_by_xpath(locator).click()
        
        #Select the Make type
     def clickOnModelType(self):
        reader = ReaderFile.ReadXML()
        locator = reader.readXml('ModelType')
        
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