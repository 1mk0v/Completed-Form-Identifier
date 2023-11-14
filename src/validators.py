import datetime
import email_validator
import phonenumbers
from phonenumbers import carrier
from phonenumbers.phonenumberutil import number_type
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
    try:
        email_validator.validate_email(email)
        return True
    except:
        return False

def phoneValidate(phone:str):
    try:
        return carrier._is_mobile(
            number_type(phonenumbers.parse(phone))
        )
    except:
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