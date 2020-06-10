import xml.etree.ElementTree as et
import os
import sys

#Input variables.
# --------------------------------
copies = sys.argv[1]

upc = sys.argv[2]
qty = sys.argv[3]
extra = sys.argv[4]
model = sys.argv[5]

print(copies, qty, extra, model, upc,)
# --------------------------------

#XML data parsing.
parsedData = et.parse('C:\\Users\\IntentRefurbish\\Desktop\\workstation\\workstation\\xmlscript\\boxlabelextra.xml')
rootPrint = parsedData.getroot().find('Command').find('Print')

#Setting print copies qty.
rootPrint.find('PrintSetup').find('IdenticalCopiesOfLabel').text = str(copies)

#Setting label upc.
rootPrint.find('NamedSubString/[@Name="upc"]').find('Value').text = str(upc)
#Setting label qty.
rootPrint.find('NamedSubString/[@Name="qty"]').find('Value').text = str(qty)
#Setting label extras.
rootPrint.find('NamedSubString/[@Name="extra"]').find('Value').text = str(extra)
#Setting label model.
rootPrint.find('NamedSubString/[@Name="model"]').find('Value').text = str(model)

#Modifying XML file.
parsedData.write('C:\\Users\\IntentRefurbish\\Desktop\\workstation\\workstation\\xmlscript\\boxlabelextra.xml')

#Script executing.
command = 'bartend.exe /XMLScript="C:\\Users\\IntentRefurbish\\Desktop\\workstation\\workstation\\xmlscript\\boxlabelextra.xml" /X'
os.system(command)