import datetime
import re
import ast

def validateDict(data:dict):
    newDict = dict()
    for key in data:
        if emailValidate(data[key]):
            newDict[key] = 'email'
        elif dateValidate(data[key]):
            newDict[key] = 'date'
        elif phoneValidate(data[key]):
            newDict[key] = 'phone'
        else:
            newDict[key] = strValidate(data[key])
    return newDict

def strValidate(data:str):
    try:
        return type(ast.literal_eval(data)).__name__
    except:
        return type(data).__name__

def emailValidate(email:str):
    if type(email) == str and re.match(r'[^@]+@[^@]+\.[^@]+', email):
        return True
    return False

def phoneValidate(phone:str):
    if type(phone) == str and re.match(r'[+][7] \d{3} \d{3} \d{2} \d{2}', phone):
        return True
    return False

def dateValidate(date:str):
    try:
        datetime.datetime.strptime(date, '%Y-%m-%d')
        return True
    except (ValueError, TypeError):
        return False
    except:
        datetime.datetime.strptime(date, '%d.%m.%Y')
        return True