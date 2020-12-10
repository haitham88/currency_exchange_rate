from fastapi import FastAPI
import uvicorn
from app.routers import currencies


app = FastAPI()
app.include_router(currencies.router)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=3000)