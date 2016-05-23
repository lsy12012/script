# -*- coding: cp949 -*-
loopFlag = 1
from internetbook import *

#### Menu  implementation
def printMenu():
    print("\nWelcome! Book booManager Program (xml version)")
    print("========Menu==========")
    print("Load xml:  1")
    print("Print dom to xml: 2")
    print("Quit program:   3")
    print("print Accident list: 4")
    print("Add new Accident: 5")
    print("Search Accident Title: 6")
    print("Make html: 7")
    print("----------------------------------------")
    print("Get Accident data from isbn: 8")
    print("Send mail : 9")
    print("Start Web Service: 0")
    print("========Menu==========")
    
def launcherFunction(menu):
    if menu ==  '1':
        LoadXMLFromFile()
    elif menu == '3':
        QuitBookMgr()
    elif menu == '2':
        PrintDOMtoXML()
    elif menu == '4':
        PrintBookList(["title",])
    elif menu == '5':
        ISBN = str(input ('insert ISBN :'))
        title = str(input ('insert Title :'))
        AddBook({'ISBN':ISBN, 'title':title})
    elif menu == '6':
        keyword = str(input ('input keyword to search :'))
        printBookList(SearchBookTitle(keyword))
    elif menu == '8': 
        isbn = str(input ('input isbn to get :'))
        #isbn = '0596513984'
        ret = getBookDataFromISBN(isbn)
        AddBook(ret)
    elif menu == '7':
        keyword = str(input ('input keyword code to the html  :'))
        html = MakeHtmlDoc(SearchBookTitle(keyword))
        print("-----------------------")
        print(html)
        print("-----------------------")
    elif menu == '9':
        sendMain()
    elif menu == "0":
        startWebService()
    else:
        print ("error : unknow menu key")

def QuitBookMgr():
    global loopFlag
    loopFlag = 0
    BooksFree()
    
##### run #####
while(loopFlag > 0):
    printMenu()
    menuKey = str(input ('select menu :'))
    launcherFunction(menuKey)
else:
    print ("Thank you! Good Bye")
