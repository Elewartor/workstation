import xml.etree.ElementTree as et
import os
import sys

#Input variables.
# --------------------------------
copies = sys.argv[1]

upc = sys.argv[2]
part_number = sys.argv[3]
title = sys.argv[4]

# --------------------------------

#XML data parsing.
parsedData = et.parse('C:\\Users\\IntentRefurbish\\Desktop\\workstation\\workstation\\xmlscript\\label.xml')
rootPrint = parsedData.getroot().find('Command').find('Print')

#Setting print copies qty.
rootPrint.find('PrintSetup').find('IdenticalCopiesOfLabel').text = str(copies)

#Setting label upc.
rootPrint.find('NamedSubString/[@Name="upc"]').find('Value').text = str(upc)
#Setting label qty.
rootPrint.find('NamedSubString/[@Name="part_number"]').find('Value').text = str(part_number)
#Setting label model.
rootPrint.find('NamedSubString/[@Name="title"]').find('Value').text = str(title)

#Modifying XML file.
parsedData.write('C:\\Users\\IntentRefurbish\\Desktop\\workstation\\workstation\\xmlscript\\label.xml')

#Script executing.
command = 'bartend.exe /XMLScript="C:\\Users\\IntentRefurbish\\Desktop\\workstation\\workstation\\xmlscript\\label.xml" /X'
os.system(command)