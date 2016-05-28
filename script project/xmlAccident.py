from xml.dom.minidom import parse, parseString
from xml.etree import ElementTree
from urllib.request import urlopen
from launcher import *
#### 전역변수
xmlFD = -1
AccidentDoc = None


def printAccident(tags):
    global AccidentDoc
    if not checkDocument():
        return None
    
    accidentlist = AccidentDoc.childNodes
    accident = accidentlist[0].childNodes
    
    for item in accident:
        if item.nodeName == "body":
            subitems = item.childNodes
            for atom in subitems:
                if atom.nodeName in tags:
                    print("title=",atom.firstChild.nodeValue)
                

def PrintDOMtoXML():
    if checkDocument():
        print(AccidentDoc.toxml())
        

def checkDocument():
    global AccidentDoc
    if AccidentDoc == None:
        print("Error : Document is empty")
        return False
    return True
    

                                
def SearchAccidentContinent(keyword):
    global AccidentDoc
    retlist = []
    if not checkDocument():
        return None
    
    try:
        tree = ElementTree.fromstring(str(AccidentDoc.toxml()))
    except Exception:
        print("Element Tree parsing Error: maybe the xml document is not corrected.")
        return None
        
    accidentElements = tree.getiterator("book") #return list type
    for item in accidentElements:
        strContinent = item.find("continent")
        if(strContinent.text.find(keyword) >= 0):
            retlist.append((item.attrib["item"], strContinent.text))
    
    return retlist
   
def printAccident(blist):
    for res in blist:
        print(res)