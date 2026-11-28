
# AI Recommendation Engine

## Project Overview

The AI Recommendation Engine is a full-stack application designed to provide personalized recommendations based on user interactions and item similarities.

The system aims to help users discover relevant products, courses, articles, and other content through intelligent recommendation techniques.

## Project Objectives

- Build an item catalog where users can browse available items.
- Track user interactions such as views and clicks.
- Generate personalized recommendations.
- Provide popular-item suggestions for new users.
- Implement content-based filtering and collaborative filtering.
- Explain why particular items are recommended.
- Measure recommendation performance and accuracy.

## Technology Stack

### Frontend
- Next.js
- React

### Backend
- Python
- FastAPI
- Uvicorn

### Machine Learning and Data Processing
- scikit-learn
- pandas
- sentence-transformers

### Database
- PostgreSQL
- pgvector

### Performance
- Redis

## Project Structure

```text
ai-recommendation-engine/
├── frontend/
├── backend/
│   ├── app/
│   │   ├── main.py
│   │   ├── routes/
│   │   ├── models/
│   │   └── services/
│   └── requirements.txt
├── database/
├── docs/
├── README.md
└── .gitignore
```

## Current Development Status

The initial development environment has been configured.

Completed:
- Project directory initialized.
- Python virtual environment created.
- FastAPI and Uvicorn installed.
- Initial FastAPI application created.
- Backend server tested successfully.
- Git repository initialized.
- GitHub repository connected.
- Initial project commit pushed.

## Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/charitysamuel972-crypto/ai-recommendation-engine.git
```

### 2. Navigate into the project

```bash
cd ai-recommendation-engine
```

### 3. Create a virtual environment

```bash
py -m venv venv
```

### 4. Activate the virtual environment

On Windows PowerShell:

```powershell
.\venv\Scripts\Activate.ps1
```

### 5. Install dependencies

```bash
py -m pip install -r backend/requirements.txt
```

### 6. Run the backend server

```bash
py -m uvicorn app.main:app --reload --app-dir backend
```

### 7. Access the application

- API homepage: http://127.0.0.1:8000
- API documentation: http://127.0.0.1:8000/docs

## Development Roadmap

1. Set up the project environment and backend.
2. Develop the item catalog and interaction tracking.
3. Implement content-based recommendations.
4. Add popular-item recommendations for new users.
5. Introduce embeddings and collaborative filtering.
6. Integrate PostgreSQL and pgvector.
7. Implement Redis caching.
8. Develop recommendation explanations and an accuracy dashboard.

## Project Information

**Program:** UNAI TECH Virtual Internship Program 2026

**Domain:** Full Stack Development

**Project:** Project 06 – AI Recommendation Engine

**Developer:** Charity Samuel Etukudo
## Development Update

Day 2 – Phase 1

Git and GitHub configuration verified.
Repository history reviewed.
Local project connected to GitHub.


## Project Architecture and Modules

The AI Recommendation Engine is organized into separate modules to support maintainability, scalability, and efficient development.

### Main Modules

1. **Frontend:** Provides the user interface for browsing items and viewing recommendations.
2. **Backend API:** Handles requests and coordinates communication between application components.
3. **Item Catalog:** Manages available products, courses, and articles.
4. **Interaction Tracking:** Records user activities such as views and clicks.
5. **Recommendation Engine:** Generates personalized recommendations.
6. **Filtering Service:** Supports content-based and collaborative filtering.
7. **Database:** Stores application data using PostgreSQL and pgvector.
8. **Caching Service:** Uses Redis to improve retrieval speed.
9. **Evaluation Module:** Measures recommendation performance.

### Project Structure

```text
ai-recommendation-engine/
├── frontend/
├── backend/
│   ├── app/
│   │   ├── routes/
│   │   ├── models/
│   │   ├── services/
│   │   └── main.py
│   └── requirements.txt
├── database/
├── docs/
│   └── architecture.md
├── README.md
└── .gitignore
```

### Architecture Documentation

The system architecture diagram and workflow are documented in:

`docs/architecture.md`

### Development Roadmap

- Backend API development
- Item catalog implementation
- User interaction tracking
- Recommendation algorithm development
- Frontend integration
- Database integration
- Testing and performance evaluation

**Project Status:** Architecture planning and initial backend setup completed. Other modules remain planned for implementation.

## Phase 1 – Day 4: Requirements Analysis

The requirements analysis for the AI Recommendation Engine has been completed.

The document identifies the functional, non-functional and user requirements of the application. It also explains the major features, modules, development priorities and implementation tasks.

### Requirements Documentation

The complete requirements document is available here:

[View Project Requirements](docs/requirements.md)

### Development Priorities

- **Must Have:** Item catalog, backend API, interaction tracking, content-based recommendations, database integration and popular-item fallback.
- **Should Have:** Collaborative filtering, recommendation evaluation and caching.
- **Could Have:** Advanced personalization and additional performance optimization.

### Project Status

Initial project setup, architecture planning and requirements documentation completed. Implementation of the remaining modules is planned.
## Phase 1 - Day 5: First Functional Modules

### Modules Implemented

1. Item Catalog Module
   - Retrieve all available items.
   - Retrieve an individual item using its ID.

2. Interaction Tracking Module
   - Record user views.
   - Record user clicks.
   - Record user ratings.
   - Retrieve all recorded interactions.

### API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| GET | /items | Retrieve all items |
| GET | /items/{item_id} | Retrieve an individual item |
| POST | /interactions/ | Record user interaction |
| GET | /interactions/ | Retrieve all interactions |

### Testing Results

- Item retrieval: Successful
- Individual item retrieval: Successful
- Interaction recording: Successful
- Rating recording: Successful
- Interaction retrieval: Successful

### Current Development Status

The first functional backend modules have been implemented and tested using FastAPI Swagger documentation.

Note: Interaction records are currently stored in temporary memory.

## Phase 1 - Day 6 Progress

### Improvements
- Improved the Interaction Tracking Module.
- Added validation to ensure users can only interact with existing items.
- Added validation to require a rating for rating interactions.

### New Feature: Recommendation Engine
- Developed a recommendation module.
- Uses users' view and click history to identify preferred item categories.
- Recommends other items within those categories.
- Excludes items the user has already interacted with.

### Integration and Testing
- Connected the Recommendation Module to the FastAPI application.
- Tested interaction recording successfully.
- Tested recommendations using a sample user.
- Confirmed that the existing item catalogue still works.
- Verified that invalid item IDs return a 404 error.

### Technical Note
The recommendation engine currently uses a simple rule-based approach. It is not yet a machine learning model. Interaction records are stored temporarily in memory.


## Phase 1 – Weekly Progress Review (Day 7)

### Project Status
The AI Recommendation Engine has progressed from project setup and documentation to a functional FastAPI backend.

### Implemented Features
1. Item Catalog Module
   - Displays all available items.
   - Retrieves individual items by ID.

2. Interaction Tracking Module
   - Records user views, clicks and ratings.
   - Validates item IDs.
   - Requires ratings for rating interactions.

3. Recommendation Engine
   - Uses users' view and click history.
   - Identifies preferred item categories.
   - Recommends other items within matching categories.

### Technologies
- Python
- FastAPI
- Pydantic
- Git and GitHub
- Visual Studio Code

### Current Limitations
- Interaction records are stored temporarily in memory.
- Recommendations use rule-based logic, not machine learning.
- Persistent database storage has not yet been implemented.
- A frontend interface is still pending.

### Next Development Priorities
- Integrate a database for persistent storage.
- Improve recommendation logic.
- Develop a frontend interface.
- Connect the frontend to the backend API.
- Conduct further testing and debugging.

## Phase 1 – Day 8: Recommendation Engine Enhancement

### Overview
The recommendation engine was enhanced to provide more personalised recommendations based on user interactions and ratings.

### Features Implemented

1. **Weighted Interaction Scoring:** Different interaction types receive different scores:
   - View: +1
   - Click: +2
   - 5-star rating: +3
   - 4-star rating: +2
   - 3-star rating: 0
   - 2-star rating: -2
   - 1-star rating: -3

2. **Rating-Based Preferences:** The system uses user ratings to identify positive and negative preferences.

3. **Category-Based Recommendations:** Interaction scores are combined by category to identify user preferences.

4. **Recommendation Ranking:** Recommended items are ranked according to their category scores.

5. **Personalised Explanations:** Each recommendation includes a reason explaining why it was suggested.

6. **Recommendation Limit:** Users can control the number of recommendations returned using the `limit` query parameter. The permitted range is 1–20, with a default of 5.

7. **Cold-Start Handling:** New users without interaction history receive starter recommendations instead of an error response.

8. **Input Validation:** The API validates recommendation limits and rejects values outside the permitted range.

### Testing and Results

The following tests were performed using FastAPI Swagger UI:

| Test | Result |
|---|---|
| Cold-start recommendations | Passed |
| Recording user interactions | Passed |
| Personalised recommendations | Passed |
| Positive rating handling | Passed |
| Negative rating handling | Passed |
| Category score calculation | Passed |
| Recommendation explanations | Passed |
| Recommendation limit | Passed |
| Invalid recommendation limit | Passed |

### Challenges and Limitations

The interaction records are currently stored in temporary in-memory storage. Consequently, interaction data is lost whenever the application restarts.

The recommendation system also uses category-level scoring. Therefore, negative feedback on an item can affect recommendations across its entire category.

### Technical Implementation

The recommendation engine was implemented using Python and FastAPI. The system uses rule-based scoring logic to analyse user interactions and generate recommendations.

No machine-learning model has been trained or integrated at this stage.

### Outcome

The Day 8 enhancement improved the recommendation engine by introducing weighted scoring, rating-based preferences, recommendation ranking, personalised explanations, input validation and cold-start handling.