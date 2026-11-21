
from fastapi import APIRouter, HTTPException

from app.routes.items import items
from app.routes.interactions import interactions

router = APIRouter(
    prefix="/recommendations",
    tags=["Recommendations"]
)

# Generate recommendations based on a user's interactions
@router.get("/{user_id}")
def get_recommendations(user_id: str):

    # Find items the user has interacted with
    user_interactions = [
        interaction
        for interaction in interactions
        if interaction["user_id"] == user_id
    ]

    if not user_interactions:
        raise HTTPException(
            status_code=404,
            detail="No interactions found for this user"
        )

    # Collect categories of items the user has viewed or clicked
    preferred_categories = []

    for interaction in user_interactions:
        if interaction["interaction_type"] in ["view", "click"]:
            for item in items:
                if item["id"] == interaction["item_id"]:
                    if item["category"] not in preferred_categories:
                        preferred_categories.append(item["category"])

    # Find other items in the preferred categories
    recommended_items = [
        item
        for item in items
        if item["category"] in preferred_categories
        and item["id"] not in [
            interaction["item_id"]
            for interaction in user_interactions
        ]
    ]

    return {
        "user_id": user_id,
        "recommendations": recommended_items
    }