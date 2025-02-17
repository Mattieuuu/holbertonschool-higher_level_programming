#!/usr/bin/env python3
"""Module for XML serialization operations"""
import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """
    Serialize a dictionary to XML and save to file
    Args:
        dictionary: Dictionary to serialize
        filename: Output XML file name
    """
    try:
        root = ET.Element("data")

        for key, value in dictionary.items():
            child = ET.SubElement(root, key)
            child.text = str(value)

        tree = ET.ElementTree(root)
        tree.write(filename, encoding='utf-8', xml_declaration=True)
        return True
    except Exception:
        return False


def deserialize_from_xml(filename):
    """
    Deserialize XML data from file to dictionary
    Args:
        filename: Input XML file name
    Returns:
        Dictionary containing the deserialized data
    """
    try:
        tree = ET.parse(filename)
        root = tree.getroot()

        result = {}
        for child in root:
            result[child.tag] = child.text

        return result
    except Exception:
        return None
