
from fastapi import FastAPI, HTTPException

from app.routes.items import items
from app.routes.interactions import router as interactions_router
from app.routes.recommendations import router as recommendations_router

app = FastAPI(
    title="AI Recommendation Engine",
    description="An intelligent system for personalized recommendations",
    version="1.0.0"
)

# Connect application modules
app.include_router(interactions_router)
app.include_router(recommendations_router)

@app.get("/")
def home():
    return {
        "message": "Welcome to the AI Recommendation Engine!",
        "status": "Backend is running successfully"
    }

# Retrieve all catalog items
@app.get("/items")
def get_items():
    return items

# Retrieve an individual item
@app.get("/items/{item_id}")
def get_item(item_id: int):
    for item in items:
        if item["id"] == item_id:
            return item

    raise HTTPException(
        status_code=404,
        detail="Item not found"
    )