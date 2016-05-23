from xml.dom.minidom import parse, parseString
from xml.etree import ElementTree

#### 전역변수
xmlFD = -1
AccidentDoc = None

#### xml 관련 함수 구현
def LoadXMLFromFile():
    fileName = str(input("please input file name to load : "))
    global xmlFD, AccidentDoc
    try:
        xmlFD = open(fileName)
    except IOError:
        print("invalid file name or path")
    else:
        try:
            dom = parse(xmlFD)
        except Exception:
            print("loading fail!!!")
        else:
            print("XML Document loading complete")
            AccidentDoc = dom
            return dom
    return None