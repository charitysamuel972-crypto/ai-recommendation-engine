from fastapi import FastAPI

app = FastAPI(
    title="AI Recommendation Engine",
    description="An intelligent system for personalized recommendations",
    version="1.0.0"
)

@app.get("/")
def home():
    return {
        "message": "Welcome to the AI Recommendation Engine!",
        "status": "Backend is running successfully"
    }