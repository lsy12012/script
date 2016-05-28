# -*- coding: utf-8 -*-
from xml.dom.minidom import parse, parseString #minidom 파싱함수 임포트
from xml.etree import ElementTree

### global
loopFlag = 1        #무한 루프 제어변수
xmlFD = -1          #XML문서 파일 디스크립터
AccidentDoc = None  #XML 문서 파싱한 후 반환된 DOC 객체 변수




def printMenu():
    print("\nWelcome! Accident Manager Program (xml version)") 
    print("========Menu==========")
    print("Load xml:  l")
    print("Print dom to xml: p")
    print("Quit program:   q")
    print("print Accident list: b")
    print("Add new accident: a")
    print("Search Accident Title: e")
    print("Make html: m")
    print("==================")


def launcherFunction(menu):
    global AccidentDoc
    if menu == 'l':
        AccidentDoc = LoadXMLFromFile()
    elif menu == 'q':
        QuitAccidentMgr()
    elif menu == 'p':
        printDOMtoXML()        
        
        
        
def LoadXMLFromFile():#minidom메서드 XML 문서 파싱하고 전역변수 AccidentDoc에 저장
    fileName = str(input("please input file name to load: ")) #읽을 파일경로 입력
    global xmlFD
    
    try:
        xmlFD = open(fileName)  #XML 문서 open
    except IOError:
        print("invalid file name or path")
        return None
    else:
        try:
            dom = parse(xmlFD)  #XML 문서 파싱
        except Exception:
            print("parse fail")
        else:
            print("XML Document loading complete!")
            return dom
    return None
    

def AccidentFree():#사용 후에는 unlink()메서드 호출해 DOM 객체 내부의 참조를 제거
    if checkDocument():
        AccidentDoc.unlink() #minidom 객체 해제
     

def PrintDOMtoXML():#toxml()메서드를 이용해서 DOM 객체를 XML문서로 변환
    if checkDocument():
        print(AccidentDoc.toxml())
        
        












while(loopFlag > 0):
    printMenu()
    menuKey = str(input('select menu :'))    
    launcherFunction(menuKey)
else:
    print("Thank you! Good Bye")