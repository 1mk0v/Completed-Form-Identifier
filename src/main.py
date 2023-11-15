from fastapi import FastAPI, Request 
from validators import validateDict
from utils import isSubsetList, getSubsetDict
from Database.database import (
    database as db
)


app = FastAPI(
    title='Completed Form Identifier'
)

def getTemplatesNames(template:dict, fromData:dict):
    result = list()
    for i in fromData:
        validatedDBForm = validateDict(i)
        if isSubsetList(validatedDBForm.keys(), template.keys()) \
            and validatedDBForm == getSubsetDict(template, validatedDBForm):
                result.append(i['name'])
    if len(result) == 0:
        result = template
    return result


@app.post('/get_form')
async def getForm(request:Request):
    responseForm = dict(request.query_params)
    validateResponseForm = validateDict(responseForm)
    return getTemplatesNames(validateResponseForm, db.all())