import json
import datetime
import re

def str_format(value ):
    result = re.match('[a-z]{3}\:[0-9]+$', value)
    if result:
        return True
    else:
        return False

def Date_before(date):
    fmts='%Y-%m-%dT%H:%M:%S'
    date=date[:19] 
    dtimeC = datetime.datetime.now()
    dtimeV = datetime.datetime.strptime(date, fmts) 
    if (dtimeC-dtimeV).days > 7:
        return False
    return True

def msg_type(type):
    arr = ['0000','83','84']
    if type in arr:
        return True
    return False

def Valid_json(myjson):
    try:
        json.loads(myjson)
        return True
    except ValueError as error:
        print("invalid json: %s" % error)
        return False

def InsertJson(data,valid):
    if valid == True:
        insertJsonValid = json.dumps(data)
        print ('insertJsonValid: \n',insertJsonValid ) 
    else:
        insertJsonNotValid = json.dumps(data)        
        print ('insertJsonNotValid: \n',insertJsonNotValid )

s = '[{"transmitter": "abc:123456","msg_time": "2019-07-07T10:26:37.951Z","msg_type": 83,"message": "Hello World"},{"transmitter": "abc:123456","msg_time": "2019-03-15T10:26:37","msg_type": 83,"message": "Hello World"}]'

row = {}
data = {}
jsonNotValid = {}
jsonValid = {}
if Valid_json(s):
    d = json.loads(s)
for row in d :
    valid = True 
    if str_format(row['transmitter']) == False:
        valid =False
        print('transmitter is not valid ',row['transmitter'])
    if Date_before(row["msg_time"])  == False:
        valid= False
        print('msg_time is not valid',str(row["msg_time"]))
    if msg_type(str(row["msg_type"]))  == False:
        valid= False
        print('msg_type is not valid',str(row["msg_type"]))
    data[row["transmitter"]]={"transmitter": row["transmitter"],
                              "msg_time": row["msg_time"],
                              "msg_type":row["msg_type"] ,
                              "message": str(row["message"] )} 
    if valid == True:
        jsonValid = json.dumps(data) 
    else:
        jsonNotValid = json.dumps(data)  
print ('JsonValid: \n',jsonValid ) 
print ('JsonNotValid: \n',jsonNotValid )

