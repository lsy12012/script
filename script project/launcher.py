# -*- coding: cp949 -*-
loopFlag = 1
from xml.dom.minidom import parse, parseString
from xml.etree import ElementTree
from urllib.request import urlopen
from email.mime.text import MIMEText
from internetAccident import *

import smtplib
#import mysmtplib
#import Accident

AccidentDoc = None
XMLDoc = None
server = "apis.data.go.kr"
regKey = 'BrS5flwzIznCPz8iKRmQUWehNDm%2FGI9dCqieoD%2B6qH%2BKT77TYm8vVQ0me49Y1LYejkHnkEPAil7eeESY6WQCcA%3D%3D'

host = "smtp.gmail.com" # Gmail SMTP 서버 주소
port = "587"
mail = None
#mailer = None

def printMenu():
    print("\n Welcome!")
    print("===Menu===")
    print("Load XML: l")
    print("나라별 검색: n")
    print("이메일 전송: s")
    print("Quit program: q")
    

def launcherFunction(menu):
    if menu == 'l':
        LoadXMLFromFile()
    elif menu == 'n':
        if AccidentDoc == None:
            print("Error : Document is empty")
            return False
        else:
            IsoCode = SelectNation()
            PrintNation(IsoCode)
                 
    elif menu == 's':
        SendEmail()        
        
    elif menu == 'q':
        QuitAccidentMgr()
        
    else:
        print("error : unknown menu key")
      
      
def SelectNation():
    global AccidentDoc
    if not checkDocument():
        return None
    
    f = open("C:/script/script project/ISO 국가코드.txt", "r")
    print(f.read())
    f.close()            
    IsoCode = str(input("ISO 국가코드를 입력하시오: "))
    print(IsoCode, "를 선택")
    print("*************************")
    return IsoCode

        
def PrintNation(IsoCode):
    global regKey
    global XMLDoc
#    nation_dic = \
#    {
#        "continent" : "대륙: ", "ename" : "nation: ", "id" : "id: ",
#        "imgUrl" : "imgUrl1: ", "imgUrl2" : "imgUrl2: ", "name" : "국가: ",
#        "news" : "소식: ", "wrtDt" : "작성 날짜: "
#    }

    nation_dic = \
    {
        "continent" : "대륙: ", 
        "ename" : "nation: ",
        "id" : "id: ",
        "imgUrl" : "imgUrl1: ", 
        "imgUrl2" : "imgUrl2: ",
        "name" : "국가: ",
        "news" : "소식: ", 
        "wrtDt" : "작성 날짜: "
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
                    items_list = body_list[0].childNodes
                    for i, item in enumerate(items_list):
                        item_list = item.childNodes
                        for nation in item_list:
                             if nation.nodeName != "imgUrl":
                                print(nation_dic[nation.nodeName], nation.firstChild.nodeValue)                            
                                    
                else:
                    print("해당 국가에 대한 정보가 없습니다.")
    
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

## 이메일
def LoginEmail():
    global mail
    mail = smtplib.SMTP(host, port)
    mail.ehlo()
    mail.starttls()
    mail.ehlo()
    mail.login("lsy1201212@gmail.com", "sksms1gkrsus8qks")


def SendMail(mailaddress):
    text = "Hello world!"
    msg = MIMEText(text)
    senderAddr = "lsy1201212@gmail.com"
    recipientAddr = mailaddress
    
    msg['subject'] = "제목: 테스트"
    msg['From'] = senderAddr
    msg['To'] = recipientAddr
    
    global mail
    mail.sendmail(senderAddr, [recipientAddr], msg.as_string())
    mail.close()
    print("메일 전송에 성공.")
    
def SendEmail():
    LoginEmail()
    mailaddress = input("수신자의 이메일 주소를 입력하세요: ")
    print("메일 전송 중...")
    SendMail(mailaddress)



while(loopFlag > 0):
    printMenu()
    menuKey = str(input('select menu: '))
    launcherFunction(menuKey)
else:
    print("Thank you! Good Bye")