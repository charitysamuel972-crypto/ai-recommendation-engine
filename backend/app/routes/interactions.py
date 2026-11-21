
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field
from typing import Literal

from app.routes.items import items

router = APIRouter(
    prefix="/interactions",
    tags=["Interactions"]
)

# Temporary storage for user interactions
interactions = []

# Structure of an interaction
class Interaction(BaseModel):
    user_id: str
    item_id: int
    interaction_type: Literal["view", "click", "rating"]
    rating: float | None = Field(default=None, ge=1, le=5)

# Record a new interaction
@router.post("/")
def record_interaction(interaction: Interaction):

    # Check whether the item exists
    item_exists = any(
        item["id"] == interaction.item_id
        for item in items
    )

    if not item_exists:
        raise HTTPException(
            status_code=404,
            detail="Item not found"
        )

    # Require a rating when the interaction type is rating
    if interaction.interaction_type == "rating" and interaction.rating is None:
        raise HTTPException(
            status_code=400,
            detail="A rating is required for rating interactions"
        )

    # Save the interaction
    interactions.append(interaction.model_dump())

    return {
        "message": "Interaction recorded successfully",
        "interaction": interaction
    }

# Retrieve all recorded interactions
@router.get("/")
def get_interactions():
    return interactions