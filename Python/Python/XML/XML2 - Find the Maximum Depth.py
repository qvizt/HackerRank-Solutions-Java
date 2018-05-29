# Solution for XML2 - Find the Maximum Depth

import xml.etree.ElementTree as etree

maxdepth = 0


def depth(elem, level):
    level += 1
    global maxdepth
    maxdepth = max(maxdepth, level)
    for child in elem:
        depth(child, level)


if __name__ == '__main__':
    n = int(input())
    xml = ""
    for i in range(n):
        xml = xml + input() + "\n"
    tree = etree.ElementTree(etree.fromstring(xml))
    depth(tree.getroot(), -1)
    print(maxdepth)
