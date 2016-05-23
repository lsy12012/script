loopFlag = 1
from xmlAccident import*

####메뉴
def printMenu():
    print("\nWelcome! Accident Manager Program(xml version)")
    print("========Menu========")
    print("Load xml:  1")
    print("Print dom to xml: 2")
    print("Quit program:   3")
    print("print Accident list: 4")
    print("Add new Accident: 5")
    print("Search Accident name: 6")
    print("Make html: 7")
    print("----------------------------------------")
    print("Get book data from Item: 8")
    print("send mail : 9")
    print("Start Web Service: 0")
    print("========Menu==========")
    
def launcherFunction(menu):
    if menu == '1':
        LoadXMLFromFile()
    elif menu == '2':
        PrintDOMtoXML()
    elif menu == '3':
        QuitAccidentMgr()
    elif menu == '4':
        PrintAccidentList(["name", ])
    elif menu == '5':
        continent = str(input('insert continent : '))
        name = str(input('insert name : '))
        AddAccident({'continent':continent, 'name':name})
    elif menu == '6':
        keyword = str(input('input keyword to search : '))
        printAccidentList(SearchAccidentTitle(keyword))
    elif menu == '7':
        keyword = str(input('input keyword code to the html : '))
        html = MakeHtmpDoc(SearchAccidentTitle(keyword))
        print("-----------------")
        print(html)
        print("-----------------")
    elif menu == '8':
        continent = str(input('input continent to get : '))
        ret = getAccidentDataFromCONTINENT(continent)
        AddAccident(ret)
    elif menu == '9':
        sendMain()
    elif menu == '0':
        startWebService()
    else:
        print("error : unknown menu key")
        
def QuitAccidentMgr():
    global loopFlag
    loopFlag = 0
    AccidentFree()
    
##### 작동 #####
while(loopFlag > 0):
    printMenu()
    menuKey = str(input('select menu : '))
    launcherFunction(menuKey)
else:
    print("Thank you! Good Bye")

        
        