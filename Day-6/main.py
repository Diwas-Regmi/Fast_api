from fastapi import FastAPI
from exceptions import (PincodeNotFoundError, pincode_not_found_handler)

app = FastAPI(
    title = "Pincode Lookup API",
    description="Autofill city and space from indian pincode during checkout"
)
@app.get("/")
def root():
    return {"message": "Pincode lookup api"}