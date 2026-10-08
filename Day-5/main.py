
from fastapi import FastAPI,Query,HTTPException
from models import MenuItem, MenuResponse
from data import menu_items
app = FastAPI(
    title="chai point menu API",
    description="read only menu API for kiosk displays and mobile app")


@app.get("/")
def root():
    return {"message": "welcome to chai point menu api"}

@app.get("/menu", response_model = MenuResponse)
def get_menu(category :str | None = Query(None, description = "Filter by chai, snacks, or combos")):
    if category:
        filtered = [item for item in menu_items if item["category"] == category.lower()]
        if not filtered:
            raise HTTPException(status_code=404, detail=f"no item found in category : {category}")
        return MenuResponse(count=len(filtered), items=filtered)

    # Return all items when no category parameter is provided
    return MenuResponse(count=len(menu_items), items=menu_items)

@app.get("/menu/{item_id}", response_model=MenuItem)
def get_item(item_id: int):
    for item in menu_items:
        if item["id"] == item_id:
            return item
    raise HTTPException(status_code=404, detail=f"Menu item with item : {item_id} not found.")