from fastapi import FastAPI

app = FastAPI(
    title = "Pincode Lookup API",
    description="Autofill city and space from indian pincode during checkout"
)
@app.get("/")
def root():
    return {"message": "Pincode lookup api"}