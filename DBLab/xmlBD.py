from xml.dom import minidom
from xml.etree import ElementTree as ET
tree = ET.ElementTree('sample.xml')
tree=ET.parse('sample.xml')
file01 = open('music.xml','r')
tree=ET.parse(file01)