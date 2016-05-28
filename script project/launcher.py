# -*- coding: cp949 -*-
loopFlag = 1
from xml.dom.minidom import parse, parseString
from xml.etree import ElementTree
from urllib.request import urlopen
from internetAccident import *

AccidentDoc = None
informofLostsXMLDoc = None
server = "apis.data.go.kr"
regKey = 'BrS5flwzIznCPz8iKRmQUWehNDm%2FGI9dCqieoD%2B6qH%2BKT77TYm8vVQ0me49Y1LYejkHnkEPAil7eeESY6WQCcA%3D%3D'

def printMenu():
    print("\n Welcome!")
    print("===Menu===")
    print("Load XML: l")
    print("대륙별 검색: c")
    print("나라별 검색: n")
    print("Quit program: q")
    

def launcherFunction(menu):
    if menu == 'l':
        LoadXMLFromFile()
    elif menu == 'c':
        keyword = str(input('input keyword to search: '))
        printAccident(SearchAccidentContinent(keyword))
    elif menu == 'n':
        if AccidentDoc == None:
            print("Error : Document is empty")
            return False
        else:
            IsoCode = SelectNation()
            PrintNation(IsoCode)
                 
    elif menu == 'q':
        QuitAccidentMgr()
        
    else:
        print("error : unknown menu key")
      
def SelectNation():
    global AccidentDoc
    if not checkDocument():
        return None
    
    response = AccidentDoc.childNodes
    rsp_child = response[0].childNodes
    
    for item in rsp_child:
        if item.nodeName == "body":
            body_list = item.childNodes
            items = body_list[0]
            items_list = items.childNodes
            for i, item in enumerate(items_list):
                item_list = item.childNodes
                print("{0}. {1}".format(i, item_list[1].firstChild.nodeValue))
                
   
    IsoCode = str(input("ISO 국가코드를 입력하시오: "))
    print(IsoCode, "를 선택")
    return IsoCode

        
def PrintNation(IsoCode):
    global regKey
    global informofLostsXMLDoc
    losts_inform_dic = \
    {
        "continent" : "대륙: ", "ename" : "nation: ", "id" : "id: ",
        "imgUrl" : "imgUrl1: ", "imgUrl2" : "imgUrl2: ", "name" : "국가: ",
        "news" : "소식: ", "wrtDt" : "작성 날짜: "
    }
    URL = "http://" + server + "/1262000/AccidentService/getAccidentList?serviceKey=" + regKey + "&isoCode1=" + IsoCode
   # URL = "http://apis.data.go.kr/1262000/AccidentService/getAccidentList?serviceKey=BrS5flwzIznCPz8iKRmQUWehNDm%2FGI9dCqieoD%2B6qH%2BKT77TYm8vVQ0me49Y1LYejkHnkEPAil7eeESY6WQCcA%3D%3D&numOfRows=999&pageSize=999&pageNo=1&startPage=1"
   # print(IsoCode)
   # print(URL)
    try:
        xmlFD = urlopen(URL)
    except IOError:
        print("loading fail!!!")
    else:
        try:
            informofLostsXMLDoc = parse(xmlFD)
        except Exception:
            print("Error: Document is empty")
        else:
            print("검색 조건에 해당하는 정보들을 출력합니다.")
            response = informofLostsXMLDoc.childNodes
            rsp_child = response[0].childNodes
            for item in rsp_child:
                if item.nodeName == "body":
                    body_list = item.childNodes
                    items = body_list[0]
                    items_list = items.childNodes
                    for i, item in enumerate(items_list):
                        item_list = item.childNodes
                        for losts_inform in item_list:
                            if losts_inform.nodeName != "rnum":
                                print(losts_inform_dic[losts_inform.nodeName], losts_inform.firstChild.nodeValue)        

    
#### xml 관련 함수 구현
def LoadXMLFromFile():
    global xmlFD, AccidentDoc
    try:
        xmlFD = urlopen("http://apis.data.go.kr/1262000/AccidentService/getAccidentList?serviceKey=BrS5flwzIznCPz8iKRmQUWehNDm%2FGI9dCqieoD%2B6qH%2BKT77TYm8vVQ0me49Y1LYejkHnkEPAil7eeESY6WQCcA%3D%3D&numOfRows=999&pageSize=999&pageNo=1&startPage=1")
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

def QuitAccidentMgr():
    global loopFlag
    loopFlag = 0
    Quit()

def Quit():
    if checkDocument():
        AccidentDoc.unlink()
        

def checkDocument():
    global AccidentDoc
    if AccidentDoc == None:
        print("Error : Document is empty")
        return False
    return True

while(loopFlag > 0):
    printMenu()
    menuKey = str(input('select menu: '))
    launcherFunction(menuKey)
else:
    print("Thank you! Good Bye")