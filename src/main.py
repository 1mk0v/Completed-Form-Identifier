from fastapi import FastAPI, Request 
from validators import validateDict
from Database.database import (
    database as db,
    templates
)

app = FastAPI(
    title='Completed Form Identifier'
)

@app.post('/get_form')
async def getForm(
    request:Request
):
    dictForm = dict(request.query_params)
    validatedForm = validateDict(dictForm)
    for i in db.all():
        validatedDBElement = validateDict(i)
        if set(validatedDBElement.keys()).issubset(set(validatedForm.keys())):
            print("TRUE")
    return dictForm