from Src.utils import ReaderFile
import time

class TruckDealerSearch():
    
     def __init__(self,driver):
      self.driver=driver

      
     def openUrl(self):
      reader = ReaderFile.ReadXML()
      self.driver.get(reader.readInI('test', "URL"))
         
    #Expand the Dealer arrow icon at home page
     def clickOnDealerIcon(self):
        reader = ReaderFile.ReadXML()
        locator = reader.readXml('Dealer')
        time.sleep(3)
        self.driver.find_element_by_xpath(locator).click()
      
      
        #Click on Search Dealer Button
     def clickOnSearchDealer(self):
        reader = ReaderFile.ReadXML()
        locator = reader.readXml('SearchDealerButton')
        time.sleep(3)
        self.driver.find_element_by_xpath(locator).click()
        
        #Click on All Class Droplist
     def clickOnAllClass(self):
        reader = ReaderFile.ReadXML()
        locator = reader.readXml('AllClass')
        time.sleep(3)
        self.driver.find_element_by_xpath(locator).click()
        
        #Select option under the All Class droplist
     def selectClassOption(self):
        reader = ReaderFile.ReadXML()
        locator = reader.readXml('ClassHeavyduty')
        time.sleep(3)
        self.driver.find_element_by_xpath(locator).click()
                
        #Click on All Category Droplist
     def clickOnAllCategory(self):
        reader = ReaderFile.ReadXML()
        locator = reader.readXml('AllCategory')
        time.sleep(3)
        self.driver.find_element_by_xpath(locator).click()
        
        #Select option under the All Class droplist
     def selectCategoryOption(self):
        reader = ReaderFile.ReadXML()
        locator = reader.readXml('CategoryAmbulance')
        time.sleep(3)
        self.driver.find_element_by_xpath(locator).click()
        
        #Click on All Make Droplist
     def clickOnAllMake(self):
        reader = ReaderFile.ReadXML()
        locator = reader.readXml('AllMake')
        time.sleep(3)
        self.driver.find_element_by_xpath(locator).click()
        
        #Select option under the All Make droplist
     def selectMakeOption(self):
        reader = ReaderFile.ReadXML()
        locator = reader.readXml('MakeFord')
        time.sleep(3)
        self.driver.find_element_by_xpath(locator).click()
        
        locator= "zip_code";      
        self.driver.find_element_by_id(locator).send_keys(reader.readInI('test', "zip_code"))
        
        #Click on Dealer search button
     def clickOnDealerSearchButton(self):
        reader = ReaderFile.ReadXML()
        locator = reader.readXml('Search')
        time.sleep(3)
        self.driver.find_element_by_xpath(locator).click()
      
        #Click on Dealer search result button
     def clickOnDealerResultButton(self):
        reader = ReaderFile.ReadXML()
        locator = reader.readXml('DealerResultButton')
        time.sleep(2)
        self.driver.find_element_by_xpath(locator).click()
        
        #Expand the Dealer Class option
     def clickOnDealerClass(self):
        reader = ReaderFile.ReadXML()
        locator = reader.readXml('DealerClass')
        time.sleep(3)
        self.driver.find_element_by_xpath(locator).click()
        
        #Select the Multiple Dealer class
     def clickOnDealerClass1(self):
        reader = ReaderFile.ReadXML()
        locator = reader.readXml('MultiiClass1')
        time.sleep(3)
        self.driver.find_element_by_xpath(locator).click()
        
     def clickOnDealerClass2(self):
        reader = ReaderFile.ReadXML()
        locator = reader.readXml('MultiiClass2')
        time.sleep(3)
        self.driver.find_element_by_xpath(locator).click()
        
     def clickOnDealerClass3(self):
        reader = ReaderFile.ReadXML()
        locator = reader.readXml('MultiiClass3')
        time.sleep(3)
        self.driver.find_element_by_xpath(locator).click()
        
        #Click on Update button at Class popup window
     def clickOnDealerClassUpdateButton(self):
        reader = ReaderFile.ReadXML()
        locator = reader.readXml('DealerUpdateButton')
        time.sleep(3)
        self.driver.find_element_by_xpath(locator).click()
        
        #Click Back to home page
     def clickOnBackToHome(self):
        reader = ReaderFile.ReadXML()
        locator = reader.readXml('BackToHome')
        time.sleep(2)
        self.driver.find_element_by_xpath(locator).click()
        
        