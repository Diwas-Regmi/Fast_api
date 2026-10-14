from fastapi import FastAPI
from exceptions import (PincodeNotFoundError, pincode_not_found_handler, InvalidPinCodeError, invalid_pincode_handler)
from models import LocationResponse, BulkResponse, BulkRequest
from data import pincode_db
app = FastAPI(
    title = "Pincode Lookup API",
    description="Autofill city and space from indian pincode during checkout"
)

#register your custom exception handler
app.add_exception_handler(PincodeNotFoundError,pincode_not_found_handler)
app.add_exception_handler(InvalidPinCodeError, pincode_not_found_handler())


@app.get("/")
def root():
    return {"message": "Pincode lookup api"}

@app.get("/pincode/{code}, response_model = LocationResponse")
def lookup_pincode(code:str):
    if len(code) != 6 or not code.isdigit():
        raise InvalidPinCodeError(code, "must be exactly 6 digit")
    if code not in pincode_db:
        raise PincodeNotFoundError(code)

    return pincode_db[code]