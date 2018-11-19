from Src.utils import ReaderFile
import time

class Equipmentkeywordsearch():
    
     def __init__(self,driver):
      self.driver=driver
      
     def openUrl(self):
      reader = ReaderFile.ReadXML()
      self.driver.get(reader.readInI('test', "URL1"))
      
        
      locator = "modelText";  
      self.driver.find_element_by_id(locator).send_keys(reader.readInI('test', "make1"))
      
      #locator= "zip_code";      
      #self.driver.find_element_by_id(locator).send_keys(reader.readInI('test', "zip_code"))
      
        #Click Searchbutton at home page
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
        
      