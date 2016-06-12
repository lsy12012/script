# -*- coding: utf-8 -*-
"""
Created on Sun Jun 12 18:37:54 2016

@author: dltkd
"""

def SelectNation():
    global AccidentDoc
    if not checkDocument():
        return None
    
    f = open("C:/script/script project/ISO 국가코드.txt", "r")
    print(f.read())
    f.close()            
    IsoCode = str(input("ISO 국가코드를 입력하시오: "))
    print(IsoCode, "를 선택")
    return IsoCode

        
def PrintNation(IsoCode):
    global regKey
    global XMLDoc
    nation_dic = \
    {
        "continent" : "대륙: ", "ename" : "nation: ", "id" : "id: ",
        "imgUrl" : "imgUrl1: ", "imgUrl2" : "imgUrl2: ", "name" : "국가: ",
        "news" : "소식: ", "wrtDt" : "작성 날짜: "
    }
    URL = "http://" + server + "/1262000/AccidentService/getAccidentList?serviceKey=" + regKey + "&isoCode1=" + IsoCode

    try:
        xmlFD = urlopen(URL)
    except IOError:
        print("loading fail!!!")
    else:
        try:
            XMLDoc = parse(xmlFD)
        except Exception:
            print("Error: Document is empty")
        else:
            response = XMLDoc.childNodes
            rsp_child = response[0].childNodes
            for item in rsp_child:
                if item.nodeName == "body":
                    body_list = item.childNodes
                    items = body_list[0]
                    items_list = items.childNodes
                    for i, item in enumerate(items_list):
                        item_list = item.childNodes
                        for nation in item_list:
                            if nation.nodeName != "rnum":
                                print(nation_dic[nation.nodeName], nation.firstChild.nodeValue)        

    
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