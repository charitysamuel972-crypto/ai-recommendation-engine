
from fastapi import APIRouter, Query

from app.routes.items import items
from app.routes.interactions import interactions

router = APIRouter(
    prefix="/recommendations",
    tags=["Recommendations"]
)

# Assign scores to different interaction types
def calculate_interaction_score(interaction):
    interaction_type = interaction["interaction_type"]

    if interaction_type == "view":
        return 1

    if interaction_type == "click":
        return 2

    if interaction_type == "rating":
        rating = interaction.get("rating")

        rating_scores = {
            1: -3,
            2: -2,
            3: 0,
            4: 2,
            5: 3
        }

        return rating_scores.get(rating, 0)

    return 0

# Generate personalised recommendations
@router.get("/{user_id}")
def get_recommendations(
    user_id: str,
    limit: int = Query(default=5, ge=1, le=20)
):

    # Find all interactions belonging to the user
    user_interactions = [
        interaction
        for interaction in interactions
        if interaction["user_id"] == user_id
    ]

    # Cold-start handling for users with no interactions
    if not user_interactions:
        return {
            "user_id": user_id,
            "message": "No interaction history found. Showing popular items.",
            "preferred_categories": [],
            "category_scores": {},
            "recommendations": [
                {
                    **item,
                    "reason": "Suggested as a starting recommendation for a new user."
                }
                for item in items[:limit]
            ]
        }

    # Track items the user has already interacted with
    interacted_item_ids = {
        interaction["item_id"]
        for interaction in user_interactions
    }

    # Calculate scores for each category
    category_scores = {}

    for interaction in user_interactions:

        item = next(
            (
                item for item in items
                if item["id"] == interaction["item_id"]
            ),
            None
        )

        if item is None:
            continue

        category = item["category"]

        score = calculate_interaction_score(interaction)

        category_scores[category] = (
            category_scores.get(category, 0) + score
        )

    # Identify categories with positive scores
    preferred_categories = [
        category
        for category, score in category_scores.items()
        if score > 0
    ]

    # Generate recommendations with explanations
    recommended_items = []

    for item in items:

        if item["id"] in interacted_item_ids:
            continue

        category = item["category"]
        score = category_scores.get(category, 0)

        if score > 0:
            recommended_items.append({
                **item,
                "recommendation_score": score,
                "reason": (
                    f"You showed interest in {category} items "
                    "through your previous interactions."
                )
            })

    # Rank recommendations from highest to lowest score
    recommended_items.sort(
        key=lambda item: item["recommendation_score"],
        reverse=True
    )

    # Apply the requested recommendation limit
    recommended_items = recommended_items[:limit]

    return {
        "user_id": user_id,
        "preferred_categories": preferred_categories,
        "category_scores": category_scores,
        "recommendations": recommended_items
    }