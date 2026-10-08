from pydantic import BaseModel

class MenuItem(BaseModel):
    id: int
    name:str
    category:str
    # price: float
    description:str
    available : bool

class MenuResponse(BaseModel):
    status : str  = "success"
    count : int
    items : list[MenuItem]

