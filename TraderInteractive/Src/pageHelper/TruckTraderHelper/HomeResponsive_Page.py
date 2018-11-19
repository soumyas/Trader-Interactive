from Src.utils import ReaderFile
import time

from selenium import webdriver
import unittest
#from Src.pageHelper.TruckTraderHelper import HomeResponsive_Page

class HomeResponsive_Page():  
    
     def __init__(self,driver):
      self.driver=driver
      
     def openUrl(self):
      reader = ReaderFile.ReadXML()
      self.driver.get(reader.readInI('test', "URL"))
      
      locator = "modelText";  
      self.driver.find_element_by_id(locator).send_keys(reader.readInI('test', "make"))
      
       
      locator= "zip_code";      
      self.driver.find_element_by_id(locator).send_keys(reader.readInI('test', "zip_code"))
      
    #Click Search button at home page
     def clickOnSearchButton(self):
        reader = ReaderFile.ReadXML()
        locator = reader.readXml('SearchButton')
        time.sleep(3)
        self.driver.find_element_by_xpath(locator).click()
        
        #Click Back to home page
     def clickOnBackToHome(self):
        reader = ReaderFile.ReadXML()
        locator = reader.readXml('BackToHome')
        time.sleep(2)
        self.driver.find_element_by_xpath(locator).click()
        
        #Click Seller Type
     def clickOnSellerType(self):
        reader = ReaderFile.ReadXML()
        locator = reader.readXml('SellerType')
        time.sleep(2)
        self.driver.find_element_by_xpath(locator).click()
        
        #Click on Private Seller
     def clickOnPrivateSeller(self):
        reader = ReaderFile.ReadXML()
        locator = reader.readXml('PrivateSeller')
        time.sleep(2)
        self.driver.find_element_by_xpath(locator).click()
        
        #Verify Private Seller
     #def verifyPrivateSeller(self):
         #reader = ReaderFile.ReadXML()
        # locator = reader.readXml('PrivateSeller')
        #print (self.is_element_present(By.XPATH, locator))
        #self.assertFalse(self.is_element_present(By.XPATH, locator)) 
        
        #Click on Private Party
     def clickOnPrivateParty(self):
        reader = ReaderFile.ReadXML()
        locator = reader.readXml('PrivateParty')
        time.sleep(3)
        self.driver.find_element_by_xpath(locator).click()
        
     def getprivatepartydetails(self):
        reader = ReaderFile.ReadXML()
        locator = reader.readXml('PrivatePartyDetails')
        time.sleep(3)
        return(self.driver.find_element_by_xpath(locator).get_attribute('innerHTML'))
        
     def getprivatepartydetailsafterclick(self):
        reader = ReaderFile.ReadXML()
        locator = reader.readXml('PrivatePartyDetailsAClick')
        time.sleep(3)
        return(self.driver.find_element_by_xpath(locator).get_attribute('innerHTML'))
     
     def comparestring(self, expected, actual):
         self.assertEqual(expected, actual)
         
         
        #Click on Non-Private seller
     def clickOnNonPrivateSeller(self):
        reader = ReaderFile.ReadXML()
        locator = reader.readXml('NonPrivateSeller')
        time.sleep(2)
        self.driver.find_element_by_xpath(locator).click()
        
        #Verify Non-Private seller
     #def verifyNonPrivateSeller(self):
      #  reader = ReaderFile.ReadXML()
       # locator = reader.readXml('NonPrivateSeller')
        #print (self.is_element_present(By.XPATH, locator))
        #self.assertFalse(self.is_element_present(By.XPATH, locator)) 
        
        #Click on Non Private Party
     def clickOnNonPrivateParty(self):
        reader = ReaderFile.ReadXML()
        locator = reader.readXml('NonPrivateParty')
        time.sleep(3)
        self.driver.find_element_by_xpath(locator).click()
        
     def getnonprivatepartydetails(self):
        reader = ReaderFile.ReadXML()
        locator = reader.readXml('NonPrivatePartyDetails')
        time.sleep(3)
        return(self.driver.find_element_by_xpath(locator).get_attribute('innerHTML'))
    
     def getnonprivatepartydetailsafterclick(self):
        reader = ReaderFile.ReadXML()
        locator = reader.readXml('NonPrivatePartyDetailsAClick')
        time.sleep(3)
        return(self.driver.find_element_by_xpath(locator).get_attribute('innerHTML'))
     
         
        #Click StartOver
     def clickOnRefineSearch(self):
        reader = ReaderFile.ReadXML()
        locator = reader.readXml('StartOver')
        time.sleep(2)
        self.driver.find_element_by_xpath(locator).click()