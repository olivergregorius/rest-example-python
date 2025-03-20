import uvicorn
from fastapi import FastAPI

from app.routes import customers

app = FastAPI()
app.include_router(customers.router)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
