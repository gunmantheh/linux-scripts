#!/usr/bin/env python

import urllib.request, json
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
    global i, dataList, server, xmlurl, xml, dom, node, node2, part, remoteFile, choice, e
    i = 0
    dataList = []
    server = 'http://10.0.33.26:32400'
    xmlurl = server + '/search?local=1&query=' + sys.argv[1]
    try:
        xml = urllib.request.urlopen(xmlurl)
        dom = parse(xml)
        for node in dom.getElementsByTagName('Video'):
            print(getAttr(node, 'grandparentTitle') + ' (' + getAttr(node, 'year') + ')')
            print(node.attributes['title'].value)
            for node2 in node.getElementsByTagName('Media'):
                for part in node2.getElementsByTagName('Part'):
                    # print('-'*10,end="")
                    i += 1
                    print(
                        str(i) + ' - [' + getAttr(part, 'container') + '] - [' + getAttr(node2,
                                                                                         'videoResolution') + '] - ',
                        end="")
                    remoteFile = server + part.attributes['key'].value
                    dataList.append(remoteFile)
                    print(remoteFile)
            print()
        choice = int(input('Which do you want to play (0 for nothing): '))
        if choice == 0:
            sys.exit()
        # return 0
        elif choice > 0 and choice <= len(dataList):
            print(dataList[choice - 1])
            call(["mpv", dataList[choice - 1]])
    except Exception as e:
        print(e)

if __name__ == '__main__':
    main()


