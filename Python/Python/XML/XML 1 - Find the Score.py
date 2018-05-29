# Solution for XML 1 - Find the Score

import sys
import xml.etree.ElementTree as etree


def get_attr_number(node):
    sum = len(node.attrib)
    for child in node:
        sum += get_attr_number(child)
    return sum


if __name__ == '__main__':
    sys.stdin.readline()
    xml = sys.stdin.read()
    tree = etree.ElementTree(etree.fromstring(xml))
    root = tree.getroot()
    print(get_attr_number(root))