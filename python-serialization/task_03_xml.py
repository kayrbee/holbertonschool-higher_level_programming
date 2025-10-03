#!/usr/bin/python3
"""
Use xml module to convert to/from xml
"""


import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """
    Convert a dict object to xml file
    """
    if not dictionary or not filename:
        print(f"[XML Conversion] dict or filename not provided")
        return False

    try:
        root = ET.Element("data")

        for key, value in dictionary.items():
            child = ET.SubElement(root, key)
            child.text = str(value)

        tree = ET.ElementTree(root)
        tree.write(filename, encoding="utf-8", xml_declaration=True)
    except (ET.ParseError, TypeError, AttributeError) as e:
        print(e)
    except FileNotFoundError as e:
        pass
    
def deserialize_from_xml(filename):
    try:
        tree = ET.parse(filename)
        root = tree.getroot()

        data = {}
        for child in root:
            data[child.tag] = child.text
        data["age"] = int(data["age"])
        return data
    except Exception as e:
        print(f"Deserialisation error {e}")
