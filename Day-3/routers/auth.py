import uvicorn
from fastapi import APIRouter

router = APIRouter()

@router.get('/auth/')
async def get_user():
    return {'user': 'authenticated'}

#
# if __name__ == "__main__":
#     uvicorn.run("auth:app",
#                 host = '127.0.0.1',
#                 port = 8000,
#                 reload=True)