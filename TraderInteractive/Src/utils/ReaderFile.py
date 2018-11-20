#import easy to use xml parser called minidom:
from xml.dom.minidom import parseString
import os
import configparser
from configparser import SafeConfigParser

#all these imports are standard on most modern python implementations
class ReadXML:
    def readXml(self,str):
            file = open(r"..\\..\\..\\LocatorFactory\\locator.xml",'r')
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
            parser.read(r'..\\..\\..\\Config\\settings.ini')
            value=parser.get(header, key)
            return value