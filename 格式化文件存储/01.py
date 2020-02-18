import xml.etree.ElementTree as et

stu = et.Element("Student")

name = et.SubElement(stu,'Name')
name.attrib = {'lang','en'}
name.text = 'liudana'

age = et.SubElement(stu,'age')
age.text = 18

et.dump(stu)