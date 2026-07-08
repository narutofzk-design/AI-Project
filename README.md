# AI-Powered Student Study Assistant

A web-based study assistant prototype built with Python and Flask. This project demonstrates simple AI techniques (keyword matching, frequency-based scoring, randomized quiz generation, and proportional scheduling) without requiring any external AI/ML libraries.

## Features

1. **Study Chatbot** - An interactive chatbot that uses keyword matching to provide study tips, exam advice, time management strategies, and emotional support.

2. **Study Planner** - Generates a personalized study schedule by distributing total study hours proportionally across subjects and days.

3. **Quiz Generator** - Multiple-choice quizzes on various topics (Python, Science, Math, Study Skills) with random question selection and automatic scoring.

4. **Text Summarizer** - Extractive text summarization using word frequency scoring. Extracts the most important sentences from any input text.

## Tech Stack

- **Backend:** Python 3 + Flask
- **Frontend:** HTML + Jinja2 templates + CSS + Bootstrap 5 (CDN)
- **Session Storage:** Flask's built-in signed cookie sessions (no database needed)
- **AI Logic:** Pure Python (no external AI/ML libraries)

## Folder Structure

```
study_assistant/
├── app.py                    # Flask app + all routes
├── requirements.txt          # Python dependencies
├── test_app.py               # Automated test script
├── logic/
│   ├── __init__.py           # Package marker
│   ├── chatbot_logic.py      # Keyword-matching responses
│   ├── planner_logic.py      # Study schedule generator
│   ├── quiz_logic.py         # Question bank + scoring
│   └── summarizer_logic.py   # Text summarization algorithm
├── templates/
│   ├── base.html             # Shared layout (navbar, footer, CSS/JS links)
│   ├── home.html             # Dashboard with 4 feature cards
│   ├── chatbot.html          # Chat interface (AJAX-powered)
│   ├── planner.html          # Planner form + schedule display
│   ├── quiz.html             # Quiz start, questions, and results
│   └── summarizer.html       # Text input + summary output
└── static/
    └── style.css             # Custom stylesheet
```

## Installation & Setup

### Prerequisites
- Python 3.8 or higher installed on your system

### Steps

1. **Clone or download** the project folder:
   ```
   cd study_assistant
   ```

2. **Create a virtual environment** (recommended):
   ```
   python -m venv venv
   ```

3. **Activate the virtual environment:**
   - Windows: `venv\Scripts\activate`
   - macOS/Linux: `source venv/bin/activate`

4. **Install dependencies:**
   ```
   pip install -r requirements.txt
   ```

5. **Run the application:**
   ```
   python app.py
   ```

6. **Open in browser:**
   ```
   http://127.0.0.1:5000
   ```

## Routes

| Route | Method | Purpose |
|-------|--------|---------|
| `/` | GET | Home dashboard with links to all 4 tools |
| `/chatbot` | GET | Render chat interface |
| `/chatbot/ask` | POST | Receive user message, return bot reply (JSON) |
| `/planner` | GET | Show planner form |
| `/planner/generate` | POST | Generate study schedule |
| `/quiz` | GET | Show quiz start screen, pick topic |
| `/quiz/start` | POST | Generate quiz questions, store answers in session |
| `/quiz/submit` | POST | Compare answers to session, return score |
| `/summarizer` | GET | Show text input form |
| `/summarizer/generate` | POST | Run summarization, return summary |

## How Each Feature Works (AI Logic)

### Chatbot (`chatbot_logic.py`)
- Lowercases user input and checks against a dictionary of keyword-to-response pairs
- Longer keywords are checked first to avoid partial matches
- If no keyword matches, returns a cycling fallback response
- Chat history stored in `session['chat_history']`

### Study Planner (`planner_logic.py`)
- Takes subjects, total hours, and number of days as input
- Distributes hours proportionally using simple division
- Adds slight variation on alternate days (only when enough hours available)
- Returns a structured schedule with time blocks starting at 9:00 AM

### Quiz Generator (`quiz_logic.py`)
- Static `QUESTION_BANK` dictionary organized by topic
- `random.sample()` picks N questions without repeats
- Correct answers stored in `session['quiz_answers']` on quiz start
- On submit, compares user answers against session data and calculates score

### Text Summarizer (`summarizer_logic.py`)
- Classic extractive summarization algorithm:
  1. Split text into sentences
  2. Calculate word frequency (excluding stopwords)
  3. Score each sentence by sum of its word frequencies
  4. Normalize scores by sentence length (square root)
  5. Return top N sentences in original order

## Running Tests

```
python test_app.py
```

This will test all GET and POST routes and verify they return status 200.

## Group Members

| Name | Role |
|------|------|
| Member 1 | Backend (app.py, routes) |
| Member 2 | AI Logic (chatbot, summarizer) |
| Member 3 | AI Logic (planner, quiz) |
| Member 4 | Frontend (templates, CSS) |

## License

This project is for educational purposes (university group project).
