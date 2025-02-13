#!/usr/bin/python3
import xml.etree.ElementTree as ET


def serialize_to_xml(dictionnary, filename):

    root = ET.Element("data")

    for key, value in dictionnary.items():
        child = ET.SubElement(root, key)
        child.text = str(value)

    tree = ET.ElementTree(root)
    tree.write(filename)


def deserialize_from_xml(filename):

    tree = ET.parse(filename)
    root = tree.getroot()

    dictionnary = {child.tag: child.text for child in root}
    return dictionnary
