#!/usr/bin/python3
"""
Use xml module to convert to/from xml
"""


import xml.etree.ElementTree as ET
import os


def serialize_to_xml(dictionary, filename):
    """
    Convert a dict object to xml file
    """
    if not filename:
        print("filename not provided")
        return False
    
    if not dictionary:
        print("warning: dictionary is empty, nothing to convert")
        return False

    try:
        root = ET.Element("data")

        for key, value in dictionary.items():
            child = ET.SubElement(root, key)
            child.text = str(value)

        tree = ET.ElementTree(root)
        tree.write(filename, encoding="utf-8", xml_declaration=True)
        return True
    except Exception as e:
        print(e)
        return False
    
def deserialize_from_xml(filename):
    if not os.path.exists(filename):
        print(f"[XML Conversion] Error: File '{filename}' does not exist.")
        return False
    
    try:
        tree = ET.parse(filename)
        root = tree.getroot()

        data = {}
        for child in root:
            data[child.tag] = child.text
        # data["age"] = int(data["age"])
        return data
    except (Exception) as e:
        print(f"Deserialisation error {e}")
        return {}
