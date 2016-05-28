# -*- coding: cp949 -*-
from xmlAccident import *
from http.client import HTTPConnection
from http.server import BaseHTTPRequestHandler, HTTPServer

##global
conn = None
regKey = 'BrS5flwzIznCPz8iKRmQUWehNDm%2FGI9dCqieoD%2B6qH%2BKT77TYm8vVQ0me49Y1LYejkHnkEPAil7eeESY6WQCcA%3D%3D'
server = "apis.data.go.kr"
#host 
#port



def userURIBuilder(server, **user):
    str = "http://" + server + "/1262000/AccidentService/getAccidentList" + "?"
    for key in user.keys():
        str += key + "=" + user[key] + "&"
    return str

    
def connectOpenAPIServer():
    global conn, server
    conn = HTTPConnection(server)


def getAccidentDataFromContinent(continent):
    global server, regKey, conn
    if conn == None:
        connectOpenAPIServer()
        uri = userURIBuilder(server, servicekey = regKey)
        conn.request("GET", uri)
        req = conn.getresponse()
        print(req.status)
        if int(req.status) == 200:
            print("Book data downloading complete!")
            return extractAccidentData(req.read())
        else:
            print("OpenAPI request has been failed!! please retry")
            return None
            
  
def extractAccidentData(strXml):
    from xml.etree import ElementTree
    tree = ElementTree.fromstring(strXml)
    print(strXml)
    
    itemElements = tree.getiterator("item")
    print(itemElements)
    for item in itemElements:
        continent = item.find("continent")
        name = item.find("name")
        print(name)
        if len(name.text) > 0:
            return {"continent":continent.text, "name":name.text}