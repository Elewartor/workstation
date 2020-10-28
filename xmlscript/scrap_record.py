import xml.etree.ElementTree as et
import os
import sys

#Input variables.
# --------------------------------
scrap_number = sys.argv[1]
# --------------------------------

#XML data parsing.
parsedData = et.parse('C:\\Users\\IntentRefurbish\\Desktop\\workstation\\workstation\\xmlscript\\scrap_record.xml')
rootPrint = parsedData.getroot().find('Command').find('Print')

#Setting label scrap number.
rootPrint.find('NamedSubString/[@Name="scrap_record_number"]').find('Value').text = str(scrap_number)

#Modifying XML file.
parsedData.write('C:\\Users\\IntentRefurbish\\Desktop\\workstation\\workstation\\xmlscript\\scrap_record.xml')

#Script executing.
command = 'bartend.exe /XMLScript="C:\\Users\\IntentRefurbish\\Desktop\\workstation\\workstation\\xmlscript\\scrap_record.xml" /X'
os.system(command)