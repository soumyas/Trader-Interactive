#import easy to use xml parser called minidom:
from xml.dom.minidom import parseString
import os
import configparser
from configparser import SafeConfigParser

#all these imports are standard on most modern python implementations
class ReadXML:
    def readXml(self,str):
            #open the xml file for reading:
            #locator_dir = os.getcwd()
            #print(locator_dir)
            #if "trucktrader" not in locator_dir:
            #    locator_dir = locator_dir.replace(r'Src\tests\equipmenttrader', 'LocatorFactory\locator.xml')
            #else:
            #    locator_dir = locator_dir.replace(r'Src\tests\trucktrader', 'LocatorFactory\locator.xml')
            
            #locator_dir = locator_dir.replace(os.sep, '/')
            #print(locator_dir)
            
            file = open('C:/Users/admin/eclipse-workspace/TraderInteractive/LocatorFactory/locator.xml','r')
            #convert to string:
            data = file.read()
            #close file because we dont need it anymore:
            file.close()
            #parse the xml you got from the file
            dom = parseString(data)
            #retrieve the first xml tag (<tag>data</tag>) that the parser finds with name tagName:
            xmlTag = dom.getElementsByTagName(str)[0].toxml()
            #strip off the tag (<tag>data</tag>  --->   data):
            xmlData=xmlTag.replace('<'+str+'>','').replace('</'+str+'>','')
            return xmlData
        
    def readInI(self, header,key):
            parser = SafeConfigParser()
            #data_dir = os.getcwd()
            #if "trucktrader" not in data_dir:
            #    data_dir = data_dir.replace(r'Src\tests\equipmenttrader', 'Config\settings.ini')
            #else:
            #    data_dir = data_dir.replace(r'Src\tests\trucktrader', 'Config\settings.ini')
            #data_dir = data_dir.replace(os.sep, '/')
            #print(data_dir)
            #parser.read(data_dir)
            #value = parser.get(header, key)
            #return value
            parser.read('C:/Users/admin/eclipse-workspace/TraderInteractive/Config/settings.ini')
            value=parser.get(header, key)
            return value