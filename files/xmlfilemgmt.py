
import xml.etree.ElementTree as ET
import os


def write_xml(filename):
    # Create root element
    root = ET.Element("data")
    person1 = ET.SubElement(root, "person")
    name1 = ET.SubElement(person1, "name")
    name1.text = "John Doe"
    age1 = ET.SubElement(person1, "age")
    age1.text = "30"
    person2 = ET.SubElement(root, "person")
    name2 = ET.SubElement(person2, "name")
    name2.text = "Jane Smith"
    age2 = ET.SubElement(person2, "age")
    age2.text = "25"

    tree = ET.ElementTree(root)
    tree.write(filename)


def read_xml(filename):
    tree = ET.parse(filename)
    root = tree.getroot()
    for person in root.findall("person"):
        name = person.find("name").text
        age = person.find("age").text
        print(f"Name: {name}, Age: {age}")


def delete_xml(filename):
    if os.path.exists(filename):
        os.remove(filename)
        print(f"{filename} deleted successfully")
    else:
        print(f"{filename} does not exist")


filename = "data.xml"
write_xml(filename)
read_xml(filename)
delete_xml(filename)

