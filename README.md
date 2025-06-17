# Run the program
```
uvicorn main:app reload
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
└── main.py                        # Orchestrate session, receive user input
