from fastapi import FastAPI
from fastapi import Request
import uvicorn

app = FastAPI(
    title="Swiggy Order Service",
    description=(
        "Internal API for managing orders"
        "Handle creation, tracking of delivery systems"
    ),
    version="1.2.1",
    docs_url="/docs",
    redoc_url= "/redoc",
    openapi_url="/openapi.json"
)

@app.get("/")
def read_root():
    """Root Endpoint - Health Check"""
    # FastAPI converts this dict to json
    return {"message": "Welcome to swiggy Order Service", "status":"healthy"}


@app.get("/about")
def about():
    """returns api metadata"""
    return {"service":"order-service",
            "team":"backend platform",
            "region": "ap-south-1",
            "version": "1.2.2"
            }

@app.get("/orders")
def list_orders():
    """list recent orders"""
    return {
        "orders": [
            {
                "id":1,
                "item":"butterchicken",
                "status": "delivered"
            },
            {
                "id":2,
                "item":"dal bhat",
                "status": "preparing"
            },
            {
                "id":3,
                "item":"momo",
                "status": "delivered"
            },
        ]
    }
@app.get("/orders/status")
def order_status():
    """get order status"""
    return {
        "total_today":2_340_23,
        "top_city": "Bangaluru",

    }

@app.get("/debug/request-info")
async def request_info(request:Request):
    """inspect the raw request object"""
    return {
        "method": request.method,
        "url": str(request.url),
        "headers": dict(request.headers),
        "path_params": request.path_params,
        "query_params": dict(request.query_params),
    }
@app.get("orders/active",summary="Get Active Orders",
         description=(
                 "Returns all orders that are currently being prepared"
                 " or are out for delivery"
         ),
         tags = ["orders"],
         response_description="List of active order objects",
         deprecated=False
         )
def get_active_order():
    """this docstring also appears in docs"""
    return {"active_orders":[
        {"id":1, "item": "masala dosa", "status":"Out for delivery"}
    ]
    }
@app.get("/restaurants", tags = ["Restaurants"])
def list_restro():
    """another docstring for another endpoint"""
    return {
        "restaurants": [
            {"test": "test"}
        ]
    }
@app.get("/restaurants/delhi", tags = ["Restaurants"])
def list_restro_delhi():
    """another docstring for another endpoint"""
    return {
        "restaurants": [
            {"test": "test"}
        ]
    }