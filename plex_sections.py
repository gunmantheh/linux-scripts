#!/usr/bin/env python

import urllib.request
from xml.dom.minidom import parse
import urllib
import sys, getopt
from subprocess import call


def getAttr(elem, key):
    if key in elem.attributes:
        return elem.attributes[key].value
    else:
        return ""

# init variables

# this is a test comment

def main():
    global i, dataList, server, xmlurl, xml, dom, node, e
    i = 0
    dataList = []
    server = 'http://127.0.0.1:32400'
    xmlurl = server + '/library/sections'
    try:
        xml = urllib.request.urlopen(xmlurl)
        dom = parse(xml)
        for node in dom.getElementsByTagName('Directory'):
            print(getAttr(node, 'title') + ' (' + getAttr(node, 'key') + ')')
    except Exception as e:
        print(e)

if __name__ == '__main__':
    main()


