# LangCraft: German Idiom Learning App

LangCraft is an interactive web application for learning German idioms through AI-powered exercises, games, and feedback. It leverages modern LLMs (Large Language Models) to generate idioms, evaluate user input, and create engaging language activities.

---

## Features

- **Idiom Generation:** Generate German idioms by topic and level.
- **Matching Exercises:** Practice matching idioms to their meanings.
- **Usage Feedback:** Get AI feedback on your example sentences.
- **Correct Usage Game:** Identify correct and incorrect idiom usage.
- **Session Memory:** Track user progress and session history.
- **Modern UI:** Responsive, user-friendly interface.

---

## Project Structure

```
idiom_game/
│
├── chains/
│   ├── generate_idioms.py         # LLMChain for generating idioms
│   ├── sentence_feedback.py       # Chain to evaluate learner sentences
│   ├── match_translation.py       # Function/tool to generate matching pairs
│   └── correct_usage_game.py      # LLMChain that gives 3 examples (2 wrong, 1 correct)
│
├── prompts/
│   ├── generate_prompt.txt
│   ├── feedback_prompt.txt
│   └── usage_check_prompt.txt
│
├── memory/
│   └── idiom_memory.py            # Store and fetch current idioms
│
├── utils/
│   └── router.py                  # Routes to different chains based on user action
│
├── main.py                        # Orchestrate session, receive user input
│
├── templates/                     # HTML templates for FastAPI/Jinja2
│
├── static/                        # CSS and JS files
│
├── api/
│   ├── endpoints.py               # FastAPI endpoints
│   └── schemas.py                 # Pydantic models
│
├── notebooks/                     # Jupyter notebooks for prototyping
│
└── .env                           # Environment variables (API keys, etc.)
```

---

## Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/langcraft.git
cd langcraft
```

### 2. Install dependencies

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

### 3. Set up environment variables

Create a `.env` file in the project root with your API keys:

```
OPENAI_API_KEY=sk-...
MISTRAL_API_KEY=...
HUGGINGFACE_API_KEY=...
```

### 4. Run the app

```bash
uvicorn main:app --reload
```

Visit [http://localhost:8000](http://localhost:8000) in your browser.

---

## Usage

- **Generate Idioms:** Choose topic and level, then generate idioms.
- **Practice:** Try matching exercises and sentence feedback.
- **Track Progress:** Your session history is saved for personalized learning.

---

## License

This project is licensed under the [MIT License](LICENSE)